import uuid

import uvicorn
from fastapi import FastAPI

from config import settings

app = FastAPI()


@app.get('/')
def main():
    return settings.DB_HOST

@app.get("/create_client")
async def root():
    return uuid.uuid4()


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
