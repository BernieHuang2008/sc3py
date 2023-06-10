import json

sprites = {}  # {sprite_name: sprite} The dict contains all the Sprites in this program.
res_file = open('result/main.py', 'w')  # The file to save the result.
with open("project.json") as f:  # Load the 'project.json' file.
    j = json.load(f)
    for sprite in j['targets']:  # Get all the Sprites in this program.
        name = sprite['name']  # Get the name of the Sprite.
        sprites[name] = sprite  # Storage the Sprite in the 'sprites'.

with open(
        "blocks_format.compiler.config.json") as f:  # load the format file. It defined how to turn Scratch code into Python code.
    FORMAT = json.load(f)  # Load to 'FORMAT'


def get_blocks(sprite):
    # Get all the blocks of the Sprite.
    def parse_each_block(block_id):
        # Parse each block.

        def get_value(val):
            if val.isdigit():
                return val
            else:
                return "'{}'".format(val)

        if isinstance(block_id, list):
            if len(block_id) == 2:
                return get_value(block_id[1])
            elif len(block_id) == 3:
                return "game.var({}, {})".format(get_value(block_id[1]), get_value(block_id[2]))
            else:
                print('Error: block_id is a list, but the length is not 2 or 3.', block_id)
                return ''

        block = blocks[block_id]  # Get the block.
        opcode = block['opcode']  # Get 'opcode'. (The 'opcode' is the type of the block.)

        _format = FORMAT[opcode]  # Get format of the specified opcode.
        code = _format['code']  # Get scratch code.
        var_counts = code.count(
            '__!')  # Get the number of variables (which will be replaced by compiler) in the scratch code.
        for i in range(var_counts):
            v_index = code.find('__!')  # Index of the variable. VAR is started by '__!' and ended by '!__'.
            v_str = code[v_index + 3:]  # The string of the variable.
            v_str = v_str[:v_str.find("!__")]  # Ending by '!__'.
            v_type = v_str.split('.')[0]  # Get the type of the variable. ('getval' or 'getcode' etc.)
            v_content = '.'.join(v_str.split('.')[1:])  # This is the path shows where to get the content.
            indent = ' ' * _format['indents'][i]  # Indent of this variable.
            if v_type == 'getval':
                # If the type is 'getval', then get the value of the variable and fill the blank directly (adding indent).
                code = code.replace('__!' + v_str + '!__',
                                    eval("block['fields']" + v_content).replace('\n', '\n' + indent))
            elif v_type == 'getcode':
                # If the type is 'getcode', then get the code of the variable and parse it. Fill the blank with the parsed code (adding indent).
                code = code.replace('__!' + v_str + '!__',
                                    parse_each_block(eval("block['inputs']" + v_content)).replace('\n', '\n' + indent))

        if block['next'] is None:
            # if the block is the last block, just return the code.
            return code
        else:
            # else, parse the next block and return the code.
            code += parse_each_block(block['next'])
            return code

    blocks = sprite['blocks']  # Get all the blocks of the Sprite.
    head_blocks = []  # The blocks which are the first block of the script.
    for b_id in blocks:  # b_id is the id of each block.
        block = blocks[b_id]  # Get the block.
        b_toplevel = block["topLevel"]  # If the block is the first block of the script, then 'topLevel' is True.
        if b_toplevel:
            # If the block is a head_block, then add it to 'head_blocks'.
            head_blocks.append(block)

    for hb in head_blocks:  # hb stands for head_block.
        active_condition = hb['opcode']  # Get the active condition of the script.
        _next = hb['next']  # Get the next block's ID of the script.
        code = parse_each_block(_next)  # Parse the next block, the code will be returned.
        res_file.write(
            '\nCONDITION [{}]\n    {}'.format(active_condition, code.replace('\n', '\n    ')))  # Print the code.


if __name__ == '__main__':
    get_blocks(sprites['角色1'])
