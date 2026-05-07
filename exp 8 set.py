#creating the new set
a={1,2,3,4,5,6,7,8,9,10,10,10,'divakar'}
print(a)

#type of datatype
print(type(a))

#length of set
print(len(a))

#adding new value in set
a.add(20)
print(a)
#more value adding at a time in set
a.update([30,40,50,60])
print(a)
#removing value from the set
a.remove(60)
print(a)

#pop operation
a.pop()
print(a)

#membership opearation /boolen opearation
print(200 in a)