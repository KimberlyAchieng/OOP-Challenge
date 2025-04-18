# Importing the class Pet from pet.py
from pet import Pet

# Create your pet
my_pet = Pet("Buddy")

# Check initial status
print(f"Initial status of {my_pet.name}:")
my_pet.get_status()

# Interact with your pet
print(f"\nAfter interacting with {my_pet.name}...")
my_pet.eat()
my_pet.sleep()
my_pet.play()

# Check status again
my_pet.get_status()

# Bonus features
my_pet.train("roll over")
my_pet.train("sit")
my_pet.show_tricks()
