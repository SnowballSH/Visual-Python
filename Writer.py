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
    return f"all({i})"


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

    def close(self):
        # Close the file
        self.append_file.close()

    def clear(self):
        with open(self.file_path, "w") as f:
            f.write("")

    @staticmethod
    def deter_type(string):
        value = eval(string)
        type_ = type(value).__name__
        return type_, string

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

    def write(self, string):
        self.f.write(string)

    ##########################
    # Workplace: 12944qwerty #
    # task: compiler program #
    ##########################

    # [We still cannot print vars, and i dunno how to do that.] Fixed by Snowball
    def print_(self, *args, end=None, sep=' '):
        thing = ", ".join(args)
        self.f.write(
            f'print({thing}' + str(f", end={end}" if end is not None else "") + str(
                f", sep={sep}" if sep != ' ' else "") + ")\n")

    ##########################
    # Workplace: Hoax        #
    # task: var assignments  #
    ##########################

    # str, int, float, bool - 4 var types, automatically, its string
    # always accepts strings as input, even if its a int or a boolean

    # var_value must be in '"2"' if string form when input!

    def assign_var(self, var_name, var_value):
        type_, value = self.deter_type(var_value)
        self.f.write(f'{var_name}: {type_} = {value}\n')
