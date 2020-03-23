l=['a','b','c','b','a','a','c']

#[[x, l.count(x) for x in set(l)]

print(l)

d = dict((x, l.count(x)) for x in set(l))

print(d)
