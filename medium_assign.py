'''

This file contains the functions that you need for completing this assignment. 

1. expression_1() --> 30%
2. expression_2() --> 40%
3. expression_3() --> 30% 

Failure to follow the variable name guides will lead to reduction of 10 points. 

DO NOT EDIT THE FUNCTION NAMES.


'''

def expression_1(x):

     #Write a code that returns value for the following expression: x^3 - (2x + x^2) - 100 
    result = x ** 3 - (2 * x + x ** 2) - 100
    return result


def expression_2(x, y):

        #Write code that returns only the integer value of the following expression: (x^4 / 2y) - (3xy) + (6y / 7x)
    result = (x ** 4)/(2 * y) - 3 * x * y + (6 * y)/(7 * x)
    return result


def expression_3(x, y):

       # Write code that returns the value of the following expression: (x^3 + y^2) / (x^2 - y^3)
    result = (x ** 3 + y ** 2) / (x ** 2 - y ** 3)
    return result

if __name__ == "__main__":
    
    x = float(input('Enter a value: '))
    result_1 = expression_1(x)
    print(f'Result 1 is {result_1}')

    x_1 = float(input('Enter x value: '))
    y_1 = float(input('Enter y value: '))
    result_2 = expression_2(x_1, y_1)
    print(f'Result 2 is {result_2}')

    x_2 = float(input('Enter x value: '))
    y_2 = float(input('Enter y value: '))
    result_3 = expression_3(x_2, y_2)
    print(f'Result 3 is {result_3}')
