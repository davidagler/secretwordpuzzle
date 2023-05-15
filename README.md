# Secret Word Puzzle

Suppose there are three logicians. On a table, they are presented with the following letter combinations (let's call these letter combinations "words" for convenience):

aaa, abc, abd, ace, abf

A single word is selected from that list of words and each logician is given exactly one letter from that word in an envelope. No logician is given the same occurrence of a letter. For example, if "a" occurs twice in a word, one logician can have the first "a" and the second logician can have the second "a". In contrast, if "a" occurs once in a word, two logicians cannot both have "a". All three logicians open up their envelope at the same time, then consider whether they know the word based on their letter.

1. Based on the letter given, logician 1 knows the word, but logicians 2 and 3 do not. 
2. Logician 1 then states "I know the word."
3. Logician 2 hears this and then says "I did not know the word at the beginning but now that Logician 1 says they know the word, now I know the word."
4. Logician 3 hears this and then says "I did not know the word at the beginning. And, I did not know the word after Logician 1 said they knew the word. But now that Logician 2 says they know the word, now I know the word."

Question: What is the word? What letter does each logician have?

# Prior Versions of the Puzzle

The core element of this puzzle is that the second and third logicians are not supposed to be able to reason to their word by reasoning from their letter. More specifically, Logician 2 is only supposed to know the word after Logician 1 says that they know the word. And, Logician 3 is only supposed to know the word after Logician 2 says they know the word. The main problem with prior versions of this puzzle is that they suggest that this is how the puzzle is to be read but then the solution requires you to ignore this fact. 

- Puzzle 1 word list from Summers "Mind Teasers & Mind Puzzlers": word_list = ["HOE", "OAR", "PAD", "TOE", "VAT"] 
- Puzzle 2 from "Mind Your Decisions": https://www.youtube.com/watch?v=D3hWpU4Pdvg
