class_num,count = int(input()),0
for i in range(class_num):
    people = int(input())
    if people > count:
        count = people
print(count)