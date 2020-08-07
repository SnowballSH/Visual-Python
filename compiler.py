"""
This is the compiler file. It will take in the json file and use the Writer class to generate the end result.
"""
from Writer import *
import json
import os

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
            gen.print_(args, end=end, sep=sep)
        if 'if' in block:
            conditional = attrs['condition']
            gen.if_(conditional)
            parse(attrs['blocks'])
            gen.end_tab()
        if 'while' in block:
            condition = attrs['condition']
            gen.while_(condition)
            parse(attrs['blocks'])
            gen.end_tab()
        if 'func' in block:
            name = attrs['name']
            args = attrs['args']
            gen.functions(name, *args)
            parse(attrs['blocks'])
            gen.end_tab()
        if 'return' in block:
            output = attrs['output']
            gen.return_(output)
        if 'var' in block:
            gen.assign_var(attrs['name'], attrs['value'])
        if 'comment' in block:
            gen.comment(attrs['args'])
        if 'invoke' in block:
            func = attrs['function']
            args = attrs['args']
            gen.callFunction(func, *args)

        if 'eval' in block:  # DEVELOPMENT PURPOSES ONLY
            gen.write(attrs["statement"])


def test_case():
    from time import sleep

    parse(blocks)

    gen.close()

    divider = ['-' for _ in range(180)]
    print(f"Compiled code. Executing {gen.file_path} in 2 seconds.\n")

    sleep(2.0)
    print(*divider, '\n', sep='')

    os.system('python test.py')

    print('\n', *divider, sep='')


# test_case()
