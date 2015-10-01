s1 = "Hello"
s2 = " World."
print s1 + s2
print s1
print s2

print "swap in one line"
s1, s2 = s2, s1
print s1 + s2
print s1
print s2
"""
Output
Hello World.
Hello
 World.
swap in one line
 World.Hello
 World.
Hello
"""