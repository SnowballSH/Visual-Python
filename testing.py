import Writer as Wt

#####################
# DO NOT IMPORT SYS #
#####################

w = Wt.Writer("test.py")

w.print_("'Hello'", "'World!'", "5", sep="'|'")

# Testing my var assignment

w.assign_var("stringVar", "'Hello!!'")
w.assign_var("stringVar2", "'5'")
w.assign_var("intVar", "5 * 3")
w.assign_var("floatVar", "5.2 + 3/2")
w.assign_var("boolVar", Wt.gt_(3, 4))

w.if_(Wt.all_(Wt.lte(-2, 8), Wt.e("intVar", 15)))
w.print_("boolVar")
w.print_("'Hello'", "'World!'", sep="'$^%'")

w.while_(Wt.gt_(5,6))
w.print_("'Hello There'")
w.end_tab()
w.print_("'Good There'")
w.end_tab()
w.print_("'Goodbye There'")

w.functions("FirstFunction","Hello","there")
w.return_("'World!'","print")
w.end_tab()

w.close()


