from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Messege": "HELL-O WORLD"}
