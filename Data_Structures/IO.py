myfile = open("test.txt", "w")
myfile.write("Hello World")
myfile.close()

my_new_file = open("file.txt", "w")
my_new_file.write("Hello")
my_new_file.close()

# print(my_new_file.read())  # This line will throw an error because the file is opened in write mode, not read mode.
my_new_file = open("file.txt", "r")
print(my_new_file.read())  # This will print the content of the file, which is "Hello"
my_new_file.close()

my_new_file = open("file.txt", "a")
my_new_file.write(" World") 
my_new_file.close()

my_new_file = open("file.txt", "r")
print(my_new_file.readlines())