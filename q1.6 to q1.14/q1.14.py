# Constants
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2

# Given masses and distances
mass_earth = 5.972e24  # Mass of Earth in kilograms
mass_moon = 7.34767309e22  # Mass of Moon in kilograms
mass_sun = 1.989e30  # Mass of Sun in kilograms
distance_earth_sun = 1.496e11  # Average distance between Earth and Sun in meters
distance_moon_earth = 3.844e8  # Average distance between Moon and Earth in meters

# Calculate gravitational forces
force_earth_sun = G * (mass_earth * mass_sun) / distance_earth_sun**2
force_moon_earth = G * (mass_moon * mass_earth) / distance_moon_earth**2

# Print calculated forces
print(f"Gravitational force between Earth and Sun: {force_earth_sun:.2e} N")
print(f"Gravitational force between Moon and Earth: {force_moon_earth:.2e} N")

# Comparison and explanation
if force_earth_sun > force_moon_earth:
    print("The gravitational force between the Earth and the Sun is stronger.")
    print("Therefore, the Earth is more attracted to the Sun compared to the Moon.")
else:
    print("The gravitational force between the Moon and the Earth is stronger.")
    print("Therefore, the Moon is more attracted to the Earth compared to the Sun.")
#The gravitational force between the Earth and the Sun is significantly stronger than that between the Moon and the Earth. This is evident because the Sun's mass is much greater than the Moon's mass, despite the Moon being much closer to Earth than the Sun is.