#Bubblesort
def Bubblesort(x):
    n = len(x)
    for i in range (n-1):
        for j in range (n-1):
            if x[j]>x[j+1]:
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
A=[2,10,23,4,14]
Bubblesort(A)
print(A)

#Selectionsort
def Selectionsort(x):
     n = len(x)
     for i in range(n-1):
         pos = i
         mm = x[i]
         for j in range(i+1, n):
             if x[j]<mm:
                 mm = x[j]
                 pos = j
         if pos != i:
             temp = x[i]
             x[i] = x[pos]
             x[pos] = temp
             
B = [3,42,5,2,4,10]
Selectionsort(B)
print(B)

#Insertionsort
def insertionsort(x):
 
    # traverse dari 1 sampai len(arr)
    for i in range(1, len(x)):
 
        key = x[i]
 
        # Pindahkan elemen arr[0...i-1], yang lebih besar
        # dari key, satu posisi ke kanan
        # dari posisi sekarang
        j = i-1
        while j >=0 and key < x[j] :
                x[j+1] = x[j]
                j -= 1
        x[j+1] = key
 
 
# testing
x = [12, 11, 13, 5, 6]
insertionsort(x)
print ("Sorted array: ")
for i in range(len(x)):
    print ("%d" %x[i], end=" ")