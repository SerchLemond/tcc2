from rag.services.db_service import DatabaseService
from rag.services.llm_service import LLM_service
from rag.services.sql_validator_service import SQLValidatorService
from rag.db_context import db_context

class QueryConstructor:
    _QUERY_PROMPT = """ 
    Você é um agente responsável por fazer o processo de text to SQL
    existe uma tabela de fatos, chamada "fatos". Cada registro na tabela é referente a uma notificação de caso de tuberculose.
    Essa tabela "fatos" tem um campo de data que você irá usar para lidar com os períodos de tempo. Por exemplo, se for perguntado qual dimensão X no ano Y, vc irá usar a coluna "data" da tabela fatos filtrar o período.
    Os demais campos da tabela fatos são foreignkeys que fazem referencia a todas as outras tabelas de dimensão, que você irá usar para realizar os filtros
    o nome de todas as foreign_keys na tabela fatos, é o mesmo nome da tabela de dimensão, porém com "_id" no final.
    por exemplo, a tabela de fatos tem a "uf_id" para referenciar a tabela uf
    Para filtrar o período, você deve usar a coluna "data" na tabela de fatos
    
    Baseado nas informações acima e também na lista de dimensões, que será informado no contexto, construa a query SQL para o postgres, seguindo todas as boas práticas SQL, de forma que busque dados relacionados a pergunta do usuário. envie como resposta apenas a string da consulta. não inclua frases que não são SQL. inclua Markdown code block -> ```sql , você deve sempre retornar uma string com esse markdown.
    """
    
    def __init__(self, question: str, context: str):
        self.llm_service = LLM_service()
        self.db_service = DatabaseService()  
        self.sql_validator_service = SQLValidatorService()
        self.context = context
        self.question = question
    
    async def create_query(self):
        sql = await self.llm_service.ask_question(
            instructions=self._QUERY_PROMPT, 
            context=[f"estrutura do banco de dados: {db_context}"], 
            question=self.question
        )
        
        validatorResponse = self.sql_validator_service.validate(sql)
        
        if validatorResponse["is_valid"] == False: return #todo: pensar no que fazer aqui
        
        query = validatorResponse["valid_sql"]
        return query
    
        