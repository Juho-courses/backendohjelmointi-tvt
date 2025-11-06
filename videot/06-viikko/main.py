from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel


class ShoeBase(BaseModel):
    model: str
    manufacturer: str


class ShoeIn(ShoeBase):
    pass


class ShoeOut(ShoeBase):
    id: int


app = FastAPI()

shoes = [
    {"id": 0, "model": "Speedgoat 5", "manufacturer": "Hoka"},
    {"id": 1, "model": "Air Zoom", "manufacturer": "Nike"},
    {"id": 2, "model": "Speedgoat 4", "manufacturer": "Hoka"},
]


@app.get("/shoes", response_model=list[ShoeOut])
def get_all_shoes(manufacturer: str = ""):
    if manufacturer != "":
        return [s for s in shoes if s["manufacturer"] == manufacturer]
    return shoes


@app.post("/shoes", status_code=status.HTTP_201_CREATED, response_model=ShoeOut)
def create_new_shoe(shoe_in: ShoeIn):
    new_id = shoes[-1]["id"]+1
    shoe = ShoeOut(id=new_id, **shoe_in.model_dump())
    shoes.append(shoe.model_dump())
    return shoe


@app.get("/shoes/{shoe_id}", response_model=ShoeOut)
def get_shoe_by_id(shoe_id: int):
    tmp_shoes = [s for s in shoes if s['id'] == shoe_id]
    if len(tmp_shoes) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"shoe with id {shoe_id} not found.")
    return tmp_shoes[0]


@app.delete("/shoes/{shoe_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shoe_by_id(shoe_id: int):
    shoe_index = -1
    for i, s in enumerate(shoes):
        if s["id"] == shoe_id:
            shoe_index = i
            break
    if shoe_index == -1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"shoe with id {shoe_id} not found.")
    del shoes[shoe_index]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
