class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Cat")
        self.breed = breed

    def make_sound(self):
        return "Meow!"

def main():
    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Whiskers", "Siamese")

    print(f"{dog.name} is a {dog.breed} and says {dog.make_sound()}")
    print(f"{cat.name} is a {cat.breed} and says {cat.make_sound()}")

if __name__ == "__main__":
    main()