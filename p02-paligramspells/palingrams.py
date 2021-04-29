"""Identify Paligrams in a dictionary file."""
import load_dictionary

words = load_dictionary.load("2of4brif.txt")


def find_palingrams():
    palingrams = []
    for word in words:
        end = len(word)
        rev_word = word[::-1]    
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-1] and rev_word[end-1:] in words:
                    palingrams.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-1:] and rev_word[:end-1] in words:
                    palingrams.append((rev_word[:end-i], word))
    return palingrams

palingrams = find_palingrams()
paligrams_sorted = sorted(palingrams)

print(f"Number of Palingrams = {len(paligrams_sorted)}")
for first, second in paligrams_sorted:
    print(f"{first} {second}")

