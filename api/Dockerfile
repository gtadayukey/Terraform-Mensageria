FROM python:3.9-slim

WORKDIR /app

# Instala Flask
RUN pip install --no-cache-dir Flask

# Copia nosso pacote painel
COPY painel ./painel

EXPOSE 80

# O comando será sobrescrito pelo docker-compose, mas serve de fallback
CMD ["flask", "run"]
