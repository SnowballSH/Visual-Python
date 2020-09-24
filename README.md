# Visual Python - Code Generator

## Members
This team consists of 4 people.<br>
[SnowballSH ![pfp](https://avatars2.githubusercontent.com/u/66022611?s=17&v=4)](https://github.com/SnowballSH) <br>
[12944qwerty ![pfp](https://avatars1.githubusercontent.com/u/45984786?s=17&v=4)](https://github.com/12944qwerty) <br>
[NotLuka ![pfp](https://avatars0.githubusercontent.com/u/59296216?s=17&v=4)](https://github.com/NotLuka) <br>

## The Project
This project is a generator that generates a python file based on how blocks are placed in a GUI. We have 3 main files for this functionality.

- `Writer.py` - A file that writes to the python file. It has a bunch of functions that will write to the file based on the arguments given. The functions are the functions that was parsed from `compiler.py`
- `compiler.py` - A file that grabs the data from `blocks.json` and parses through it. It then passes the data to the functions in `Writer.py`.
- `gui.py` - A file that has the actual GUI. It uses pygame to create the blocks and allows you to drag the blocks. You can type in them as well. Based on the block's positions and how they're stacked, it passes the data into `blocks.json`
