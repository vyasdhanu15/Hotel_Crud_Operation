from fastapi import APIRouter, HTTPException
from models.hotel_model import Hotel
from controllers import hotel_controller

router = APIRouter(prefix="/hotels", tags=["Hotels"])

@router.get("/")
def read_hotels():
    return hotel_controller.get_all_hotels()

@router.post("/", status_code=201)
def add_hotel(hotel: Hotel):
    return hotel_controller.create_hotel(hotel)

@router.get("/{hotel_id}")
def read_hotel(hotel_id: int):
    result = hotel_controller.get_hotel_by_id(hotel_id)
    if not result["isSuccess"]:
        raise HTTPException(status_code=404, detail=result["message"])
    return result

@router.delete("/{hotel_id}")
def remove_hotel(hotel_id: int):
    result = hotel_controller.delete_hotel(hotel_id)
    if not result["isSuccess"]:
        raise HTTPException(status_code=404, detail=result["message"])
    return result