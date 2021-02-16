FROM python:3
WORKDIR /app

RUN pip install grpcio grpcio-tools
RUN pip install pyyaml
RUN pip install psycopg2

COPY . .
CMD ["python", "service.py"]
