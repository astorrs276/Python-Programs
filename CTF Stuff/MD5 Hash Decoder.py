# Failed to get the most complicated hashes
import hashlib
from itertools import product

# MD5 hash to crack
target_hash = "b16f0cf232f30e6fb91a369b12d53c57"

# List of space-related terms (Modify if needed)
space_terms = [
    # "Andromeda", "Asterism", "Aurora", "BigBang", "BlackDwarf", "Celestial", "Cepheid", "Chondrite", "Corona",
    # "DarkMatter", "DwarfPlanet", "Eclipse", "Elliptical", "Exosphere", "Galactic", "Geocentric", "Heliosphere",

    # "Hypernova", "Interstellar", "Ionosphere", "Kepler", "KuiperBelt", "Lagrange", "LightYear", "Magnetar",
    # "Mesosphere", "MeteorShower", "Nebular", "Neutrino", "Nova", "OortCloud", "Parallax", "Perihelion",
    # "Photon", "Protostar", "Pulsar", "QuarantineZone", "RedDwarf", "Retrograde", "Singularity", "SolarWind",
    # "Spectroscope", "Stratosphere", "Supercluster", "Synchrotron", "Telescope", "Thermosphere", "TidalForce",
    # "Trojan", "Ultraviolet", "VanAllenBelt", "WarpDrive", "WhiteDwarf", "Zenith"
]

# Leet replacements (e.g., A -> 4, E -> 3)
leet_map = {
    "a": "4", "b": "8", "e": "3", "g": "9", "i": "1", "l": "1", "o": "0", "s": "5", "t": "7"
}

def generate_leet_variations(word):
    variations = [word]
    for letter, replacement in leet_map.items():
        new_variations = []
        for variant in variations:
            new_variations.append(variant.replace(letter, replacement))
        variations.extend(new_variations)
    return set(variations)

def generate_case_variations(word):
    return set("".join(chars) for chars in product(*[(c.lower(), c.upper()) for c in word]))

# Number range to append/prepend (adjust as needed)
num_range = range(1000)  # 0-999

# Try different formats: numbers before/after the space-related term
for term in space_terms:
    possible_variations = generate_leet_variations(term)
    case_variations = set()
    for variation in possible_variations:
        case_variations.update(generate_case_variations(variation))
    
    for variation in case_variations:
        for num in num_range:
            for pattern in [f"{num}{variation}", f"{variation}{num}"]:
                # Compute MD5 hash
                hashed = hashlib.md5(pattern.encode()).hexdigest()
                
                # Check if it matches the target hash
                if hashed == target_hash:
                    print(f"Cracked! The password is: {pattern}")
                    exit()

print("No match found. Try expanding num_range or checking for different formats.")
