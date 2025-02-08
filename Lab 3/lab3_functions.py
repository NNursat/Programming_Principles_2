from itertools import permutations
import math

def gram_converter(gram):
    return 28.3495231 * gram

print(gram_converter(10))

def farenheit_conv(temper):
    print((5 / 9) * (temper - 32))

farenheit_conv(10)

def solve(numheads, numlegs):
    for x in range(numheads):
        y = 35 - x
        if 2 * x + 4 * y == numlegs:
            return x, y
chicken, rabbits = solve(35, 94)
# print(chicken, rabbits, sep="\n")

# prime
def takePrime(array):
    res = []
    for i in array:
        counter = 0
        for j in range(1, i + 1):
            counter += 1 if i % j == 0 else i
        
        if counter == 2:
            res.append(i)
    print(res)
# takePrime([2, 3, 4, 5, 6, 7, 8, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23])

# permutations
def printPermutations():
    user_input = input()
    perm = permutations(user_input)
    for p in perm:
        print("".join(p))

printPermutations()

    
# reverse
oooooooo = input().split()
oooooooo.reverse()
print(oooooooo)

# check if up next to number is number

def has_33():
    number = 3
    counter = 0
    arrrrrrrrrr = [1, 3, 3, 1, 1]
    for i in range(len(arrrrrrrrrr)):
        e = arrrrrrrrrr[i]
        if e == number:
            if i < len(arrrrrrrrrr) - 1:
                if arrrrrrrrrr[i + 1] == number:
                    counter += 1
                    break
    print(True) if counter > 0 else print(False)

has_33()

#spy game

def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

print(spy_game([1, 7, 2, 0, 4, 5, 0])) 

#volume of sphere

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

print(sphere_volume(1))

#unique list w/o set
def get_unique_elements(lst):
    unique_list = []
    for element in lst:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

get_unique_elements([1, 2, 3, 3, 4, 5])

#is_palindrome
def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

print(is_palindrome("Helleh"))
print(is_palindrome("kbtu"))

#histogram
def histogram(lst):
    for num in lst:
        print('*' * num)

histogram([4, 9, 7])

#guess
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    number_to_guess = random.randint(1, 20)
    print("between 1 and 20")

    attempts = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        attempts += 1

        if guess < number_to_guess:
            print("too low.")
        elif guess > number_to_guess:
            print("too high.")
        else:
            print("You guessed in", attempts, "guesses!")
            break


guess_the_number()
