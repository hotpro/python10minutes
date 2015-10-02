def some_functions():
	try:
		10 / 0
	except ZeroDivisionError:
		print("Ops, invalid")
	finally:
		print("we are done")
some_functions()