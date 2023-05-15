# Finds unique letter
def find_unique_letters(string_list):
    letter_counts = {}    
    # Count the occurrences of each letter
    for string in string_list:
        for letter in string:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1    
    # Filter out letters that appear exactly once
    unique_letters = [letter for letter, count in letter_counts.items() if count == 1]
    return unique_letters

'''
If a word contains no unique letters, we want to remove it. Otherwise the logician would not be able to know it. 
NB! If it has more than one unique letter, we also want to remove it. Otherwise the next logician would be able to know it. The next logician can only know the word AFTER they know the prior logician's word occurs exactly once.
'''
# Filters word list. If list has less than or more than one letter, remove it. 
def filter_words(letters, words):
    filtered_words = []
    for word in words:
        letter_count = 0
        for letter in letters:
            if letter in word:
                letter_count += 1
        if letter_count == 1:
            filtered_words.append(word)
    return filtered_words

#filters out the unique letters. No two logicians can have the same occurrence of a letter.
def remove_letters(list1, list2):
    filtered_list = ["".join(letter for letter in word if letter not in list1) for word in list2]
    return filtered_list

# Sample Word Lists:

'''
Puzzle 1 word list from Summers "Mind Teasers & Mind Puzzlers": word_list = ["HOE", "OAR", "PAD", "TOE", "VAT"] 
Puzzle 2 from "Mind Your Decisions": https://www.youtube.com/watch?v=D3hWpU4Pdvg

'''
#word_list = ["HOE", "OAR", "PAD", "TOE", "VAT"] # Summers  "Mind Teasers & Mind Puzzlers", p.51 (the YES, YES, YES Puzzle)
#word_list = ["cat", "dog", "has", "max", "dim", "tag"] #Mind Your Decisions Puzzle https://www.youtube.com/watch?v=D3hWpU4Pdvg 
word_list = ["aaa", "abc", "abd", "ace", "abf"] #My Puzzle
#word_list = ['aaa']

print(f"Here is our word list: {word_list}")
if len(word_list) == 1:
    print(f"There is a solution. The word is {word_list}")

'''
Identify the letters Logician 1 has, identify the possible words, remove words that don't have that letter, then filter the remaining letters from the word list.
'''
# Find the unique letters in the initial word list
letter_result1 = find_unique_letters(word_list)
print(f"Logician 1's letter must be {letter_result1}")

# L1's possible words
log1_poss_words = filter_words(letter_result1, word_list)
print(f"The available words for Logician 1 are {log1_poss_words}")

# Removing Logician 1's letters gives us these letters
log2_letters = remove_letters(letter_result1, log1_poss_words)
print(f"Removing Logician 1's letters gives us {log2_letters}")

'''
Identify the letters Logician 2 has, identify the possible words, remove words that don't have that letter, then filter the remaining letters from the word list.
'''

# Finding the unique letters in these letters gives us L2's possible letters
letter_result2 = find_unique_letters(log2_letters)
print(f"Logician 2's possible letters: {letter_result2}")

# Now we want L2's possible words
log2_poss_words = filter_words(letter_result2, log1_poss_words)
print(f"Logician 2's possible words: {log2_poss_words}")

# Removing Logician 1 and 2's letters gives us:
log3_letters_p1 = remove_letters(letter_result1, log2_poss_words)
log3_letters = remove_letters(letter_result2, log3_letters_p1)
print(f"Removing Logician 2's letters gives us {log3_letters}")

'''
Identify the letters Logician 3 has, identify the possible words. If there is one, then state there is a solution and state the word. 
'''

# Unique letters in these letters gives us L3's possible letters
letter_result3 = find_unique_letters(log3_letters)
print(f"Logician 3's possible letters: {letter_result3}")

# Now we want L3's possible words
log3_poss_words = filter_words(letter_result3, log2_poss_words)
print(f"Logician 3's possible words: {log3_poss_words}")

if len(log3_poss_words) == 1:
    print(f"There is a solution. The word is: {log3_poss_words}")
else: 
    print("There is no solution.")

