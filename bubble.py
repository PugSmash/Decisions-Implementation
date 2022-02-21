
def bubble(l):
    for i in range(len(l)):
        for i in range((len(l) - 1)):
            a = l[i]
            b = l[i + 1]
            if a > b:
                l[i], l[i + 1] = b, a
            else:
                pass
    return l

l = [2, 3, 84, 43, 431, 544, 675, 2234, 4342, 525]

print(bubble(l))