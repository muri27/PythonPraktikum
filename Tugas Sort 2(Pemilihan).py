n = input().split()
n_int = int(n[0])
x = []
y = []
x_list=[]
for i in range(n_int):
    m = int(input())
    x.append(m)
for j in range(n_int):
    c = x.count(j)
    y.append(c)
new_y = set(y)
new_y.remove(max(new_y))
a = max(new_y)
for k in range(len(y)-1):
    if y[k] == a:
        x_list.append(y[k])
        
if len(x_list) >= 2:
    print("Waspada Koalisi")
else:
    print(a)