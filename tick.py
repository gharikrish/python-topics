def ticket():
    print("welcome to xyz metro")
    a = int(input("hi how many ticket you want : "))
    seat = 1
    for i in range(a):
        name = str(input("enter the name :   "))
        age = int(input("enter the age :  "))
        contact = int(input("please enter the mobile number : "))
        print("SEAT NO : ",seat)
        print("Name    : ",name)
        print("Age     : ",age )
        print("                    ")
        print("******************")
        print("                  ")
        seat = seat + 1
        
ticket()