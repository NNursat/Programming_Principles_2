#w3 schools
print(bool(0))
print(bool(0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001))
#this is border between false and true

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

