import json

# global variables
sprites = {}  # {sprite_name: sprite} The dict contains all the Sprites in this program.
res_file = open('result/main.py', 'w')  # Compiled Python code will be written to this file.

# open Scratch Code File
with open("project_allblocks.json") as f:
    j = json.load(f)
    # Get all Sprites in this program, and store them in 'sprites'.
    for sprite in j['targets']:
        name = sprite['name']
        sprites[name] = sprite

# load format file (which is used to turn Scratch into Py Code)
with open("blocks_format.compiler.config.json") as f:
    FORMAT = json.load(f)  # Load to 'FORMAT'


def parse_sprite(sprite):
    """
    Parse a Sprite.
    :param sprite: a sprite from 'sprites'.
    :return: None. The result will be written to 'res_file' directly.
    """

    def parse_each_block(block_id):
        """
        Parse each block.
        :param block_id: the id of specified block (str) | a value (list)
        :return: the parsed code (or value) as str.
        """

        # if the block is a value, parse it.
        if isinstance(block_id, list):
            # https://en.scratch-wiki.info/wiki/Scratch_File_Format
            return {
                4: lambda x: x[0],  # Number
                5: lambda x: x[0],  # Positive Number
                6: lambda x: x[0],  # Positive Integer
                7: lambda x: x[0],  # Integer
                8: lambda x: x[0],  # Angle
                9: lambda x: "'{}'".format(x[0]),  # Color
                10: lambda x: "'{}'".format(x[0]),  # String
                11: lambda x: "game.broadcast({})".format(x[0]),  # Broadcast
                12: lambda x: "game.var('{}', '{}')".format(x[0], x[1]),  # Variable
                13: lambda x: "game.list('{}', '{}')".format(x[0], x[1]),  # List
            }[block_id[0]](block_id[1:])  # just like 'switch'.
        else:
            # get the block dict and some info.
            block = blocks[block_id]
            opcode = block['opcode']

            # get format of the specified 'opcode', and init.
            _format = FORMAT[opcode]
            code = _format['code']

            # get the number of blanks in format.
            var_counts = code.count('__!')

            # fill the blanks one by one.
            # Blanks is started by '__!' and ended by '!__'.
            for i in range(var_counts):
                # get info
                v_index = code.find('__!')  # index
                v_str = code[v_index + 3:]
                v_str = v_str[:v_str.find("!__")]  # string value
                v_type = v_str.split('.')[0]  # type
                v_path = '.'.join(v_str.split('.')[1:])  # path
                indent = ' ' * _format['indents'][i]  # indent

                # fill the blank
                if v_type == 'fields':
                    # find the target from 'fields/v_path' and fill the blank
                    code = code.replace('__!' + v_str + '!__',  # find blank
                                        eval("block['fields']" + v_path).replace('\n', '\n' + indent),  # add indent
                                        1)  # replace only one times.
                elif v_type == 'inputs':
                    # find the target from 'inputs/v_path' and fill the blank
                    code = code.replace('__!' + v_str + '!__',
                                        parse_each_block(eval("block['inputs']" + v_path)).replace('\n', '\n' + indent),
                                        1)
                else:
                    pass

            if block['next'] is None:
                # if the block is the last block, just return the code.
                return code.strip()
            else:
                # else, parse the next block and return the code.
                code += parse_each_block(block['next'])
                return code.strip()

    # get all blocks
    blocks = sprite['blocks']
    head_blocks = []  # Blocks which are the first block of the script.

    # get head_blocks
    for b_id in blocks:  # b_id for 'block_id'.
        block = blocks[b_id]
        # check if it is a head block.
        if 'when' in block['opcode'] or 'define' in block['opcode']:
            # it's a "head_block".
            head_blocks.append(block)

    # generate code
    class_code_head = "class Generate_{}(scgame.Sprite):\n".format(sprite['name'].replace(' ', '_'))
    class_code = ""
    active_condition_count = {}  # The dict contains the count of each active condition.
    for hb in head_blocks:  # hb for 'head_block'.
        active_condition = hb['opcode']
        active_condition_count[active_condition] = active_condition_count.get(active_condition, 0) + 1
        # parse the second block
        _next = hb['next']
        code = parse_each_block(_next)
        # generate code
        class_code += '\ndef {}_{}(self):\n    {}'.format(active_condition,
                                                          active_condition_count[active_condition],
                                                          code.replace('\n', '\n    ')
                                                          )

    # generate event func.
    for condition in active_condition_count:
        class_code += '\n\ndef {}(self):\n    {}\n\n\n'.format(condition, '\n    '.join(
            ["threading.Thread(target=self.{}_{})".format(condition, i + 1) for i in
             range(active_condition_count[condition])]))

    # write to file
    res_file.write(class_code_head + class_code.replace('\n', '\n    '))


if __name__ == '__main__':
    # write import
    res_file.write("import threading\nimport scgame\n\n")
    parse_sprite(sprites['motion'])
