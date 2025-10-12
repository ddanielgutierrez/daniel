# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

def count_vowels_and_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    constant_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                constant_count += 1
    return(vowel_count, constant_count)                

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(paragraph):
    sentences = paragraph.replace('!', '.').replace('?', '.').split('.')
    clean_sentences = []
    for s in sentences:
        s = s.strip()
        if s:
            clean_sentences.append(s)
    total_vowels = 0
    total_consonants = 0

    for sentence in clean_sentences:
        v, c = count_vowels_and_consonants(sentence)
        total_vowels += v
        total_consonants += c
    
    num_sentnences = len(clean_sentences)
    if num_sentnences > 0:
        average_vowels = total_vowels / num_sentnences
        average_consonants = total_consonants / num_sentnences
    else:
        average_vowels = 0
        average_consonants = 0
    return (num_sentnences, average_vowels, average_consonants)

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

num_sentences, avg_vowels, avg_consonants = average_vowels_and_consonants(paragraph)
print(f"Average vowels per sentence: {avg_vowels:.2f}")
print(f"Average consonants per sentence: {avg_consonants:.2f}")

