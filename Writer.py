# Main Writer for master branch


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

    ##########################
    # Workplace: SnowballSH  #
    # task: built-in funcs   #
    ##########################

    # Added r to \n because it prints a newline, not add the \n
    # We still cannot print vars, and i dunno how to do that.
    def print_(self, *args, end=r'\n', sep=' '):
        thing = sep.join([str(w) for w in args])
        self.f.write(f'print("{thing}", end="{end}")\n')

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

    ##########################
    # Workplace: Luka        #
    # task:                  #
    ##########################
