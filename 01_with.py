strtext = "Hello, World!!!"

try:
    with open("file.txt", "w") as file_out, open("file2.txt", "w") as file2_out:
        print(strtext, file=file_out)
        print(strtext, file=file2_out)
except IOError as e:
    print(e)
