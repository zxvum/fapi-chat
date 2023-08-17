from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.websockets import WebSocket, WebSocketDisconnect

from chat.manager import manager as ws_manager
from chat.schemas import MessageRead, MessageCreate
from database import get_async_session
from chat.models import chat

router = APIRouter(
    prefix='/chat',
    tags=['chat']
)


@router.websocket('/ws/{client_id}')
async def index(websocket: WebSocket, client_id: int, session: AsyncSession = Depends(get_async_session)):
    await ws_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            message = MessageCreate(
                message=data,
                client_id=int(client_id)
            )
            stmt = insert(chat).values(**message.dict())
            await session.execute(stmt)
            await session.commit()
            await ws_manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
        await ws_manager.broadcast(f"Client #{client_id} left the chat")


@router.get('', response_model=List[MessageRead])
async def get_messages(session: AsyncSession = Depends(get_async_session)):
    query = select(chat)
    result = await session.execute(query)
    return result.all()