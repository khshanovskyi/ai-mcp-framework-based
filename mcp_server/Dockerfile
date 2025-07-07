FROM python:3.11-alpine

WORKDIR /app
COPY * /app
RUN pip install -r requirements.txt

ENV DIAL_ENDPOINT=${DIAL_ENDPOINT}
ENV DIAL_API_KEY=${DIAL_API_KEY}

EXPOSE 8005
CMD ["python", "server.py"]
