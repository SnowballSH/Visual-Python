# Main Writer for master branch


class Writer:
    def __init__(self, file_path):
        self.file_path = file_path

        self.clear()

        self.append_file = self.f = open(file_path, "a")

    def close(self):
        # Close the file
        self.append_file.close()

    def clear(self):
        with open(self.file_path, "w") as f:
            f.write("")

    ###########################################
    # Example of how your code will look like #
    ###########################################

    def print(self, *args):
        thing = " ".join([str(w) for w in args])
        self.f.write(f'print("{thing}")')

    # In the running file:
    '''
    import Writer
    w = Writer.Writer("try.py")
    w.print("Hello", "World!")
    w.close()
    '''

    # In the target file:
    '''
    print("Hello World!")
    '''
