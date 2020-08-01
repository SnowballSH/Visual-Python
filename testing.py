  
import Writer

w = Writer.Writer("test.py")

w.print_("Hello", "World!")

#Testing my var assignment
w.assignVar("stringVar", "Hello!!", 'str')
w.assignVar("stringVar2", "5", 'str')
w.assignVar("intVar", "5", 'int')
w.assignVar("floatVar", "5", 'float')
w.assignVar("boolVar", "True", 'bool')

w.close()

