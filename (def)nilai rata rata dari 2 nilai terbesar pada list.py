#Menampilkan nilai rata rata dari 2 nilai terbesar pada list

x = list(input())
n = len(x)

def rata2maks(x):
    if x[0] > x[1]:
        maks1 = x[0]
    else:
        maks1 = x[1]
    for i in range(2, n):
        if x[i] > maks1:
            maks2 = maks1
            maks1 = x[i]
        elif x[i] > maks2:
            maks2 = x[i]
    return ((int(maks1)+(int(maks2)))/2)

print(rata2maks(x))