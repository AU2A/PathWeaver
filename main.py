import argparse, os


class printFolder:
    def __init__(self, args):
        self.path = args.path
        self.output = f"{os.path.basename(os.path.dirname(self.path))}/"
        self.printFolderTree(args.path, " ")
        with open(args.output, "w") as f:
            f.write(self.output)

    def printFolderTree(self, path, prefix):
        if len(os.listdir(path)) == 0:
            return
        lastFile = os.listdir(path)[-1]
        for file in os.listdir(path):
            self.output += "\n" + prefix
            if os.path.isdir(os.path.join(path, file)):
                if file == lastFile:
                    self.output += f"┗━ {file}/"
                else:
                    self.output += f"┣━ {file}/"
                self.printFolderTree(
                    os.path.join(path, file),
                    prefix + ("    " if file == lastFile else "┃   "),
                )
            else:
                if file == lastFile:
                    self.output += f"┗━ {file}"
                else:
                    self.output += f"┣━ {file}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path where you want to create.", type=str)
    parser.add_argument(
        "-o", "--output", help="Output file name.", type=str, default="output.txt"
    )
    args = parser.parse_args()
    printFolder(args)
