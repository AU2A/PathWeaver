import argparse, os


class printFolder:
    def __init__(self, path):
        self.path = os.path.normpath(path)
        print(f"{self.path}/")
        self.printFolderTree(path, " ")

    def printFolderTree(self, path, prefix):
        if len(os.listdir(path)) == 0:
            return
        lastFile = os.listdir(path)[-1]
        for file in os.listdir(path):
            print(prefix, end="")
            if os.path.isdir(os.path.join(path, file)):
                print(f"{"┗" if file == lastFile else "┣"}━ {file}/")
                self.printFolderTree(
                    os.path.join(path, file), prefix + ("    " if file == lastFile else "┃   ")
                )
            else:
                print(f"{"┗" if file == lastFile else "┣"}━ {file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path where you want to create.", type=str)
    args = parser.parse_args()
    printFolder(args.path)
