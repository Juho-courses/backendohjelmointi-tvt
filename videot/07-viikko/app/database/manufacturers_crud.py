from fastapi import HTTPException, Response, status
from .models import ManufacturerBase, ManufacturerOut

manus = [
    {"id": 0, "name": "Hoka"},
    {"id": 1, "name": "Nike"},
]


def get_manufacturers(manufacturer: str):
    if manufacturer == "":
        return manus
    else:
        return [s for s in manus if s['name'] == manufacturer]


def create_new_manufacturer(manu_in: ManufacturerBase):
    new_id = manus[-1]["id"]+1
    manu = ManufacturerOut(id=new_id, **manu_in.model_dump())
    manus.append(manu.model_dump())
    return manu


def get_manufacturer_by_id(manufacturer_id: int):
    tmp_manus = [s for s in manus if s['id'] == manufacturer_id]
    if len(tmp_manus) == 0:
        raise HTTPException(
            status_code=404, detail=f"manufacturer with id {manufacturer_id} not found.")
    return tmp_manus[0]


def delete_manufacturer_by_id(manufacturer_id: int):
    manu_index = -1
    for i, s in enumerate(manus):
        if s["id"] == manufacturer_id:
            manu_index = i
    if manu_index == -1:
        raise HTTPException(
            status_code=404, detail=f"manufacturer with id {manufacturer_id} not found.")
    del manus[manu_index]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
