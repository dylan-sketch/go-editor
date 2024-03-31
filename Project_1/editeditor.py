'''
with open("your_file.txt", "r") as file:
    content = file.read()

# Replace the typo
corrected_content = content.replace("godo", "good")

# Open the file in write mode and write the corrected content back to it
with open("your_file.txt", "w") as file:
    file.write(corrected_content)
'''


import sys


def create_file(filename, word1, word2):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        #replace the typo
        corrected_content = content.replace(word1, word2)

        #write the corrected content
        with open(filename, 'w') as file:
            file.write(corrected_content)
        print(f"file '{filename}' corrected successfully." )
    except Exception as e:
        print(f"error: {e}")


def main():
    if len(sys.argv) != 4:
        print("Usage: goed <filename> "<wrong_text>" "<right_text>"")
        return
    filename = sys.argv[1]
    text_wrong = sys.argv[2]
    text_right = sys.argv[3]


    create_file(filename, text_wrong, text_right)

if __name__ == "__main__":
    main()
