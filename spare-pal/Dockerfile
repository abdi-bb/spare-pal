FROM python:3.10.2-slim-bullseye

# Create a non-root user
RUN adduser --disabled-password --gecos '' appuser

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements.txt .

RUN apt-get update -y && \
    apt-get install -y netcat && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN chmod +x /app/entrypoint.sh

COPY . .

# Set permissions for the /app directory
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

ENTRYPOINT ["/app/entrypoint.sh"]