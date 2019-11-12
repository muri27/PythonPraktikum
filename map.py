#Mencari Selisih Terkecil
a = map(int, input().split())
b = sorted(a)
c = []

for i in range(len(b)-1):
    x = b[i+1] - b[i]
    c.append(x)
print(min(c))

#Perkalian Terbesar dan Terkecil
x = map(int, input().split())
y = map(int, input().split())
print(max(x)*min(y))
