import Writer as Wt

w = Wt.Writer("test.py")

w.print_("'Hello'", "'World!'", sep="'|'")

# Testing my var assignment

w.assign_var("stringVar", "'Hello!!'")
w.assign_var("stringVar2", "'5'")
w.assign_var("intVar", "5")
w.assign_var("floatVar", "5.2")
w.assign_var("boolVar", Wt.gt_(3, 4))

w.print_("boolVar")

w.close()
