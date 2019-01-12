def helpWithFiles():
    """
To work with files, you must first open them. You can open a new file like this:
myfile = open('filename.txt')
* the open has several functionalities, and you can open a file in several different modes: read(r), write(w), append(a), b(binary), binary write mode (wb),create(c) reading and writing (w+), etc.
* Don't forget to close a file after you have opened it, for example:
myfile.close()
* To use the content of a file, use the file.read() method. for example:
myfile.read()
So this is the basic summary when working with files:
"r"
read from file
does not create a new file, or let you write/add to the current file
"r+"
This one actually lets you write to the file
"w"
Does not let you read from the file, instead it creates or overwrites the current file
"""


print("write method")
writeFile = open("testfile2.txt","w")
for i in range(5):
    writeFile.write("This is line "+str(i)+"\n")
    #print(myFile.read(-2)) # Printing a negative(-2), would actually just print the entire file
writeFile.close()
input("At this moment, if you open testfile2.txt, you will see multiple lines. Press enter to continue the execution of the program")


print("write plus method")
writeFile2 = open("testfile2.txt","w+")
writeFile2.write("This is now the only line in the file.")
writeFile2.close()
input("At this moment, I have overwritten the previous testfile2.txt. Now it only has one line")
input("press enter")


print('normal .read() method')
myFile = open("testfile.txt","r")
#contents = myFile.read()
for i in range(5):
    print(myFile.read(5))
    #print(myFile.read(-2)) # Printing a negative(-2), would actually just print the entire file
myFile.close()

print(".readlines() method")
another = open("testfile.txt","r")
for i in range(3):
    print(another.readline())
another.close()

myFile = open("testfile2.txt","r+")
contents = myFile.read()
myFile.write("\nwith r+, you could basically append to the file")
myFile.write("\njust another appended line")
#contents2 = myFile.read() # why is this line not printing any contents, but the file does reflect the changes?
print("")
print("file contents without r+")
print(contents)
myFile.close()

msg = "This is a new file\n"
myFile2 = open("testfile3.txt","w+")
myFile2.write(msg)
myFile2.write(msg+"some random text")
amount_written = myFile2.write(msg)
print(amount_written)
myFile2.close()
#print(helpWithFiles.__doc__)


print("using a with statement to not have to open and close a file:")
with open("file4.txt") as f:
    print(f.read())