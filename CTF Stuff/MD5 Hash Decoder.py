import hashlib
from itertools import product

# hash to crack
target_hash = "2212e01ddbc681e7930e308a27aec679d1ccf36baa26ebec2d43d24813bfa4be"

minions = [
    "Kevin", "Stuart", "Bob", "Dave", "Jerry", "Carl", "Phil", "Tim", "Mark", "Tom", "Jorge", "Donny", "Ken", "Mike", "Norbert", "Lance", "John", "Paul", "Steve", "Chris", "Larry", "Darwin", "Mel"
]

common_first_names = [
    "Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas", "Henry", "Alexander",
    "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Jackson", "Sebastian", "Jack", "Aiden", "Owen", "Samuel",
    "Matthew", "Joseph", "Levi", "Mateo", "David", "John", "Wyatt", "Carter", "Julian", "Luke", "Grayson",
    "Isaiah", "Gabriel", "Anthony", "Dylan", "Leo", "Lincoln", "Jaxon", "Asher", "Christopher", "Joshua",
    "Andrew", "Theodore", "Caleb", "Ryan", "Nathan", "Adrian", "Isaac", "Thomas", "Charles", "Josiah",
    "Hudson", "Christian", "Hunter", "Connor", "Eli", "Ezra", "Aaron", "Angel", "Robert", "Nolan",
    "Jameson", "Nicholas", "Gabriel", "Cameron", "Zachary", "Leonardo", "Luca", "Blake", "Santiago",
    "David", "Maxwell", "Ian", "Jordan", "Evan", "Roman", "Jonathan", "Miles", "Adam", "Cooper",
    "Jude", "Elliot", "Jason", "Ezekiel", "Elias", "Easton", "Eli", "Milo", "Elliot", "Riley",
    "Theo", "Kayden", "Nathaniel", "Axel", "Eli", "Nathan", "Landon", "Austin", "Evan", "Diego",
    "Xander", "Avery", "Amos", "Tyler", "Xander", "Caden", "Ezekiel", "Elias", "Brody", "Henry",
    "Zane", "Levi", "Owen", "Theo", "Liam", "Jordan", "Aiden", "Luka", "Evan", "Riley",
    "Elijah", "Grayson", "James", "Roman", "Christopher", "Samuel", "Mason", "Matthew", "Noah",
    "Jackson", "Caleb", "Joshua", "Sebastian", "Isaiah", "Nolan", "Hunter", "David", "Zachary",
    "Isaac", "Wyatt", "Oliver", "Mason", "Lucas", "Jackson", "Jameson", "Levi", "Andrew",
    "Lucas", "Henry", "Benjamin", "Landon", "Mateo", "Grayson", "Ethan", "David", "Matthew",
    "Isaiah", "Nathan", "Christian", "Adrian", "Hunter", "Eli", "Thomas", "Liam", "Ezra",
    "Milo", "Aiden", "Wyatt", "Jackson", "John", "Owen", "Santiago", "Carter", "Blake",
    "Daniel", "Isaac", "Landon", "Miles", "Levi", "Aiden", "Tyler", "Hudson", "Maxwell",
    "Joseph", "Julian", "Nolan", "David", "Wyatt", "Roman", "Luca", "Grayson", "Blake",
    "Jaxon", "Hudson", "Xander", "Julian", "Zachary", "Elijah", "Jude", "Mason", "Owen",
    "Axel", "Miles", "Wyatt", "Zane", "Hunter", "Cooper", "David", "Tyler", "Evan",
    "Carter", "Andrew", "Oliver", "Blake", "Austin", "Riley", "Leo", "Eli", "Theo",
    "Liam", "Nathaniel", "Ryan", "Roman", "Joshua", "Lucas", "Noah", "Mason", "Zachary",
    "David", "Levi", "Jason", "Christian", "Cameron", "Luka", "Gabriel", "Ezekiel", "Avery",
    "Sebastian", "Jonathan", "Cooper", "John", "Adam", "Jack", "Nathan", "Hudson", "Amos",
    "Easton", "Hunter", "Elijah", "Ian", "David", "Riley", "Santiago", "Zane", "Joseph",
    "Matthew", "Landon", "Isaac", "Eli", "Wyatt", "Hudson", "Carter", "Aiden", "Miles",
    "Caleb", "Luca", "John", "Grayson", "Ryan", "Noah", "Levi", "Julian", "Jason", "David",
    "Milo", "Roman", "Mason", "Sebastian", "Hunter", "Joshua", "Caden", "James", "Luke",
    "Joseph", "Christian", "Ezekiel", "Ian", "Jonathan", "Hunter", "Jackson", "Nathan",
    "Blake", "Nathaniel", "David", "Maxwell", "Roman", "Tyler", "Landon", "Mateo", "Jaxon",
    "Leo", "Milo", "Samuel", "Zachary", "Isaiah", "Owen", "Wyatt", "Luca", "Mason", "Nolan",
    "Easton", "Axel", "Eli", "Grayson", "Roman", "Ezekiel", "Theo", "Liam", "Cameron",
    "Ezra", "Sebastian", "Jason", "Hunter", "Jackson", "Maxwell", "Avery", "John", "Adam",
    "Zane", "David", "Mason", "Joseph", "Liam", "Roman", "Owen", "Aiden", "Xander",
    "Joshua", "Sebastian", "Hudson", "Carter", "Luke", "Riley", "Wyatt", "Miles", "Isaac",
    "Jackson", "David", "Benjamin", "Luca", "Zachary", "Evan", "Levi", "Ryan", "Milo",
    "Tyler", "Liam", "Hunter", "Isaiah", "Easton", "Ezekiel", "David", "Wyatt", "Leo",
    "Owen", "Luca", "Sebastian", "Hudson", "Adrian", "Maxwell", "Roman", "John", "Mateo",
    "Grayson", "Nathan", "Ryan", "Zachary", "Jackson", "Benjamin", "Milo", "Liam", "Caden",
    "Leo", "Jackson", "Eli", "Evan", "Jason", "Levi", "Sebastian", "Oliver", "Nathaniel",
    "Matthew", "David", "Julian", "Luca", "Blake", "Axel", "Santiago", "Carter", "Ezra",
    "Noah", "Isaac", "Riley", "David", "Zachary", "Lucas", "Leo", "Roman", "Aiden", "Blake"
]

# Try different formats: numbers before/after the space-related term
for minion in minions:
    for voice_actor in common_first_names:
        pattern = f"{minion}-{voice_actor}"
        hashed = hashlib.sha256(pattern.encode()).hexdigest()
        
        if hashed == target_hash:
            print(f"{minion}-{voice_actor}")
            print(hashed)
            exit()




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

print("No match found. Try expanding num_range or checking for different formats.")
