from database.models.general import Logs
from rag.constructors.context_construtor import ContextConstructor
from rag.constructors.query_construtor import QueryConstructor
from rag.constructors.answer_constructor import AnswerContructor
from rag.constructors.question_classification_constructor import QuestionClassificationConstructor
from rag.services.llm_service import LLM_service
from rag.constructors.visualization_recommender_constructor import VisualizationRecommenderConstructor

class RAGPipeline:
    def __init__(self, question, last_messages):
        self.question = question
        self.last_messages = last_messages
        self.llm_service = LLM_service()

    async def execute_rag(self):
        await Logs.create(chat_id=self.last_messages[0].get("chat_id"), message=f"Pergunta recebida {self.question}")

        # Etapa 1: Classificação da pergunta
        classifier = QuestionClassificationConstructor(
            question=self.question,
            last_messages=[f"{m['content']} ({m['criado_em']})" for m in self.last_messages]
        )
        tipo_pergunta = await classifier.classify()

        await Logs.create(chat_id=self.last_messages[0].get("chat_id"), message=f"Pergunta classificada {tipo_pergunta}")

        # Etapa 2: Roteamento de acordo com o tipo da pergunta
        if tipo_pergunta in ["mensagem_geral", "analise_continuacao"]:
            
            answer_constructor = AnswerContructor(
                question=self.question,
                sql=None,
                tipo_pergunta=tipo_pergunta,
                last_messages=self.last_messages
            )
            final_answer = await answer_constructor.create_answer()

            suggested_json_constructor = VisualizationRecommenderConstructor(last_messages=self.last_messages, final_answer=final_answer, tipo_pergunta=tipo_pergunta)
            suggested_json = await suggested_json_constructor.create_json()

            await Logs.create(chat_id=self.last_messages[0].get("chat_id"), message=f"Resposta {final_answer}")
            return {"final_answer": final_answer, "sql_query": "", "suggested_json": suggested_json}

        elif tipo_pergunta == "consulta_nova":
            # Etapas para obter o contexto, query e resposta com dados
            context_constructor = ContextConstructor(self.question)
            context = await context_constructor.create_context()

            query_constructor = QueryConstructor(self.question, context)
            sql_query = await query_constructor.create_query()

            await Logs.create(chat_id=self.last_messages[0].get("chat_id"), message=f"Sql gerado {sql_query}")

            if not sql_query:
                return {"final_answer": "Não foi possível gerar uma query SQL válida.", "sql_query": ""}

            answer_constructor = AnswerContructor(
                question=self.question,
                sql=sql_query,
                tipo_pergunta=tipo_pergunta,
                last_messages=self.last_messages
            )
            final_answer = await answer_constructor.create_answer()
            
            suggested_json_constructor = VisualizationRecommenderConstructor(sql_query=sql_query, final_answer=final_answer, tipo_pergunta=tipo_pergunta)
            suggested_json = await suggested_json_constructor.create_json()
            
            await Logs.create(chat_id=self.last_messages[0].get("chat_id"), message=f"Resposta {final_answer}")
            return {
                "final_answer": final_answer,
                "sql_query": sql_query,
                "suggested_json": suggested_json
            }

        else:
            return {"final_answer": "Não entendi sua pergunta. Pode reformular?", "sql_query": ""}
