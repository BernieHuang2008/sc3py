import json


def find_all_pos(sub, s):
    import re
    return [sub.start() for sub in re.finditer(sub, s)]


sprites = {}
with open("project.json") as f:
    j = json.load(f)
    for s in j['targets']:
        name = s.get('name')
        sprite = sprites[name] = {}
        sprite['isStage'] = s.get('isStage')
        sprite['blocks'] = s.get('blocks')
        sprite['variables'] = s.get('variables')

with open("blocks_format.compiler.config.json") as f:
    FORMAT = json.load(f)


def get_blocks(sprite):
    def parse_each_block(block_id):
        block = blocks[block_id]
        opcode = block['opcode']

        _format = FORMAT[opcode]
        code = _format['code']
        var_counts = code.count('__!')
        for i in range(var_counts):
            v_index = code.find('__!')
            v_str = code[v_index + 3:]
            v_str = v_str[:v_str.find("!__")]
            v_type = v_str.split('.')[0]
            v_content = '.'.join(v_str.split('.')[1:])
            indent = ' ' * _format['indents'][i]
            if v_type == 'getval':
                code = code.replace('__!' + v_str + '!__',
                                    eval("block['inputs']" + v_content).replace('\n', '\n' + indent))
            elif v_type == 'getcode':
                code = code.replace('__!' + v_str + '!__',
                                    parse_each_block(eval("block['inputs']" + v_content)).replace('\n', '\n' + indent))

        if block['next'] is None:
            return code
        else:
            code += parse_each_block(block['next'])
            return code

    blocks = sprite['blocks']
    head_blocks = []
    for b_id in blocks:
        block = blocks[b_id]
        b_toplevel = block["topLevel"]
        if b_toplevel:
            head_blocks.append(block)

    for hb in head_blocks:
        active_condition = hb['opcode']
        _next = hb['next']
        code = parse_each_block(_next)
        print(code)


if __name__ == '__main__':
    get_blocks(sprites['角色1'])
