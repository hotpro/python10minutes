import pickle
mylist = ["This", "is", 4, 1234]
myfile = open("binary.dat", "wb")
pickle.dump(mylist, myfile)
myfile.close()

myfile = open("binary.dat", "rb")
loadedlist = pickle.load(myfile)
print(loadedlist)

myfile = open("text.txt", "w")
myfile.write("This is a sample string")
myfile.close()

myfile = open("text.txt", "r")
print(myfile.read())
myfile.close()