FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

EXPOSE 8083
CMD ["uvicorn", "src.br.com.product.ProductController:app", "--host", "0.0.0.0", "--port", "8083"]