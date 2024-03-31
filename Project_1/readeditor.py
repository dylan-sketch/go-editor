import sys


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(content)
    except Exception as e:
        print(f"error: {e}")


def main():
    if len(sys.argv) != 2:
        print("Usage: goed <filename>")
        return
    filename = sys.argv[1]

    read_file(filename)

if __name__ == "__main__":
    main()
