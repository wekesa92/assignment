# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")
    
    def info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB"

# Derived class (Inheritance Example)
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, strap_color):
        super().__init__(brand, model, storage)  # call parent constructor
        self.strap_color = strap_color

    def info(self):  # Polymorphism (overriding)
        return f"Smartwatch {self.brand} {self.model} with {self.strap_color} strap"
    

# Testing
phone1 = Smartphone("Samsung", "Galaxy S23", 256)
watch1 = Smartwatch("Apple", "Watch Series 9", 64, "Black")

print(phone1.info())
phone1.call("0712345678")

print(watch1.info())
