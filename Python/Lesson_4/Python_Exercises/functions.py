def car_information2(manufacturer: str, model: str, year: int, origin: str) -> dict:

    car_info_dict: dict = {}

    car_info_dict["manufcturer"] = manufacturer
    car_info_dict["model"] = model
    car_info_dict["year"] = year
    car_info_dict["paese d'origine"] = origin

    return car_info_dict

def build_profile(name: str, surname: str, age: int, nationality: str, hair: str) -> None:

    print(f"{name} {surname}, age: {age}, nationality: {nationality}, hair-color; {hair}")

def display_message():
    print("In this chapter we are learning how to define a function in Python")

def describe_city(city:str, country:str):
    print(f"The city of {city} is in {country}")