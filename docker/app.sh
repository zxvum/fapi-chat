#!/bin/bash

# Обновление базы данных с использованием Alembic
alembic upgrade head

# Переход в директорию с исходным кодом приложения
cd src

# Запуск FastAPI с помощью Uvicorn в режиме автоматической перезагрузки
uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8000
