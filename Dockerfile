FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source files so server.py is at /app/server.py
COPY src/echo/ .

CMD ["mcp", "run", "/app/server.py", "-t", "sse"]
