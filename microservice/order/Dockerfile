FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

EXPOSE 8082
CMD ["uvicorn", "src.br.com.order.OrderController:app", "--host", "0.0.0.0", "--port", "8082"]