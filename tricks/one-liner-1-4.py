#!/usr/bin/python

txt = ['lambda functions are anonymous functions.',
'anonymous functions dont have a name.',
'functions are objects in Python.']

mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)

lst = [(True, line) if 'anonymous' in line else (False, line) for line in txt]

print(lst)

print(list(mark))