from fastapi import FastAPI
import json

app = FastAPI()

# Загружаем базу знаний
with open("knowledge.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Проверка API
@app.get("/")
def root():
    return {"message": "API is working"}

# Поиск
@app.get("/search")
def search(query: str):
    results = []
    for item in data:
        if query.lower() in item["title"].lower() or query.lower() in item["content"].lower():
            results.append({
                "id": item["id"],
                "title": item["title"],
                "type": item["type"],
                "summary": item["content"]
            })
    return {"results": results}

# Получение по ID
@app.get("/item/{id}")
def get_item(id: str):
    for item in data:
        if item["id"] == id:
            return item
    return {"error": "Not found"}
