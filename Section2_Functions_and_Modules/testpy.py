msg = "hello world"
file = open('file4.txt', "w")
writtenAmount = file.write(msg)
print(writtenAmount)
file.close()