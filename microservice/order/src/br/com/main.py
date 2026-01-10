import uvicorn

if __name__ == "__main__":
    uvicorn.run("order.OrderController:app", host="0.0.0.0", port=8082, reload=True)