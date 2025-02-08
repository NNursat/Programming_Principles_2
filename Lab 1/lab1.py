print("Hello, world!")

if 5 > 2:
    print("YES")
#tabulyacia vajna

x = 10
y = "word"

#comment
"""
multiple
line
comment
"""

print(x)
print(y)

x = str(3)
y = float(3)

print(type(x))
print(type(y))
x1, y1, z1 = 1, 2, 3

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

def newFunc():
    print("useless function")

newFunc()

a = "hello Mr.pp2"

print(a[5])

for x in a:
    print(x)

def lenfunc(str):
    print(len(str))

lenfunc(a)

if "Mr" not in a:
    print("yes")
else:
    print("NO")

print(a[:15])

print(a.upper())
print(a.lower())

b = "      h e l l o         "
bb = "word"
print(b.strip())
print(b)

print(b.replace("h", "f"))
print(b.split(" "))

age = int(input())
txt = "I'm", age, "years old"
print(f"I'm {age} years old")

print("to use another double \"quote\" use back slash")

print(bb.capitalize())