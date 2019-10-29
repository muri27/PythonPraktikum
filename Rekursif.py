#Rekursif
def tes(n):
    if n > 0:
        tes(n//2)
        print(n%2, end="")

tes(20)
tes(40)

print()
print()
 
def bintang(n):
    if (n==1):
        print("*")
    else:
        bintang(n-1)
        for i in range(n):
            print("*", end="")
        print()
        bintang(n-1)
    
bintang(3)
bintang(4)

print()
print()

def segitiga(n):
    if (n==1):
        print("*")
    else:
        segitiga(n-1)
        for i in range(n):
            print("*", end="")
        print()

segitiga(4)