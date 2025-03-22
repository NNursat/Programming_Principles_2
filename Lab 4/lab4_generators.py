#1
# n = int(input())
# for i in range(n):
#   print(i ** i, end="\n")

#2
# n = int(input())
# for i in range(0, n, 2):
#   print(i, end=", ")

#3
# n = 100
# for i in range(0, n):
#   if i % 3 == 0 or i % 4 == 0:
#     print(i, end=" - ")

# 4
# a, b = list(map(int, input().split()))
# for i in range(a, b):
#   print(i**2)

# 5
# n = int(input())
# for i in range(n, 0, -1):
#   print(i)
----------------------------------------------------------------------------------------------------------------
def generator(n):
    sq = 0
    while sq < n:
        yield sq**2
        sq += 1
    return "stop"    

gen = generator(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# 2
# def generator2(n):
#     a = 0
#     while a < n:
#         if a % 2 == 0:
#             yield a
#         a += 1
# n = int(input())
# gen2 = generator2(n)
# print(", ".join(map(str, gen2)))
# 3
# def generator3(n):
#     a = 0
#     while a <= n:
#         if a % 3 == 0 and a % 4 == 0:
#             yield a
#         a += 1
# n = int(input())
# gen3 = generator3(n)
# print (", ".join(map(str, gen3)))
# 4
# def squares(a, b):
#     while a <= b:
#         yield a ** 2
#         a += 1

# a = int(input())
# b = int(input())

# gen_squares = squares(a, b)

# for square in gen_squares:
#     print(square)
# 5
# def countdown(n):
#     while n >= 0:
#         yield n
#         n -= 1

# n = int(input())

# gen_countdown = countdown(n)

# for num in gen_countdown:
#     print(num)



