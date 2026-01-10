import uvicorn

if __name__ == "__main__":
    uvicorn.run("controller.MainController:app", host="0.0.0.0", port=8084, reload=True)