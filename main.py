import enchant
import nltk
# imports whole english dictionary as list
from nltk.corpus import words
all_words = words.words()

# makes new list with only 5 letter words
list_of_possible_words = []
for word in all_words:
    if len(word) == 5:
        list_of_word = [char for char in word]
        list_of_possible_words.append(list_of_word)

# print(list_of_possible_words)
word_list = ['', '', '', '', '']

final_word = ""
playing = True

def find_possible_words():
    global list_of_possible_words
    list_to_check = list_of_possible_words
    for tup in enumerated_list:
        if tup[1] != "":
            for list in list_to_check[:]:
                if tup[1] != list[tup[0]]:
                    list_of_possible_words.remove(list)
    if pos_unknown != []:
        for letter in pos_unknown:
            for list in list_to_check[:]:
                if letter not in list:
                    list_of_possible_words.remove(list)
    if not_in_word != []:
        for letter in not_in_word:
            for list in list_to_check[:]:
                if letter in list:
                    list_of_possible_words.remove(list)


def remove_ruled_out_words(letter, pos):
    global list_of_possible_words
    for list in list_of_possible_words[:]:
        if list[pos - 1] == letter:
            list_of_possible_words.remove(list)

while "" in word_list:
    letter1 = input("what is the first letter?(don't input anything if unknown) ")
    letter2 = input("what is the second letter?(don't input anything if unknown) ")
    letter3 = input("what is the third letter?(don't input anything if unknown) ")
    letter4 = input("what is the fourth letter?(don't input anything if unknown) ")
    letter5 = input("what is the fifth letter?(don't input anything if unknown) ")
    unknown_pos = input("what letters have an unknown position?(don't input anything if none) ")
    if unknown_pos != "":
        for letter in unknown_pos:
            not_in_position = int(input(f"what position can't {letter} be in(type the column number)"))
            remove_ruled_out_words(letter, not_in_position)
    letter_not_in_word = input("what letters aren't in the word? ")
    pos_unknown = [char for char in unknown_pos]
    not_in_word = [char for char in letter_not_in_word]
    for i in range(0, len(word_list)):
        if i == 0:
            word_list[i] = letter1
        if i == 1:
            word_list[i] = letter2
        if i == 2:
            word_list[i] = letter3
        if i == 3:
            word_list[i] = letter4
        if i == 4:
            word_list[i] = letter5
    enumerated_list = list(enumerate(word_list))
    find_possible_words()
    for possible_word in list_of_possible_words:
        word = ""
        for letter in possible_word:
            word += letter
        print(word)
