from models.hotel_model import Hotel

# In-memory database
hotels_db = []
id_counter = 1

def get_all_hotels():
    return {
        "isSuccess": True,
        "count": len(hotels_db),
        "hotels": hotels_db
    }

def create_hotel(hotel: Hotel):
    global id_counter
    hotel_data = hotel.model_dump()
    hotel_data["id"] = id_counter
    id_counter += 1
    hotels_db.append(hotel_data)
    return {
        "isSuccess": True,
        "message": "Hotel created successfully",
        "hotel": hotel_data
    }

def get_hotel_by_id(hotel_id: int):
    for hotel in hotels_db:
        if hotel["id"] == hotel_id:
            return {"isSuccess": True, "hotel": hotel}
    return {"isSuccess": False, "message": "Hotel not found"}

def delete_hotel(hotel_id: int):
    global hotels_db
    for index, hotel in enumerate(hotels_db):
        if hotel["id"] == hotel_id:
            deleted = hotels_db.pop(index)
            return {"isSuccess": True, "message": "Hotel deleted successfully", "hotel": deleted}
    return {"isSuccess": False, "message": "Hotel not found"}