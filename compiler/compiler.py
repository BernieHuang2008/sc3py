import json

# settings
SETTINGS = {
    "comment": False,
}

# global variables
sprites = {}  # {sprite_name: sprite} The dict contains all the Sprites in this program.
res_file = open(
    "result/main.py", "w", encoding="utf-8"
)  # Compiled Python code will be written to this file.

# open Scratch Code File
with open("project_allblocks.json", encoding="utf-8") as f:
    j = json.load(f)
    # Get all Sprites in this program, and store them in 'sprites'.
    for sprite in j["targets"]:
        name = sprite["name"]
        sprites[name] = sprite

# load format file (which is used to turn Scratch into Py Code)
with open("sc_code_format.compiler.json") as f:
    FORMAT = json.load(f)  # Load to 'FORMAT'


def acceptable(
    e, v_type, v_path, block_id
):  # check if the error during parsing is accpectable.
    error_code = "//".join([str(e), v_type, v_path])
    if error_code in ["'SUBSTACK2'//inputs//['SUBSTACK2'][1]"]:
        return "[√]"
    else:
        print("=" * 10, "UNACCEPTABLE ERROR", "=" * 10)
        print(f"at block '{block_id}'")
        print(f"format path: {v_type}.{v_path}")
        raise e


def parse_sprite(sprite):
    """
    Parse a Sprite.
    :param sprite: a sprite from 'sprites'.
    :return: None. The result will be written to 'res_file' directly.
    """

    def parse_each_block(block_id, inline=False):
        """
        Parse each block.
        :param block_id: the id of specified block (str) | a value (list)
        :return: the parsed code (or value) as str.
        """

        def fill_blanks(block, code, indents):
            """
            Fill the blanks in the code.

            :param block: the block dict.
            :param code: the code to fill.
            :param indents: the indents of each blank.
            :return: the filled code.

            :param block_id (hidden): the id of the block, just for exception catch use.
            :param parse_each_block (hidden): recursive function.
            """

            # get the number of blanks in format.
            var_counts = code.count("__!")

            # fill the blanks one by one.
            # Blanks starts by '__!' and ended by '!__'.
            for i in range(var_counts):
                # get info
                v_index = code.find("__!")  # index
                v_str = code[v_index + 3 :]
                v_str = v_str[: v_str.find("!__")]  # string value
                v_type = v_str.split(".")[0]  # type
                v_path = ".".join(v_str.split(".")[1:])  # path
                indent = " " * indents[i]  # indent

                # fill the blank
                try:
                    blank_value = eval(f"block['{v_type}']{v_path}")
                except KeyError as e:
                    print(f"[*] KeyError: {e} in <{block_id}>", acceptable(e, v_type, v_path, block_id))
                    blank_value = "None"
                inline = (
                    code[code.find("__!" + v_str + "!__") - 2] != " "
                )  # check if the blank is in a line.

                if v_type == "fields":
                    # find the target from 'fields/v_path' and fill the blank
                    code = code.replace(
                        "__!" + v_str + "!__",  # find blank
                        blank_value.replace("\n", "\n" + indent),  # add indent
                        1,
                    )  # replace only one times.
                elif v_type == "inputs":
                    # find the target from 'inputs/v_path' and fill the blank
                    code = code.replace(
                        "__!" + v_str + "!__",
                        parse_each_block(blank_value, inline=inline).replace(
                            "\n", "\n" + indent
                        ),
                        1,
                    )
                else:
                    raise KeyError(f"Unknown type '{v_type}'.")
            
            return code

        # if the block is a instant value/var reference, return its value.
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
            }[block_id[0]](
                block_id[1:]
            )   # switch-case
        elif block_id in blocks:
            # get the block dict and some info.
            block = blocks[block_id]
            opcode = block["opcode"]

            # get format of the specified 'opcode', and init.
            _format = FORMAT[opcode]
            code = _format["code"]

            # fill in blanks
            code = fill_blanks(block, code, _format["indents"])
                
            # comment
            if SETTINGS["comment"] and _format["comment"] is not None:
                comment = _format["comment"]
                comment = fill_blanks(block, comment, [0] * comment.count("__!"))
                clst = code.split("\n", 1)
                code = clst[0] + "  # " + comment + "\n" + clst[1]

            if block["next"] is None:
                # if the block is the last block, just return the code.
                return code.strip()
            else:
                # else, parse the next block and return the code.
                code += parse_each_block(block["next"])
                return code.strip()
        else:
            if inline:
                return "None"
            else:
                return "...  # TODO: Please complete the code here."

    # get all blocks
    blocks = sprite["blocks"]
    hat_blocks = []  # Blocks which are the first block of the script.

    # get hat blocks
    for b_id in blocks:  # b_id for 'block_id'.
        block = blocks[b_id]
        # check if it is a hat block.
        if "when" in block["opcode"] or "define" in block["opcode"]:
            # it's a "hat block".
            hat_blocks.append(block)

    # generate code
    class_code_head = "class Generate_{}(scgame.Sprite):\n".format(
        sprite["name"].replace(" ", "_")
    )
    class_code = "    def __init__(self):\n    super().__init__()\n\n"
    active_condition_count = {}  # The dict contains the count of each active condition.

    # parse the first block as the entrance.
    for hb in hat_blocks:  # hb for 'hat block'.
        active_condition = hb["opcode"]
        if hb["opcode"] == "event_whenbroadcastreceived":
            active_condition += "_" + hb["fields"]["BROADCAST_OPTION"][0]

        active_condition_count[active_condition] = (
            active_condition_count.get(active_condition, 0) + 1
        )

        # parse the second block
        _next = hb["next"]
        code = parse_each_block(_next)

        # generate code
        class_code += "\ndef {}_{}(self):\n    {}".format(
            active_condition,
            active_condition_count[active_condition],
            code.replace("\n", "\n    "),
        )

    # generate event func.
    for condition in active_condition_count:
        class_code += "\n\ndef {}(self):\n    threads = [\n        {}\n    ]\n".format(
            condition,
            ",\n    ".join(
                [
                    "threading.Thread(target=self.{}_{})".format(condition, i + 1)
                    for i in range(active_condition_count[condition])
                ]
            ),
        )
        class_code += "\n    all(t.start() for t in threads)\n    return threads"

    # write to file
    res_file.write("\n" + class_code_head + class_code.replace("\n", "\n    "))


if __name__ == "__main__":
    # write import
    res_file.write("import threading\nimport scgame\ngame={}\n\n")  # import + `game={}`(just avoiding errors)
    print(list(sprites.keys()))
    parse_sprite(sprites["motion"])
    parse_sprite(sprites["looks"])
    parse_sprite(sprites["sound"])
    parse_sprite(sprites["events"])
    parse_sprite(sprites["control"])
    # parse_sprite(sprites['sensing'])
    # parse_sprite(sprites['operators'])
    # parse_sprite(sprites['variables'])
