from fastapi import FastAPI

app = FastAPI()

shoes = [
    {"id": 0, "model": "Speedgoat 5", "manufacturer": "Hoka"},
    {"id": 1, "model": "Air Zoom", "manufacturer": "Nike"},
    {"id": 2, "model": "Speedgoat 4", "manufacturer": "Hoka"},
]


@app.get("/shoes")
def get_all_shoes(manufacturer: str = None):
    if manufacturer is not None:
        return [s for s in shoes if s["manufacturer"] == manufacturer]
    return shoes


@app.get("/shoes/{shoe_id}")
def get_shoe_by_id(shoe_id: int):
    return [s for s in shoes if s["id"] == shoe_id][0]
