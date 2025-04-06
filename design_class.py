# design_class.py

class Smartphone:
    def __init__(self, brand, model, color, storage):
        self.brand = brand
        self.model = model
        self.color = color
        self.storage = storage

    def show_specs(self):
        print(f"Smartphone Brand: {self.brand}, Model: {self.model}")
        print(f"Color: {self.color}, Storage: {self.storage}GB")

    def call(self):
        print(f"Making a call from {self.brand} {self.model}")

    def message(self):
        print(f"Sending a message from {self.brand} {self.model}")

# Subclass representing a specific type of smartphone
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, color, storage, camera_quality):
        super().__init__(brand, model, color, storage)
        self.camera_quality = camera_quality

    def show_camera_specs(self):
        print(f"Camera Quality: {self.camera_quality} MP")

    def call(self):
        print(f"Making a call with enhanced camera features from {self.brand} {self.model}")

# Creating instances of the classes
my_phone = Smartphone("Samsung", "Galaxy S21", "Phantom Gray", 128)
my_phone.show_specs()
my_phone.call()

my_camera_phone = SmartphoneWithCamera("Samsung", "Galaxy S21 Ultra", "Phantom Black", 256, 108)
my_camera_phone.show_specs()
my_camera_phone.show_camera_specs()
my_camera_phone.call()
