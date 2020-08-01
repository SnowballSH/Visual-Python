"""
This is the compiler file. It will take in the json file and use the Writer class to generate the end result.
"""
from Writer import Writer
import json
import os
import time

gen = Writer("test.py")
blocks = json.load(open("blocks.json", 'r'))

for block, attrs in blocks.items():
    if 'print' in block:
        args = attrs['args']
        end = '\\n'
        sep = ' '
        if 'end' in attrs:
            end = attrs['end'].replace('\n', '\\n')
        if 'sep' in attrs:
            sep = attrs['sep']
        gen.print_(*args, end=end, sep=sep)

gen.close()

divider = ''.join(['-' for _ in range(40)])
print(f"Compiled code. Executing {gen.file_path} in 2 seconds.\n")

time.sleep(2.0)
print(divider)

os.system('python test.py')

print(divider)