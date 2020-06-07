# get sentence as user input and store the sentence.
sentence = input("\nEnter a sentence: \n\n")

# due to case sensitivity convert the sentence to lower case.
sentence_cleaned = sentence.lower()

# use the set() function to remove duplicate characters.
sentence_letters = set(sentence_cleaned)

# use list() function to create a list of the alphabet characters.
alphabet_letters = list("abcdefghijklmnopqrstuvwxyz")

# use a for loop to loop through the elements of the sentence_letter set.
# remove each letter from the sentence_letter set from the list of alphabet
# letters. for this purpose create a new list called missing_letters and
# assign it the values of the alphabet_letters list.
for i in sentence_letters:
	if i in alphabet_letters:
		missing_letters = alphabet_letters
		missing_letters.remove(i)


# if the list of missing letters is empty, the sentence is a pangram.
# otherwise, it is not. In this case print a list of missing letters.
if len(missing_letters) == 0:
	print("\nThe sentence is a valid pangram.\n")
else:
	print("\nThe sentence is not a valid pangram.")
	print(f"\nThe following letters are missing:\n{missing_letters}\n")
