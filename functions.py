# an_int and a_string are optional, they have default values
# if one is not passed (2 and "A default string", respectively).
def passing_example(a_list, an_int=2, a_string="A default string"):
	a_list.append("A new item")
	an_int = 4
	return a_list, an_int, a_string

myList = [1, 2, 3]
myInt = 10
print passing_example(myList, myInt)
print myList
print myInt