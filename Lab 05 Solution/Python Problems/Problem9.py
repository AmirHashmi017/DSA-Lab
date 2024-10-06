def AddStudent(studentslist, name):
        studentslist.append(name)
        print(f"{name} is added to the class.")

def RemoveStudent(studentslist, name):
    if name in studentslist:
            studentslist.remove(name)
            print(f"{name} is removed from the class.")
    else:
            print(f"{name} is not in the class list.")

def DisplayStudents(studentslist):
    if studentslist:
            print("List of students in the class:")
            for student in studentslist:
                print(student)
    else:
            print("No students in the class yet.")

#Driver
studentlist=[]
AddStudent(studentlist,"Amir")
AddStudent(studentlist,"Ashir")
AddStudent(studentlist,"Ali")
DisplayStudents(studentlist)
RemoveStudent(studentlist,"Ashir")
DisplayStudents(studentlist)


