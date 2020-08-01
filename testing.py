import Writer

w = Writer.Writer("test.py")

w.print_("Hello", "World!")

# Testing my var assignment

w.assign_var("stringVar", "Hello!!", 'str')
w.assign_var("stringVar2", "5", 'str')
w.assign_var("intVar", "5", 'int')
w.assign_var("floatVar", "5", 'float')
w.assign_var("boolVar", "True", 'bool')

w.close()
