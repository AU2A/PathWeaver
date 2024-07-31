import argparse, fnmatch, os


class printFolder:
    def __init__(self, args):
        self.depth = args.depth
        self.ignore = []
        self.path = args.path

        if args.ignore != "":
            if not os.path.exists(args.ignore):
                print(f"{args.ignore} not found. Creating new file.")
                with open(args.ignore, "w") as f:
                    f.write("")
            self.ignore = open(args.ignore).read().split("\n")

        self.output = f"{os.path.basename(os.path.dirname(self.path))}/"

        self.printFolderTree(args.path, " ", 1)
        with open(args.output, "w") as f:
            f.write(self.output)

    def isIgnored(self, file):
        for i in self.ignore:
            if fnmatch.fnmatch(file, i):
                return True
        return False

    def printFolderTree(self, path, prefix, depth):
        if depth > self.depth:
            return
        if len(os.listdir(path)) == 0:
            return
        files = []
        for file in os.listdir(path):
            if self.isIgnored(file):
                continue
            files.append(file)

        lastFile = files[-1]
        for file in files:
            self.output += "\n" + prefix
            if os.path.isdir(os.path.join(path, file)):
                if file == lastFile:
                    self.output += f"┗━ {file}/"
                else:
                    self.output += f"┣━ {file}/"
                self.printFolderTree(
                    os.path.join(path, file),
                    prefix + ("    " if file == lastFile else "┃   "),
                    depth + 1,
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
    parser.add_argument(
        "-i", "--ignore", help="Ignore files or folders.", type=str, default=""
    )
    parser.add_argument(
        "-d", "--depth", help="Depth of the folder tree.", type=int, default=3
    )
    args = parser.parse_args()
    printFolder(args)
