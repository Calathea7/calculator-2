"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

from functools import reduce

def calculator():

    while True:
        promt = input("Enter your equation > ")
        tokens = promt.split(' ')

        operator, *token_nums = tokens

        nums = []
        
        answer = None

        try:
            for num in token_nums:
                nums.append(float(num))
        except:
            print("Error! All operands must be numbers. Try again.")
            continue

        if 'q' in tokens:
            break

        else:
          
            if operator == 'pow':
                answer = reduce(power, nums)

            elif operator == '+':
                answer = reduce(add, nums)

            elif operator == '-':
                answer = reduce(subtract, nums)

            elif operator == '*':
                answer = reduce(multiply, nums)

            elif operator == '/':
                answer = reduce(divide, nums)

            elif operator == 'square':
                answer = square(nums[0])

            elif operator == 'cube':
                answer = cube(nums[0])

            elif operator == 'mod':
                answer = reduce(mod, nums)
            else:
                print("You entered an invalid operator")
                continue

            print(answer)


calculator()
        

# Replace this with your code
