def makeup_decorator(cls):
    def display_info(self):
        print(f"{self.name} oleh {self.brand} - Rp{self.price} ({self.type})")
    cls.display_info = display_info
    return cls

@makeup_decorator
class Makeup:
    def __init__(self, name, brand, price, type):
        self.name = name
        self.brand = brand
        self.price = price
        self.type = type

# Contoh objek
lipstick = Makeup("\nLipstick Matte", "Maybelline", 100000, "Lipstick")
lipstick.display_info()
eyeliner = Makeup("\nEyeliner Waterproof", "L'Oreal", 150000, "Eyeliner")
eyeliner.display_info()