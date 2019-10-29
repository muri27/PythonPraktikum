n = int(input())

def bintang(x):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print("*", end="")
        print()
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i >= j:
                print("*", end="")
        print()
bintang(n)