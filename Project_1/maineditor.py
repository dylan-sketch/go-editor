import sys


def create_file(filename, text):
    try:
        with open(filename, 'w') as file:
            file.write(text)
        print(f"file '{filename}' created successfully." )
    except Exception as e:
        print(f"error: {e}")


def main():
    if len(sys.argv) != 3:
        print("Usage: goed <filename> <text>")
        return
    filename = sys.argv[1]
    text = sys.argv[2]

    create_file(filename, text)

if __name__ == "__main__":
    main()




