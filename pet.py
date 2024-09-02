import random
import time

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50
    
    def feed(self):
        self.hunger -= random.randint(5, 10)
        if self.hunger < 0:
            self.hunger = 0
        print(self.name + " has been fed.")

    def play(self):
        self.energy -= random.randint(5, 10)
        self.happiness += random.randint(5, 10)
        if self.energy < 0:
            self.energy = 0
        if self.happiness > 100:
            self.happiness = 100
        print(self.name + " is playing.")

    def sleep(self):
        self.energy += random.randint(5, 10)
        if self.energy > 100:
            self.energy = 100
        print(self.name + " is sleeping.")

    def display_status(self):
        print("\n" + self.name + "'s Status:")
        print("Hunger: " + str(self.hunger))
        print("Energy: " + str(self.energy))
        print("Happiness: " + str(self.happiness))

def main():
    pet_name = input("Enter your pet's name: ")
    pet = Pet(pet_name)
    print("Welcome to the Virtual Pet Game!")
    print("You can feed, play, or let your pet sleep.")
    
    while True:
        pet.display_status()
        choice = input("\nEnter your choice (feed/play/sleep/exit): ").lower()

        if choice == 'feed':
            pet.feed()
        elif choice == 'play':
            pet.play()
        elif choice == 'sleep':
            pet.sleep()
        elif choice == 'exit':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        # Simulate the passage of time
        time.sleep(1)

if __name__ == "__main__":
    main()
