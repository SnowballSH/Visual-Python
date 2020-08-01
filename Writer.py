  
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

    ###########################################
    # Example of how your code will look like #
    ###########################################

    '''
    def print(self, *args):
        thing = " ".join([str(w) for w in args])
        self.f.write(f'print("{thing}")')
    '''

    # In the running file:
    '''
    import Writer
    w = Writer.Writer("test.py")
    w.print("Hello", "World!")
    w.close()
    '''

    # In the target file:
    '''
    print("Hello World!")
    '''

    ##########################
    # Workplace: 12944qwerty #
    # task: compiler program #
    ##########################

    ##########################
    # Workplace: SnowballSH  #
    # task: built-in funcs   #
    ##########################

    #Added r to \n because it prints a newline, not add the \n
    #We still cannot print vars, and i dunno how to do that.
    def print_(self, *args, end=r'\n', sep=' '):
        thing = sep.join([str(w) for w in args])
        self.f.write(f'print("{thing}",end="{end}")\n')

    ##########################
    # Workplace: Hoax        #
    # task: var assignments  #
    ##########################
    
    #str, int, float, bool - 4 vartypes, automatically, its string
    #always accepts strings as input, even if its a int or a boolean
    def assignVar(self, varName, varValue, varType='str'):
        if varType == 'str':
            self.f.write(f'{varName} = "{varValue}"\n')
        elif varType == 'int':
            try:
                int(varValue)
                self.f.write(f'{varName} = {varValue}\n')
            except:
                raise TypeError("Variable value is not a integer")
        elif varType == 'float':
            float(varValue)
            self.f.write(f'{varName} = {varValue}\n')

        elif varType == 'bool':
            if varValue not in ["True", "False"]:
                raise TypeError("Variable value is not a boolean")
            else:
                self.f.write(f'{varName} = {varValue.title()}\n')
            
    
    ##########################
    # Workplace: Luka        #
    # task:                  #
    ##########################
