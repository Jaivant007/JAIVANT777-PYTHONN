ch = input("enter a character: ").lower()
is_vowel = ch in "aeiou"
print(f"{ch} is a vowel" if is_vowel else f"{ch} is a consonant")
