"""
This is the compiler file. It will take in the json file and use the Writer class to generate the end result.
"""
from Writer import Writer
import json
import os
import time

gen = Writer("test.py")
blocks = json.load(open("blocks.json", 'r'))

def parse(blocks):
    for block, attrs in blocks.items():
        if 'print' in block:
            args = attrs['args']
            end = None
            sep = ' '
            if 'end' in attrs:
                end = attrs['end'].replace('\n', '\\n')
            if 'sep' in attrs:
                sep = attrs['sep']
            gen.print_(*args, end=end, sep=sep)
        if 'if' in block:
            conditional = attrs['condition']
            gen.if_(conditional)
            parse(attrs['blocks'])
            gen.end_if()

parse(blocks)

gen.close()

divider = ['-' for _ in range(180)]
print(f"Compiled code. Executing {gen.file_path} in 2 seconds.\n")

time.sleep(2.0)
print(*divider,'\n',sep='')

os.system('python test.py')

print('\n',*divider,sep='')