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
    # [We still cannot print vars, and i dunno how to do that.] Fixed by Snowball
    def print_(self, *args, end=r'\n', sep=' '):
        thing = sep.join([str(w) for w in args])
        self.f.write(f'print("{thing}", end="{end}")\n')

    ##########################
    # Workplace: Hoax        #
    # task: var assignments  #
    ##########################

    # str, int, float, bool - 4 var types, automatically, its string
    # always accepts strings as input, even if its a int or a boolean

    def assign_var(self, var_name, var_value, var_type=None):
        if var_type is None:
            type_, value = self.deter_type(var_value)
        else:
            type_ = var_type
            if var_type == 'str':
                value = str(var_value)
            elif var_type == 'int':
                try:
                    int(var_value)
                    value = int(var_value)
                except:
                    raise TypeError("Variable value is not a integer")
            elif var_type == 'float':
                float(var_value)
                value = float(var_value)
                self.f.write(f'{var_name} = {var_value}\n')

            elif var_type == 'bool':
                if var_value not in ["True", "False"]:
                    raise TypeError("Variable value is not a boolean")
                else:
                    value = bool(var_value)

            else:
                value = None

        if type_ == 'str':
            value = f'"{value}"'

        self.f.write(f'{var_name}: {type_} = {value}\n')

    ##########################
    # Workplace: Luka        #
    # task:                  #
    ##########################
