#!/usr/bin/env python3
from functools import reduce
z = list(map(lambda line: reduce(lambda a, kv: a.replace(*kv), [("one","1one"),("two","2two"),("three","3three"),("four","4four"),("five","5five"),("six","6six"),("seven","7seven"),("eight","8eight"),("nine","9nine")], line), open("input.txt", "r").readlines()))

print(z)

y = map(
lambda line: str([c for c in line if c in [str(d) for d in list(range(10))]]), z
    )
    
x = map(
lambda digits: int(f"{digits[0]}{digits[-1]}"),
list(y))

print(sum(
x
))
