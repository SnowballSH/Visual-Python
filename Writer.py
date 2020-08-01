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

def gt_(self, number, number0):
    return f'{number} > {number0}'


def lt_(self, number, number0):
    return f'{number} < {number0}'


def gte(self, number, number0):
    return f'{number} >= {number0}'


def lte(self, number, number0):
    return f'{number} <= {number0}'


def e(self, number, number0):
    return f'{number} == {number0}'


def summing(self, number, number0):
    return f'{number} + {number0}'


def substitute(self, number, number0):
    return f'{number} - {number0}'


def multiply(self, number, number0):
    return f'{number} * {number0}'


def divide(self, number, number0):
    return f'{number} / {number0}'


def divideWithIntegralResult(self, number, number0):
    return f'{number} // {number0}'


def modulus(self, number, number0):
    return f'{number} % {number0}'


def anding(self, input0, input1):
    return f'{input0} and {input1}'


def oring(self, input0, input1):
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
        value = string

        if '.' in string:
            if string.replace('.', '', 1).isdigit():
                value = float(string)
                return 'float', value

        try:
            value = int(string)
            return 'int', value
        except ValueError:
            pass

        if string in ["True", "False"]:
            return 'bool', value

        return 'str', value

    ##########################
    # Workplace: 12944qwerty #
    # task: compiler program #
    ##########################

    # Added r to \n because it prints a newline, not add the \n
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
