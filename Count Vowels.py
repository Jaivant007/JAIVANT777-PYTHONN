def count_vowels(word):
    return sum(1 for char in word if char in 'aeiouAEIOU')

words = input("enter words (space-separated): ").split()
vowel_counts = list(map(count_vowels, words))
print("Vowel Counts:", vowel_counts)
