class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        return f'{self.name} the {self.species} says {sound}'

# Example usage
dog = Animal('Buddy', 'dog')
print(dog.make_sound('woof'))