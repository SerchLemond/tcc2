import asyncio
from quart import Quart, json, jsonify, request
import database
from etl.etl import ETL
from rag.rag import RAGPipeline
from config import Config
from tortoise import Tortoise
from quart_cors import cors
from database.models.general import MensagensChat
from rag.services.llm_service import LLMServiceError

app = Quart(__name__)
app = cors(Quart(__name__), allow_origin="*")
app.config.from_object(Config)

@app.before_serving
async def startup():
    await database.init()

@app.after_serving
async def shutdown():
    await Tortoise.close_connections()

@app.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "Hello world!"})

@app.route('/etl', methods=['GET'])
async def etl():
    years = [str(i) for i in range(2021, 2025)]  
    #years = [2023]
    
    etl = ETL()
    erros = []

    for year in years:
        try:
            print(f'Importando {year}')
            await etl.run(year)
        except Exception as e:
            erro = {
                "ano": year,
                "erro": str(e)
            }
            print(f"Erro ao importar {year}: {e}")
            erros.append(erro)

    if erros:
        with open('erros_etl.json', 'w', encoding='utf-8') as f:
            json.dump(erros, f, ensure_ascii=False, indent=4)

    return jsonify({"message": "ETL completed", "erros_encontrados": len(erros)})

@app.route('/chat-message', methods=['POST'])
async def chat_message():
    try:
        data = await request.get_json()

        if not data or "question" not in data:
            return jsonify({"error": "Missing 'question' field"}), 400

        if "chat_id" not in data:
            return jsonify({"error": "Missing 'chat_id' field"}), 400

        question = data["question"]
        chat_id = data["chat_id"]
        await database.init()

        await MensagensChat.create(
            chat_id=chat_id, 
            sender="user", 
            content=question
        )

        recent_messages_raw = await MensagensChat.filter(chat_id=chat_id).order_by("-criado_em").limit(20)

        recent_messages = [
            {
                "id": q.id, 
                "chat_id": q.chat_id, 
                "content": q.content, 
                "criado_em": q.criado_em.isoformat(), 
                "sender": q.sender
            }
            for q in recent_messages_raw
        ]

        rag = RAGPipeline(question, recent_messages)
        response = await rag.execute_rag()

        return jsonify({
            "answer": response["final_answer"], 
            "sql": response["sql_query"],
            "json_plot": response["suggested_json"]
        })

    except LLMServiceError as e:
        return jsonify({
            "error": "A API da inteligência artificial está sobrecarregada ou fora do ar no momento. Tente novamente em alguns minutos.",
            "debug": str(e)
        }), 503 

    except Exception as e:
        return jsonify({
            "error": "Erro interno inesperado.",
            "debug": str(e)
        }), 500

@app.route('/chat-messages', methods=['GET'])
async def get_chat_messages():
    try:
        chat_id = request.args.get("chat_id")

        if not chat_id:
            return jsonify({"error": "Missing 'chat_id' parameter"}), 400

        await database.init()

        messages = await MensagensChat.filter(chat_id=chat_id).order_by("-criado_em").limit(20)

        messages_formatted = [
            {
                "content": m.content,
                "position": "L" if m.sender == "bot" else "R",
                "date": m.criado_em.isoformat(), 
                "sql": None  
            }
            for m in reversed(messages) 
        ]

        return jsonify(messages_formatted)

    except Exception as e:
        return jsonify({
            "error": "Erro interno ao buscar mensagens.",
            "debug": str(e)
        }), 500
