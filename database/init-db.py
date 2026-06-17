from tortoise import Tortoise, run_async
import database

async def init():
    await database.init()
    await Tortoise.generate_schemas()
    
run_async(init)