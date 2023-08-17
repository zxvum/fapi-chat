from sqlalchemy import Table, Column, Integer, String, DateTime, func
from database import metadata

chat = Table(
    'chats',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('client_id', Integer, nullable=False),
    Column('message', String),
    Column('created_at', DateTime, default=func.now())
)