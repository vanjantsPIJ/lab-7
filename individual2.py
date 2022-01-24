#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import math

if __name__ == '__main__':
    A = list(map(float, input().split()))
    neven = 0
for i in range(len(A)):
    if (i % 2) > 0:
        neven += A[i]

print("Сумма элемментов нечетных индексов: ",neven)

sum = 0

for i in range(len(A)):
    if A[i] < 0:
        first = i+1
        break

for j in range(len(A)):
    if A[j] < 0:
        second = j

print(A)
print(first, ' ', second)

for z in range(first, second):
    print("/", A[z])
    sum = sum + A[z]

print(sum)