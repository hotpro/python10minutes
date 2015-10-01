
print "Name %s\
Number %s\
String %s" % ("hello", 3, 3 * "-")

strString = """This is 
a multilines
strng"""
print strString

# WARNING: Watch out for the trailing s in "%(key)s".
print "This %(verb)s a %(noun)s" % {"noun": "test", "verb": "is"}
"""
Output
Name helloNumber 3String ---
This is
a multilines
strng
This is a test
"""
