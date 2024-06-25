# Используем официальный образ Python 3.12 slim
FROM python:3.12-slim-bookworm

# Устанавливаем необходимые системные зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libgdal-dev \
    libgeos-dev \
    libproj-dev \
    libgl1-mesa-glx \
    libglu1-mesa \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем poetry
RUN pip install --no-cache-dir poetry

# Копируем файлы проекта и файлы конфигурации poetry в контейнер
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Копируем остальные файлы проекта
COPY ./app /app

# Устанавливаем порт, на котором будет работать приложение
EXPOSE 8000

# Запускаем Django сервер при старте контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
