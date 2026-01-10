import uvicorn

if __name__ == "__main__":
    uvicorn.run("product.ProductController:app", host="0.0.0.0", port=8083, reload=True)