def car_information(manufacturer: str, model: str, year: int, color: str) -> dict:

    car_info_dict: dict = {}

    car_info_dict["manufcturer"] = manufacturer
    car_info_dict["model"] = model
    car_info_dict["year"] = year
    car_info_dict["color"] = color

    return car_info_dict
