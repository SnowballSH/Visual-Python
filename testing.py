import Writer as Wt

#####################
# DO NOT IMPORT SYS #
#####################

w = Wt.Writer("test.py")

w.print_("'Hello'", "'World!'", "5", sep="'|'")

w.blank()

# Testing my var assignment

w.assign_var("stringVar", "'Hello!!'")
w.assign_var("stringVar2", "'5'")
w.assign_var("intVar", "5 * 3")
w.assign_var("floatVar", "5.2 + 3/2")
w.assign_var("boolVar", Wt.gt_(3, 4))

w.blank(2)

w.if_(Wt.all_(Wt.lte(-2, 8), Wt.e("intVar", 15)))
w.print_("boolVar")
w.print_("'Hello'", "'World!'", sep="'$^%'")

w.blank()
w.while_(Wt.gt_(5, 6))
w.print_("'Hello There'")
w.end_tab()
w.print_("'Good There'")
w.end_tab()
w.print_("'Goodbye There'")

w.blank(2)
w.functions("my_func", "int_: int")
w.print_("int_")
w.return_(w.print_("'Idk why you return a print'", "'but ok'", end="'...\\n'", write=False))
w.end_tab()
w.blank()
w.print_("my_func(intVar)")

w.close()
