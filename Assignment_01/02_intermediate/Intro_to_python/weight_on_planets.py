'''
Milestone #2: Adding in All Planets
Mars is not the only planet in our solar system with its own unique gravity. In fact, each planet has a different gravitational constant, which affects how much an object would weigh on that planet. Below is a list of the constants for each planet compared to Earth's gravity:

Mercury: 37.6%

Venus: 88.9%

Mars: 37.8%

Jupiter: 236.0%

Saturn: 108.1%

Uranus: 81.5%

Neptune: 114.0%

Write a Python program that prompts an Earthling to enter their weight on Earth and then to enter the name of a planet in our solar system. The program should print the equivalent weight on that planet rounded to 2 decimal places if necessary.

You can assume that the user will always type in a planet with the first letter capitalized and you do not need to worry about the case where they type in something other than one of the above planets.


'''

# milestone 2

# planetaryweight.py

# Gravitational constants relative to Earth
gravity = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Prompt user for weight on Earth
earth_weight = float(input("Enter a weight on Earth: "))

# Prompt user for planet name
planet = input("Enter a planet: ").capitalize()

# Get gravity factor for the chosen planet
gravity_factor = gravity[planet]

# Calculate and round equivalent weight
planet_weight = round(earth_weight * gravity_factor, 2)

# Output the result
print(f"The equivalent weight on {planet}: {planet_weight}")
