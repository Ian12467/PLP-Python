def modify_file(input_filename, output_filename):
    # Open the input file for reading
    file = open(input_filename, "r")
    content = file.read()  # Read the entire content
    file.close()  # Close the input file
    
    # Modify the content (Example: convert to uppercase)
    modified_content = content.upper()

    # Open the output file for writing
    new_file = open(output_filename, "w")
    new_file.write(modified_content)  # Write modified content to new file
    new_file.close()  # Close the output file
    print(f"Modified content has been written to {output_filename}")

# Ask the user for a filename
input_filename = input("Enter the filename to read from: ")
output_filename = input("Enter the filename to write the modified content to: ")

# Check if input file exists
import os
if os.path.exists(input_filename):
    # Call the function to modify the file
    modify_file(input_filename, output_filename)
else:
    print(f"The file '{input_filename}' does not exist.")
