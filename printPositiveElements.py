myList = []
n = int(input("Enter size of List : "))
for i in range(n):
    element = int(input("Enter element : "))
    myList.append(element)
print("Your List is : ",myList)
print("All positive elements are : ")
for i in range(n):
    if(myList[i] >= 0):
        print(myList[i])
