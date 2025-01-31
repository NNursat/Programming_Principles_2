#w3 schools
print(bool(0))
print(bool(0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001))
#this is a border between false and true
print("Hello world")
#operators

#lists
newlist = ["kbtu", "roof", "fire"]
print(newlist)
print(newlist[-1])
print(newlist[:2])
if "fire" in newlist:
    print("Yes, it happened")

newlist.append("online")
print(newlist)

newlist.insert(3, "good news")
print(newlist)

anotherlist = ["sleep", "extended dayoff"]
newlist.extend(anotherlist)
print(newlist)

newtuple = ("vse", "bitti")
newlist.extend(newtuple)
print(newlist)

newlist.remove("online")
print(newlist)

newlist.pop(2)
print(newlist)

for x in newlist:
    print(x)

for x in range(len(newlist)):
    print(x)

mylist = ["apple", "banana", "cheetah", "dolphin", "excalibur", "fridge"]

print(sorted(mylist, reverse=True))

mylistcopy = mylist

print(mylistcopy.copy())

mylist2 = ["etot", "gorod", "budto", "pod", "vodoi"]

# mylist3 = mylist + mylist2

for i in mylist:
    mylist2.append(i)

print(mylist2)

#tuples

mytuple = ("Acura", "Bentley", "Citroen", "Dodge", "Exeed", "Ford", "Geely", "Honda", "Infiniti", "Jaguar", "Kia", "Lotus", "Mazda", "Nissan", "Opel", "Porsche", "Q", "Rolls-Royce", "Subaru", "Toyota", "U", "Volvo", "W", "Xiaomi", "Y", "Zeekr")


thistuple = tuple(("apple", "banana", "cherry")) 
print(thistuple)

print(mytuple[1:5])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# mytuple.append("Volkswagen") it will not work

temp = list(mytuple)
temp.append("Volkswagen")
mytuple = tuple(temp)

print(mytuple)

temp = list(mytuple)
temp.remove("Volkswagen")
mytuple = tuple(temp)

print(mytuple)

(mid_end, high_level, french_shit, *other_cars) = mytuple

print(mid_end)
print(high_level)
print(french_shit)
print(other_cars)

for x in mytuple:
  print(x)

#set не изменяемый и хранит только уникальные предметы и анордеред

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#dictionary

mydict = {
    "country": "Kazakhstan",
    "population": "20 millions",
    "foundation year": 1991,
    "capital": "Astana"
}
print(mydict["country"])
