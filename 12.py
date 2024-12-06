
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} makes a sound.")



class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")



bobik=Dog("bobik",15)
bobik.speak()
