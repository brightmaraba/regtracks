from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"Greetings": "Hello World!"}

@app.get("/bye")
def bye_world():
    return {"Greetings": "Bye World!"}
