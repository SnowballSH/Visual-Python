# Main Writer for master branch

import os


class Writer:
    def __init__(self, file_path):
        self.file_path = file_path

        # Create file if not exist
        if not os.path.exists(file_path):
            with open(file_path, "x"):
                pass

        self.append_file = self.f = open(file_path, "a")

    def close(self):
        # Close the file
        self.append_file.close()
