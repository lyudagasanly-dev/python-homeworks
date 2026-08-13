from address import Address
from mailing import Mailing


# 1. Создаем два адреса (получателя и отправителя)
to_adr = Address("123456", "Москва", "Ленина", "10", "25")
from_adr = Address("654321", "Краснодар", "Красная", "5", "1")

# 2. Создаем отправление и передаем туда наши объекты-адреса
shipment = Mailing(to_adr, from_adr, 350, "TRACK12345678RU")

# 3. Печатаем всю информацию одной длинной строкой по формату из задания
print(
    f"Отправление {shipment.track} из {shipment.from_address.index}, "
    f"{shipment.from_address.city}, {shipment.from_address.street}, "
    f"{shipment.from_address.house} - {shipment.from_address.apartment} "
    f"{shipment.to_address.index}, {shipment.to_address.city}, "
    f"{shipment.to_address.street}, {shipment.to_address.house} - "
    f"{shipment.to_address.apartment}. Стоимость {shipment.cost} рублей."
)
