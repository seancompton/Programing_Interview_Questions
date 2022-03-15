from array import array
import string
from tkinter.messagebox import YESNOCANCEL

#main function ya know!
def main():
    user_input = input("Please input a string: ")
    characters = find_repeat_characters(user_input)
    print_array(characters, user_input)

#loops through the repeated words and finds out if their are repeated words
def find_repeat_characters(string_of_characteres):
    user_input = string_of_characteres.replace(" ", "")
    repeated_words = []

    for i in range(len(user_input)):
        for j in range(len(user_input)):
            if i != j:
                if user_input[i] == user_input[j]:
                    repeated_words.append(user_input[i])
    return filter_repeats(repeated_words)

#gets rid of the words that are repeated in the array
#of repeated words
def filter_repeats(array_of_characters):
    empty_list = []
    for i in array_of_characters:
        if i not in empty_list:
            empty_list.append(i)
    return empty_list

#prints the array of words that it is given and if it is empty it prints
#the original word
def print_array(array_of_characters, original_user_input):
    if (len(array_of_characters) !=0):
        for i in array_of_characters:
            print(i)
    elif (len(array_of_characters) == 0):
        print(original_user_input)

main()