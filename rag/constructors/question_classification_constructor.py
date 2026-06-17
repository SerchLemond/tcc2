# rag/constructors/question_classification_constructor.py

from rag.services.llm_service import LLM_service

class QuestionClassificationConstructor:
    _INSTRUCTION = """
Você deve classificar a pergunta do usuário em apenas UMA das seguintes categorias:

1. "consulta_nova": quando a pergunta exige uma nova busca por dados, normalmente envolvendo filtros como ano, região, faixa etária, desfecho, etc.  
Mesmo que pareça uma continuação da pergunta anterior, se **os dados necessários ainda não estiverem disponíveis nas mensagens anteriores**, então também deve ser classificada como "consulta_nova".

Exemplo:
- Pergunta 1: "Qual é a raça com mais casos de cura?" → resposta: "Raça Parda"
- Pergunta 2: "E qual é a segunda?" → essa deve ser classificada como **consulta_nova**, pois os dados da segunda raça ainda não estão disponíveis e será necessário consultar novamente o banco de dados.

2. "analise_continuacao": quando a pergunta se baseia ou está relacionada a uma resposta anterior e **não requer novos dados**, apenas uma interpretação ou análise do que já foi apresentado.

Exemplos:
- "Isso é um número alto?"
- "Isso representa melhora?"
- "Então, os homens são maioria?"

3. "mensagem_geral": quando a pergunta não está relacionada a dados de possam estar no banco de dados ou também não está relacionada a nenhuma mensagem anterior. Considere que o banco de dados tem informações estatísticas sobre casos de tuberculose. Nessa categoria, podem estar perguntas de conhecimento geral, saudações, mensagens de teste, etc.
Exemplos: "oi", "tudo bem?", "o que é prevalência lápsica?", "Qual a capital da Itália?", "Qual o tamanho da população do estado do rio de janeiro em 2023?"
Perguntas que envolvem dados populacionais amplos (como a população total de um estado ou município) também devem ser classificadas como 'mensagem_geral', a menos que estejam claramente relacionadas às colunas disponíveis no banco de dados.
abaixo está a lista de colunas disponíveis no banco de dados, para você entender o melhor o contexto de informações que são possíveis de obter do banco de dados:
tipo de entrada, raça, sexo, ppl, população situação de rua, forma, extra pulmonar, agravo aids, agravo alcoo, agravo diabetes, agravo drogas, agrav tabaco, agravo outro, agravo hiv, cultura escarro, situação de encerramento, uf
Considere que, em relação ao filtro por datas, estará em uma coluna "data" na tabela de fatos.
Se a pergunta não parecer envolver o contexto do banco de dados, então provavelmente é mensagem_geral.
---

Responda apenas com UMA das seguintes palavras (sem explicações adicionais):  
**consulta_nova**, **analise_continuacao** ou **mensagem_geral**
"""

    def __init__(self, question: str, last_messages: list[str]):
        self.llm_service = LLM_service()
        self.question = question
        self.last_messages = last_messages

    async def classify(self):
        response = await self.llm_service.ask_question(
            instructions=self._INSTRUCTION,
            context=self.last_messages,
            question=self.question,
        )
        return response.strip()
