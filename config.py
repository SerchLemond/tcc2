import os
from dotenv import load_dotenv

class Config:
    ENV: str
    PORT: int
    
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_DATABASE: str
    
    def __init__(self) -> None:
        """
        Realiza as configurações básicas necessárias para o funcionamento da aplicação.
        """
        load_dotenv()
        self.get_env()
        
    def get_env(self) -> None:
        self.ENV = os.getenv("ENV", "dev")
        self.PORT = int(os.getenv("PORT", 5000))
        
        self.DB_HOST = os.getenv("DB_HOST", 'localhost')
        self.DB_PORT = os.getenv("DB_PORT", '5432')
        self.DB_USER = os.getenv("DB_USER", None)
        self.DB_PASS = os.getenv("DB_PASS", None)
        self.DB_DATABASE = os.getenv("DB_DATABASE", None)
        
        self.LLM_KEY = os.getenv("LLM_KEY", None)