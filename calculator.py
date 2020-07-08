"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

def calculator():

    while True:
        promt = input("Enter your equation > ")
        tokens = promt.split(' ')
        
        first_token = tokens[0]


        if first_token == 'q':
            return

        else:
            second_token = int(tokens[1])
            third_token = int(tokens[2])            
            if first_token == 'pow':
                print(multiply(second_token, third_token))

            elif first_token == '+':
                print(add(second_token, third_token))

            elif first_token == '-':
                print(subtract(second_token, third_token))

            elif first_token == '*':
                print(multiply(second_token, third_token))

            elif first_token == '/':
                print(divide(second_token, third_token))

            elif first_token == 'square':
                print(square(second_token, third_token))

            elif first_token == 'cube':
                print(cube(second_token, third_token))

            elif first_token == 'mod':
                print(mod(second_token, third_token))


calculator()
        

# Replace this with your code
