import zipfile
import os

class Sb3File:
    def __init__(self, sb3: dict):
        self.sb3 = sb3

    @classmethod
    def load(source: str) -> dict:
        files = {}
        with zipfile.ZipFile(source, "r") as sb3:
            for file_info in sb3.infolist():
                with sb3.open(file_info) as f:
                    files[file_info.filename] = f.read()

        self = Sb3File(files)
        return self

    def extract_src(self, dest: str) -> None:
        for file_name, content in self.sb3.items():
            if file_name != "project.json":
                # create src/ directory if not exists
                if not os.path.exists(f"{dest}/src"):
                    os.mkdir(f"{dest}/src")

                # extract resources
                with open(f"{dest}/src/{file_name}", "wb") as f:
                    f.write(content)


if __name__ == '__main__':
    sb3 = Sb3File.load('sc3py/compiler/source/Scratch作品.sb3')
    sb3.extract_src('sc3py/compiler/result')
