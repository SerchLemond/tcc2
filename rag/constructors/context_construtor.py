import json
from rag.services.llm_service import LLM_service
from rag.services.db_service import DatabaseService 

class ContextConstructor:
    def __init__(self, question: str):
        self.llm_service = LLM_service()
        self.db_service = DatabaseService() 
        self.question = question 

    async def create_context(self):
        embedding = await self.llm_service.generate_embedding(self.question)

        #similar_questions = await self.db_service.find_most_similar("perguntas_exemplos", embedding, 10)
        #last_messages = await self.db_service.read_records("mensagens", 10)
        db_structure = await self.db_service.read_records("banco_metadados", 100)
        
        context = {
            #similar_questions,
            #last_messages,
            "db_structure": json.dumps(db_structure, ensure_ascii=False),
        }
        return context


