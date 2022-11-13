# password generator
import random

alfabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['*', '+', '$', '?', '&', '(', ')', '<', '+']

result = []


def create_password():
    global result

    num_letter = int(
        input('How many letter would you like in your password? \n'))
    num_number = int(input('How many numbers would you like to add? \n'))
    num_symbol = int(input('How many symbols would you like to add? \n '))

    for index_letter in range(num_letter):
        rand = random.choice(alfabets)
        result.append(rand)

    for index_number in range(num_number):
        rand = random.randrange(0, num_number)
        result.append(numbers[rand])

    for index_symbol in range(num_symbol):
        rand = random.choice(symbols)
        result.append(rand)

    my_result = ''.join(result)

    print(my_result)


create_password()
