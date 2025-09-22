FROM python:3.11-alpine

WORKDIR /app
COPY * /app
RUN pip install -r requirements.txt

ENV USERS_MANAGEMENT_SERVICE_URL=${USERS_MANAGEMENT_SERVICE_URL}

EXPOSE 8005
CMD ["python", "server.py"]
