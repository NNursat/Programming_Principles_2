#naiti naimenwee chislo

def min_number(list1):
    minn = list1[0]
    for i in list1:
        if i < minn:
            minn = i

    return minn


lists = [3, 4, 5, 6, 7, 8, 2, 2]

print(min_number(lists))
