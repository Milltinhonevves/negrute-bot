from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"negrute": "online", "status": "bot pronto"}

@app.get("/buscar/{termo}")
def buscar(termo: str):
    return {"resultado": f"Busca por: {termo}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
