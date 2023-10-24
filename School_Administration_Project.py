import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(['Roll No.','Name','Contact No.','E-mail Id'])
            
        writer.writerow(info_list)

def take_input():
    student_details = []  # array that stores student details
    student_details.append(int(input("Enter Roll number : ")))
    student_details.append(input("Enter Name : "))
    student_details.append(input("Enter Contact Number : "))
    student_details.append(input("Enter Email-Id : "))
    return student_details

if __name__ == '__main__':
    
    num = int(input("Enter Number of records you want to enter : "))

    record = []      # main record that stores lists of student details

    for i in range(num):
        while True:
            print("Enter details for Student ", i+1, " : ")
            student_details = take_input()
            
            print("The following information will be added to the record : ")
            print(student_details)
            check = input("Are these details correct (y/n) : ")
            if check == 'y':
                record.append(student_details)
                write_into_csv(student_details)
                break
            else:
                student_details = take_input()
                
    print("")
    
    print("********************************************************")
