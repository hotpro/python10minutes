mylist = [1, 2, 3]
print mylist[0:2]
print mylist[0:0]
print mylist[0:1]
print mylist[1:1]
print mylist[0:3]
print mylist[0:-1]
mylist.append(4)
mylist.append(5)
mylist.append(6)
print mylist
mylist[0:6:2]

"""
Output
[1, 2]
[]
[1]
[]
[1, 2, 3]
[1, 2]
[1, 2, 3, 4, 5, 6]
"""