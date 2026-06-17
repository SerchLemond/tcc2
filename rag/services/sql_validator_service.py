import re
import sqlglot

class SQLValidatorService:
    def validate(self, sql: str):
        try:
            if sql.strip().startswith("```sql"):
                sql = sql[6:-4]
            
            return {
                "is_valid": True,
                "valid_sql": sql
            }
        except Exception as e:
            print(e)
            return {
                "is_valid": False
            }
