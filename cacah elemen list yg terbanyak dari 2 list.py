#Menentukan cacah elemen list yg terbanyak dari 2 list
a = list(input())
b = list(input())
besar = 0

def cacahmaks(a,b):
    m = len(a)
    n = len(b)
    if m>n:
        return a
    else:
        return b
    

print(cacahmaks(a,b))  

    