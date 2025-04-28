def solve(ransomNote, magazine):
    ransomNote = list(ransomNote)
    magazine = list(magazine)
    for char in ransomNote:
        if char not in magazine:
            return False
        magazine.remove(char)
    return True