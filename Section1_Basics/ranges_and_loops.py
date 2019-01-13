
### ranges
aNum = 27
print('Hello '+str(aNum))
#The range function
nums = range(3,301,3) # range (from 3, to 300, in increments of 3)
i=0
while (nums[i] !=18):
        print(nums[i])
        i+=1

nums = list(range(5,8))

print(nums)
print(len(nums))

### Now we get to the for loops ###
sampleData = ["chevy", 'ford', 'toyota', 'dodge', 'honda']

print("For in python sort of works like a foreach in other languages")
for car in sampleData:
    print(car)
print("Using range to cycle through a for loop")
for i in range(4):
    print(sampleData[i])