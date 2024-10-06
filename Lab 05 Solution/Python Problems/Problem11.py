def SearchStudent(studentslist,name):
    Isfind=False
    for i in range(len(studentslist)):
        if(studentslist[i]==name):
            Isfind=True
            print(f"{name} found in students list at index {i}")
    if(not Isfind):
        print("No such student found in list.")

#Driver
studentslist=["Amir","Ashir","Ali","Abdullah","AHmad","Umer","Usman"]
SearchStudent(studentslist,"Ashir")
SearchStudent(studentslist,"AbuBakar")