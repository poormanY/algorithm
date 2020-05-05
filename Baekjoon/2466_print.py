import sys
input = sys.stdin.readline

# k : star, n : max_len
def midStar(k, n):
    blank = " "
    star = "*"
    stars = star * k
    blanks = blank * ((n-k)//2)
    return blanks + stars

def printStars(n):
    l = 2*n-1
    for k in range(l):
        if k+1 == n:
            s = midStar(1, l)
        elif k+1 < n:
            s = midStar((n-k-1)*2+1, l)
        elif k+1 > n:
            s = midStar((k+1-n)*2+1, l)
        print(s)

N = int(input())
printStars(N)
