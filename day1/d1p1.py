#!/usr/bin/env python3
print(sum(map(lambda digits: int(f"{digits[0]}{digits[-1]}"),list(map(lambda line: [c for c in line if c in [str(d) for d in list(range(10))]],open("input.txt", "r").readlines())))))
