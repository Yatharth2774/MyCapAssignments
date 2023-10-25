#write a Python program which accepts the radius of a circle from the user and computes area.
import math
radius = float(input("Enter  radius of circle : "))
PI = math.pi

area = PI*radius*radius

print("Area of circle with radius : ",radius, " is : ", area)


#write a Python program to accept a filename from the user and print the extension of that.
filename = input("Enter complete filename : ")
extension = (filename.split(".")[-1]).lower() #takes last element of the list i.e. the extension part onnly
if extension == 'c' :
    print("The extension of the file is : C")
elif extension == "py":
    print("The extension of the file is : Python")
elif extension == "cpp":
    print("The extension of the file is : C++")
elif extension == "java":
    print("The extension of the file is : Java")
else:
    print("Extension Unknown!!!")
