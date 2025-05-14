cup = lambda x:x**2

ar = [1,2,3,4,5]

mp = map(cup, ar)

# print(type(mp))
# print(list(mp))



ar2 = filter(lambda x:x>2,ar)
print(type(ar2))
print(ar2)
print(list(ar2))