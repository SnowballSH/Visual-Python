# Main Writer for master branch

# builtin funcs

##########################
# Workplace: SnowballSH  #
# task: built-in funcs   #
##########################


def abs_(i):
    return f"abs({i})"


def all_(*args):
    i = ", ".join(args)
    return f"all(({i}))"


def any_(*args):
    i = ", ".join(args)
    return f"any(({i}))"


#####################################
# Added this below - Hoax
def bin_(i):
    return f"bin({i})"


def divmod_(i, j):
    return f"divmod({i}, {j})"


# eval, exec (i dunno how to do)

def filter_(i, j):
    return f"filter({i}, {j})"


def format_(value, format_spec):
    return f".format({value},{format_spec})"


def getattr_(obj, name):
    return f"getattr({obj}, {name})"


def hasattr_(obj, name):
    return f"hasattr({obj}, {name})"


def hash_(obj):
    return f"hash({obj})"


def hex_(x):
    return f"hex({x})"


def id_(obj):
    return f"id({obj})"


###############################
# i dunno if i should put this # - Input function below
###############################

def input_(prompt):
    return f"input({prompt})\n"


def isinstance_(obj, clsinfo):
    return f"isinstance({obj},{clsinfo})\n"


def issubclass_(class_, clsinfo):
    return f"issubclass({class_}, {clsinfo})\n"


# i dunno how to do iter

def len_(i):
    return f"len({i})"


# i also dont know how to do map, max, min (im reading the python docs, i just dunno how to do it)

#####################################
def range_(start, stop="", step=""):
    return f'range({start})' if stop == "" else f'range({start},{stop})' if step == "" else f'range({start},{stop},{step})'


def enum(sequence, start=""):
    return f'enumerate({sequence})' if start == "" else f'enumerate({sequence},{start})'


# operators

##########################
# Workplace: Luka        #
# task: Operators        #
##########################

def gt_(number, number0):
    return f'{number} > {number0}'


def lt_(number, number0):
    return f'{number} < {number0}'


def gte(number, number0):
    return f'{number} >= {number0}'


def lte(number, number0):
    return f'{number} <= {number0}'


def e(number, number0):
    return f'{number} == {number0}'


def summing(number, number0):
    return f'{number} + {number0}'


def substitute(number, number0):
    return f'{number} - {number0}'


def multiply(number, number0):
    return f'{number} * {number0}'


def divide(number, number0):
    return f'{number} / {number0}'


def floor_div(number, number0):
    return f'{number} // {number0}'


def modulus(number, number0):
    return f'{number} % {number0}'


def anding(input0, input1):
    return f'{input0} and {input1}'


def oring(input0, input1):
    return f'{input0} or {input1}'


class Writer:
    def __init__(self, file_path):
        self.file_path = file_path

        self.clear()

        self.append_file = self.f = open(file_path, "a")

        self.vars = None

        self.tab = 0
        self.tab_str = ""

    def close(self):
        # Close the file
        self.append_file.close()

    def clear(self):
        with open(self.file_path, "w") as f:
            f.write("")

    def update_tab(self, amount=0):
        self.tab = amount
        self.tab_str = " " * 4 * amount

    def comment(self, text: str):
        self.write("# " + text + "\n")

    def blank(self, amount: int = 1):
        self.write("\n" * amount)

    @staticmethod
    def deter_type(string):
        try:
            value = eval(string)
            type_ = type(value).__name__
            return type_, string
        except NameError:
            return None, string

    """
    @staticmethod
    def safe_deter_type(string):
        value = string

        if any([(a in string) for a in "+,-,*,/,//,%".split(",")]):
            return 'float', value

        if '.' in string:
            if string.replace('.', '', 1).replace('-', '', 1).isdigit():
                value = float(string)
                return 'float', value

        try:
            value = int(string)
            return 'int', value
        except ValueError:
            pass

        if string in ["True", "False"] or any([a in string for a in ">,<,>=,<=,==,and,or".split(",")]):
            return 'bool', value

        return 'str', value
        
    """

    def write(self, string, no_tab=False):
        ts = self.tab_str if not no_tab else ""
        self.f.write(ts + string)

    def print_(self, *args, end=None, sep=' ', write=True):
        thing = ', '.join(args)
        p = f"print({thing}" + str(f", end={end}" if end is not None else "") + str(
            f", sep={sep}" if sep != ' ' else "") + ")\n"
        if write:
            self.write(p)
        return p

    def end_tab(self):
        self.update_tab(self.tab - 1)

    def if_(self, statement):
        self.write(f'if {statement}:\n')
        self.update_tab(self.tab + 1)

    def while_(self, statement):
        self.write(f'while {statement}:\n')
        self.update_tab(self.tab + 1)

    def functions(self, name, *args):
        arguments = ", ".join(args)
        self.write(f'def {name}({arguments}):\n')
        self.update_tab(self.tab + 1)

    def return_(self, output):
        self.write(f'return {output}\n')

    def callFunction(self, name, *args):
        arguments = ", ".join(args)
        self.write(f'{name}({arguments})')

    # str, int, float, bool - 4 var types, automatically, its string
    # always accepts strings as input, even if its a int or a boolean

    # var_value must be in '"2"' form if string form when input!

    def assign_var(self, var_name, var_value):
        type_, value = self.deter_type(var_value)
        self.write(f'{var_name}{f": {type_}" if type_ is not None else ""} = {value}\n')
