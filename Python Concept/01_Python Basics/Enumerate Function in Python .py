ar = [3,4,6,6,7,8,9]
for i in enumerate(ar):
    print(i)
    print(type(i))

for ind,val in enumerate(ar):
    print(ind)
    print(val)
    print(type(val))
    print(type(ind))
    print("Index is {} and value is {}".format(ind,val))
    print("Index is {} and value is {}".format(ind,val),end="\n\n")



for ind,val in enumerate(ar,start=4):
    print(ind)
    print(val)
    print(type(val))
    print(type(ind))
    print("Index is {} and value is {}".format(ind,val))
    print("Index is {} and value is {}".format(ind,val),end="\n\n")