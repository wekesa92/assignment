# File Read & Write Challenge

# Open the input file and read contents
with open("input.txt", "r") as infile:
    content = infile.read()

# Modify the content (example: make it uppercase)
modified_content = content.upper()

# Write the modified content to a new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("File has been read and modified version written to output.txt")

# Error Handling Lab

try:
    # Ask user for filename
    filename = input("Enter the filename to read: ")

    # Try opening the file
    with open(filename, "r") as file:
        content = file.read()

    print("File content successfully read:")
    print(content)

except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
