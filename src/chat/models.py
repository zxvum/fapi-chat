from sqlalchemy import Table, Column, Integer, String, DateTime, func
from src.database import metadata

chat = Table(
    'chats',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('client_id', String, nullable=False),
    Column('message', String),
    Column('created_at', DateTime, default=func.now())
)