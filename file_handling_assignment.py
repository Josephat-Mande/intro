filecontent="my_file.txt","x"

# Create a new file with the given content

with open('my_file.txt', 'w') as file:
    file.write("filecontent")
    file.write("linetwo")
    file.write("line3")
    print("File created successfully.")

    file.close()
    print("File closed successfully.")
    
    

        # Read the content of the file
        
with open('my_file.txt', 'r') as file:
            file_content = file.read()
            print("File content:", file_content)