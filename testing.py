import Writer

w = Writer.Writer("test.py")

w.print_("'Hello'", "'World!'", sep="|")

# Testing my var assignment

w.assign_var("stringVar", "'Hello!!'")
w.assign_var("stringVar2", "'5'")
w.assign_var("intVar", "5")
w.assign_var("floatVar", "5.2")
w.assign_var("boolVar", "True")

w.print_("intVar")

w.gt_(5,6)
w.lt_(2,9)
w.gte(189,3929)
w.lte(29229,2828)
w.e(22,39)

w.summing(28,40)
w.substitute(299,292)
w.multiply(2929,191)
w.divide(2992,393883)
w.divideWithIntegralResult(27,103)
w.modulus(22,48)

w.anding(True, False)
w.oring(False, True)


w.close()
