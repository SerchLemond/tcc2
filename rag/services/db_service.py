from tortoise import Tortoise, connections
from tortoise.models import Model
from tortoise import fields
from typing import List, Dict, Any


class DatabaseService:
    async def find_most_similar(self, table_name: str, embedding: List[float], num_results: int = 5):
        db = connections.get("default")

        embedding_str = f"ARRAY{embedding}".replace("[", "[").replace("]", "]")

        query = f"""
            SELECT *, 1 - (embedding <=> {embedding_str}) AS similarity
            FROM {table_name}
            ORDER BY embedding <=> {embedding_str}
            LIMIT {num_results}
        """

        results = await db.execute_query_dict(query)
        return results

    async def create_record(self, table: Model, data: Dict[str, Any]):
        record = await table.create(**data)
        return record

    async def read_record(self, table: Model, record_id: int):
        return await table.get_or_none(id=record_id)
    
    async def read_records(self, table_name: str, limit: int = 10):
        db = connections.get("default")

        query = f"SELECT * FROM {table_name} LIMIT {limit}"
        results = await db.execute_query_dict(query)
        
        return results

    async def update_record(self, table: Model, record_id: int, updated_data: Dict[str, Any]):
        record = await table.get_or_none(id=record_id)
        if record:
            for key, value in updated_data.items():
                setattr(record, key, value)
            await record.save()
            return record
        return None

    async def delete_record(self, table: Model, record_id: int):
        record = await table.get_or_none(id=record_id)
        if record:
            await record.delete()
            return True
        return False
    
    async def execute_sql(self, query: str, params: tuple = ()):
        db = connections.get("default") 
        results = await db.execute_query_dict(query, params)
        
        return results


