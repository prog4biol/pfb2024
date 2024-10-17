#!/usr/bin/env python3

s1 = {3, 14, 15, 9, 26, 5, 35, 9}
s2 = {60, 22, 14, 0, 9}

print(f"Set 1              : {s1}")
print(f"Set 2              : {s2}")
print(f"Intersection method: {s1.intersection(s2)}")
print(f"Intersection &     : {s1 & s2}")
print(f"Difference method  : {s1.difference(s2)}")
print(f"Difference -       : {s1 - s2}")
print(f"Union method       : {s1.union(s2)}")
print(f"Union |            : {s1 | s2}")
print(f"SymDiff method     : {s1.symmetric_difference(s2)}")
print(f"SymDiff ^          : {s1 ^ s2}")
