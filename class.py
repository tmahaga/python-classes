class Temperature:
    def __init__(self, celsius,fahrenheit,kelvin):
        self.cel = celsius
        self.fah = fahrenheit
        self.kel = kelvin

    def convert_to_fahrenheit(self):
        return (self.fah * 9/5) + 32

    def convert_to_kelvin(self):
        return self.kel + 273.15

    def convert_to_celsius(self):
        return (self.fah - 32) * 5/9


# Create object
temp = Temperature(25, 77, 298.15 )

print(f"Temperature in Celsius: {temp.convert_to_celsius()}")
print(f"Temperature in Fahrenheit: {temp.convert_to_fahrenheit()}")
print(f"Temperature in Kelvin: {temp.convert_to_kelvin()}")