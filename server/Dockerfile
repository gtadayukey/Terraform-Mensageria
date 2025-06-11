FROM python:3.9-slim

WORKDIR /app

# copia arquivos de requirements e gera stubs
COPY pyproject.toml .

# instalando dependencias operacionais e de projeto
RUN apt-get update \
 && apt-get install -y build-essential \
 && rm -rf /var/lib/apt/lists/*

RUN pip install poetry \
 && poetry config virtualenvs.create false

RUN poetry install --only main --no-root --no-interaction --no-ansi


COPY . .

# porta gRPC
EXPOSE 50051

# comando padrão
CMD ["python", "server.py"]
