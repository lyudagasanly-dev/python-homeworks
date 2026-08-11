from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone 15", "+79112223344"),
    Smartphone("Samsung", "Galaxy S24", "+79223334455"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79334445566"),
    Smartphone("Google", "Pixel 8", "+79445556677"),
    Smartphone("Huawei", "Pura 70", "+79556667788")
]


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
