class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

# Create an instance of the Animal class
dog = Animal("Dog", "Woof")
cat = Animal("Cat", "Meow")

# Call the make_sound method
dog.make_sound()
cat.make_sound()