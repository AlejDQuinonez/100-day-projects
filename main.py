print()
greetings = """
Welcome to the Game of Thrones Bastard Name Generator!
About: This program creates a bastard surname like from the famous show
of game of thrones.
"""
region_of_birth = """
What would you like your last name to be? Heres a list if you don't know
the regions:
Crownlands    = Waters
Dorne         = Sand
Iron Islands  = Pyke
North         = Snow
Reach         = Flowers
Riverlands    = Rivers
Stormlands    = Storm
Vale of Arryn = Stone
Westerlands   = Hill\n
"""
print(greetings)
firstName = input("What would you like your first name to be?\n")
lastName = input(region_of_birth)
print()
print("Your Game of Thrones Bastard's name is:")
print(firstName + " " + lastName)
print()