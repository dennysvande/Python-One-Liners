#!/usr/bin/python

a = "cat"
b = "chello"
c = "chess"

ls = lambda a, b: len(b) if not a else len(a) if not b else min(ls(a[1:], b[1:]) + (a[0] != b[0]), ls(a[1:], b)+1, ls(a, b[1:])+1)

print(ls(a,b))
print(ls(a,c))
print(ls(b,c))