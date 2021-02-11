
'''

This file contains the functions that you need for completing this assignment. 

1. append_two_strings() --> Function to append a string2 to string1. -- 30%
2. append_character() --> Function to append a character to the end of string. -- 30% 
3. append_num_to_string() --> Function to append a number to the end of a string. -- 40%

Failure to follow the variable name guides will lead to reduction of 10 points. 

DO NOT EDIT THE FUNCTION NAMES.


'''


def append_two_strings(string_1, string_2):

    result_string = string_1 + string_2
    return result_string


def append_character(string_1, char_1):

    result_char = string_1 + char_1
    return result_char


def append_num_to_string(string_1, num_1):

    result_num = string_1 + str(num_1)
    return result_num

if __name__ == "__main__":
    
    string_1 = input('Enter string 1: ')
    string_2 = input('Enter string 2: ')
    result = append_two_strings(string_1, string_2)
    print(f'The result string is: {result}')

    string_1 = input('Enter a string: ')
    char_1 = input('Enter a character: ')
    result = append_character(string_1, char_1)
    print(f'The result string is: {result}')

    string_1 = input('Enter a string: ')
    num_1 = input('Enter a number: ')
    result = append_character(string_1, num_1)
    print(f'The result string is: {result}')
