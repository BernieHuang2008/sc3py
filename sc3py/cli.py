import argparse


def main():
    parser = argparse.ArgumentParser(description="Compile Scratch 3.0 project to Python Code.")
    parser.add_argument("-i", "--input", help="Path to the '.sb3' project file", required=True)
    parser.add_argument("-o", "--output", help="Path to the output Python file", required=False)
    args = parser.parse_args()

    print(args)

    # with open(args.project, encoding="utf-8") as f:
    #     project = json.load(f)

    # with open(args.output, "w", encoding="utf-8") as res_file:
    #     res_file.write("import scgame\n")
    #     res_file.write("import threading\n\n")

    #     for sprite in project["targets"]:
    #         compile_sprite(sprite, res_file)