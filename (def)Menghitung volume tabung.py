#Menghitung volume tabung
import math

r = int(input())
t = int(input())

def volume(r,t):
    volume = math.pi * pow(r, 2) * t
    return volume

print(volume(r,t))