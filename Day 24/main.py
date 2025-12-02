with open("my_file1.txt") as file:
    contents = file.read()
    print(contents)



with open("New_file.txt","w") as new_file:
    new_file.write("its a new file")