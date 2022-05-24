from collections import Counter
import math
import sys

def getdistance(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def fun2(mylist):
    # x=[]
    # for a in mylist:
    #     if a not in x:
    #         x.append(a)
    # return x
    #or
    return list(set(mylist))

def fun3(st1,st2):
    return st1[:math.ceil(len(st1)/2)]+st2[:math.ceil(len(st2)/2)] , st1[math.ceil(len(st1)/2):]+st2[math.ceil(len(st2)/2):]


def fun4(c):
     vowels = ('a', 'e', 'i', 'o', 'u')
     return ''.join([x for x in c if x not in vowels])

def fun5(st,ch):
    return [ i for i,x in  enumerate(st) if x==ch ]


def fun6():
    f = open(sys.argv[len(sys.argv)-1], "r")
    my_str = f.read()
    f.close()
    words = Counter(my_str.split()).most_common(20)
    words = [word[0] for word in words]
    f = open("popular_words.txt", "w")
    f.write("\n". join(map(lambda word: str(word), words)))
    f.close()


# x=getdistance(1,2,3,4)
# print(x)

# y=fun2([1,2,2,2,3,6,6])
# print(y)

# a=fun3("abcd","abcde")
# print(a)


# x=fun4('mobile')
# print(x)

# x=fun5('google','o')
# print(x)
fun6()