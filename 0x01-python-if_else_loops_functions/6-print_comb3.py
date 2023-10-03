#!/usr/bin/python3
for x in range(0, 8):
    for y in range(0, 10):
        if y > x:
            print(f"{x * 10 + y:02d}, ", end='')
print(89)
