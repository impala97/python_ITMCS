import sys

def remove(l):

    l.sort()

    top = 0
    while top < len(l)-1:
        if l[top] == l[top+1] :
            l.remove(l[top])
        else :
            top +=1
    return l