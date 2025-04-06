# Part 1: File Read & Write Challenge

def modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
            modified_content = content.upper()  # Modify content to uppercase (you can modify as needed)

        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        print(f"Content written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except IOError:
        print("Error: There was an issue with reading or writing the file.")

# Part 2: Error Handling Lab

def get_filename_and_process():
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the output file: ")

    modify_file(input_filename, output_filename)

if __name__ == "__main__":
    get_filename_and_process()
