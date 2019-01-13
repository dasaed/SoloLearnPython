from math import pi
print("Tuples are like lists, except that they are inmutable.")
myName = ("Carlos","Dasaed", "Salcedo")
myWife = "Erika","Paola", "Prada" # This is a tuple too
print(myName[0])
print(myWife[1])


print("#####################################################")
myBrother = ["Joshua","Isaac", "Salcedo", "Carreno"]
print(str(myBrother[0:1]) + " " + str(myBrother[2:3]))
print("you can also print from begining to a certain point, or from a certain point to the end")
print(myName[:2])
print(myBrother[2:])

print("######################## list comprenhension #############################")
evenCubes = [i**3 for i in range(11) if i**3 %2 ==0]
print(evenCubes)
reverseList = [1,2,3,4,5,6,7,8,9,10]
print(reverseList[::-1])
print("######################## String Formatting #############################")
primes = [2,3,5,7,11,13,17,19,29]
print("Some Prime Numbers: {0} {1} {2}".format(primes[3],primes[2],primes[1]) )
a ="{alpha}{omega}".format(alpha="-Infinity",omega="+Infinity")
print(a)

print("######################## Other Useful String Functions #############################")
print("Strings have many useful methods, like: join, replace, startswith, endswith, upper, lower, and split, amongst many others")
print(".join()")
print(str(primes[0:3]))
print("|".join(str(primes[0:3])))#Weird how this generates all those extra characters
a = "The First Odd Primes: "+"".join(str(primes[1:4]))
print(a)
print(".replace()")
print(a.replace("The First Odd Primes:","First odd Numbers" ))
print(".startswith()")
print(a.startswith("The"))
print(".endswith()")
print(a.endswith("10101010101010"))
print(".upper()")
print(a.upper())
print(".lower()")
print(a.lower())
print(".split()")
print(a)
print(a.split(":")[1])
b=a.split(":")[1]
print("This is a: "+a+"\n"+"This is b: "+b)


print("######################## Other Useful Number Functions #############################")
lis=[i/3 for i in range(6)]#lis =  changeble
tup=(-1,1,7,5,3,15,37,41,25,26,32,50,71,80)#tup = unchangeable
dic={"wife":1992,"mom":1970, "dad":1968, "brother":2004, "I":1991}#dictionary
print(tup)
print(lis)
print(dic)
print(min(tup))
print(max(tup))
print(abs(tup[0]))
print(sum(lis))


print("######################## Other Useful List Functions #############################")
mult11 = [55,44,33,22,11]
if all([(i%11 == 0) for i in mult11]):
    print("All numbers are divisible by 11")
if any([i % 2 == 0 ] for i in mult11):
    print("No multiple of 11 is even")
for v in enumerate(mult11):
    print(v)
a = enumerate(mult11)
print(a)



print("######################## Text Analyzer #############################")
#myFile = open("myLife.txt", "r")
#print(myFile.read())
#myFile.close()

def count_char(text,char):
    count = 0
    for c in text:
        if c==char:
            count+=1
    return count


with open("myLife.txt", "r") as f:
    text = f.read()
print(text)
print(count_char(text,"m"))

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text.lower(),char) / len(text)
    print("{0} - {1}%".format(char,round(perc,2)))


###########0 , 1, 2, 3
numbers = (55,44,33,22)
print(max( min(numbers[:2]) , abs(-42) ))



