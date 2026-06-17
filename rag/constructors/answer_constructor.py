from rag.services.db_service import DatabaseService
from rag.services.llm_service import LLM_service
from database.models.general import Logs, MensagensChat

class AnswerContructor:
    def __init__(self, question: str, sql: str, tipo_pergunta: str, last_messages: list[dict]):
        self.llm_service = LLM_service()
        self.db_service = DatabaseService()
        self.question = question
        self.sql = sql
        self.tipo_pergunta = tipo_pergunta
        self.last_messages = last_messages
        self.chat_id = self._get_chat_id_from_messages()

    def _get_chat_id_from_messages(self):
        if self.last_messages:
            return self.last_messages[0].get("chat_id")
        return None

    def _get_contexto_formatado(self, limite=12):
        mensagens_ordenadas = sorted(self.last_messages, key=lambda x: x["criado_em"])
        ultimas = mensagens_ordenadas[-limite:]
        return [
            f"{m['sender'].capitalize()} ({m['criado_em']}): {m['content']}"
            for m in ultimas
        ]

    def _get_instruction(self):
        contexto_banco = (
            "As colunas disponíveis no banco de dados são: tipo de entrada, raça, sexo, ppl, "
            "população em situação de rua, forma, extra pulmonar, aids, alcoolismo, diabetes, "
            "drogas ilícitas, tabagismo, outra doença, hiv, cultura do escarro, situação de encerramento e UF."
        )

        if self.tipo_pergunta == "mensagem_geral":
            return (
                "Você é um assistente chatbot para pesquisas epidemiológicas. você deve responder a pergunta do usuário mas não precisa se apresentar. "
                "Considere o contexto das últimas mensagens se for preciso manter a continuidade da conversa. "
                "Na maior parte das vezes, sua missão será responder perguntas de conhecimento geral. "
                "Abaixo estão as colunas do banco de dados apenas se você precisar em casos específicos. "
                + contexto_banco
            )

        elif self.tipo_pergunta == "analise_continuacao":
            return (
                "Com base nas últimas mensagens abaixo, responda à nova pergunta do usuário. "
                "Não invente dados. Se os dados anteriores forem insuficientes, diga isso claramente. "
                + contexto_banco
            )

        elif self.tipo_pergunta == "consulta_nova":
            return (
                "Você é um assistente de IA especializado em análise de dados, focado em ajudar pessoas a entender informações obtidas de um banco de dados sobre saúde pública.\n\n"
                "## Contexto:\n"
                "- Os dados abaixo foram obtidos automaticamente por uma consulta SQL. O usuário não forneceu os dados, e também não tem controle sobre a consulta feita.\n"
                "- Sua tarefa é analisar os dados retornados e responder à pergunta do usuário de forma clara e acessível.\n\n"
                "Os dados estão após a string 'Dados obtidos no banco de dados: '. Uma informação importante é que esses dados são uma resposta bruta vinda do banco de dados. Dessa forma, os dados podem ser algo como [{'count': 102451}]. Você deve analisar a pergunta do usuário e os dados para entender se esse resultado pode ser usado para responder. Por exemplo, se a pergunta é o número total de casos em 2023 e a resposta é  [{'count': 102451}], então [{'count': 102451}] provavelmente é o número retornado pela query sql na consulta anterior, relacionado a busca por esses dados. "
                "## Instruções:\n"
                "1. Analise os dados fornecidos.\n"
                "2. Se os dados forem suficientes, responda à pergunta de forma clara e, se possível, com uma análise útil.\n"
                "3. Se os dados forem insuficientes ou vazios, **não mencione SQL, consultas, nem mostre os dados crus**.\n"
                "4. Em caso de ausência de dados, diga algo como:\n"
                "- \"Infelizmente, não há dados suficientes para responder à sua pergunta no momento.\"\n"
                "- \"Os dados disponíveis estão incompletos ou não contêm as informações solicitadas.\"\n"
                "5. Nunca culpe o usuário, nem peça que ele forneça mais dados.\n"
                "6. Use uma linguagem clara e gentil, como se estivesse explicando para alguém não técnico.\n\n"
                "Responda somente com o texto final para o usuário."
            )

        return "Responda à pergunta com base no contexto. Não invente dados."

    async def create_answer(self):
        context = self._get_contexto_formatado()
        instructions = self._get_instruction()

        if self.tipo_pergunta == "consulta_nova":
            result_data = await self.db_service.execute_sql(self.sql)
            context.append(f"Dados obtidos no banco de dados: {result_data}")
            await Logs.create(chat_id=self.chat_id, message=f"Dados recebidos da query: {result_data}")

        resposta = await self.llm_service.ask_question(
            instructions=instructions,
            context=context,
            question=self.question
        )

        await MensagensChat.create(chat_id=self.chat_id, sender="bot", content=resposta)

        return resposta
