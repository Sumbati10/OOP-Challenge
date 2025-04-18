from pet import Pet

# Create a new pet
my_pet = Pet("Max")

print(f"Creating pet: {my_pet.name} 🐶")

# Simulate some actions
my_pet.eat()
my_pet.play()
my_pet.sleep()

# Teach tricks
my_pet.train("roll over")
my_pet.train("play dead")

# Show current status and tricks
my_pet.get_status()
my_pet.show_tricks()

