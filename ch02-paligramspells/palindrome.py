"""Fin palindromes (letter palingrams) in a dictionary file."""
import load_dictionary

word_list = load_dictionary.load("2of4brif.txt")
palindromes = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        palindromes.append(word)

print(f"Found {len(palindromes)} palindroms in the dictionary")
print(*palindromes, sep='\n')
