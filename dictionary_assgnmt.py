str = input("Please Enter a String : ")

myDict = {}
for char in str:
    myDict[char] = myDict.get(char, 0) + 1

print(myDict)
