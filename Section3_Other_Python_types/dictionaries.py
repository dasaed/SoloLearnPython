print("Dictionaries are data structures used to map arbitrary keys to values")
ages = {"dave": 24, "Mary": 42, "John": 58}
print(ages["dave"])
print(ages["Mary"])

colors = {
    "red": [255,0,0],
    "green": [0,255,0],
    "blue": [0,0,255]
}
try:
    print(rgb["yellow"])
except:
    print("Yellow is not one of the RGB Colors")

emptyDictionary = {}
print(emptyDictionary)

colors["yellow"] = [255,255,0]
colors["white"] = [255,255,255]
colors["black"] = [255,255,255]
print(colors)
colors["black"] = [0,0,0]
print("orange" in colors)
print("black" in colors)
print("white" not in colors)
print("Use the get method to get elements from a dictionary, and in case an element doesn't exist, it will return a \"None\", instead of an error")
print(colors.get("orange","Orange is not in this dictionary"))
print(colors.get("white"))








