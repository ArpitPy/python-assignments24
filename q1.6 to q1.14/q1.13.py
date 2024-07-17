def get_color(wavelength):
    if 400 <= wavelength < 440:
        return "Violet"
    elif 440 <= wavelength < 460:
        return "Indigo"
    elif 460 <= wavelength < 500:
        return "Blue"
    elif 500 <= wavelength < 570:
        return "Green"
    elif 570 <= wavelength < 590:
        return "Yellow"
    elif 590 <= wavelength < 620:
        return "Orange"
    elif 620 <= wavelength <= 720:
        return "Red"
    else:
        return "Unknown"

# Test the function with example wavelengths
wavelengths = [450, 510, 580, 650]

for wavelength in wavelengths:
    color = get_color(wavelength)
    print(f"A wavelength of {wavelength} nm corresponds to the color: {color}")
