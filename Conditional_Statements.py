age = 21 
if (age>=18):
    print("can vote and apply for license")


light ="green"
if (light == "red"):
    print("Stop")
elif (light == "green"):
    print("Go")
elif(light == "yellow"):
    print("Wait")


light ="pink"
if (light == "red"):
    print("Stop")
elif (light == "green"):
    print("Go")
elif(light == "yellow"):
    print("Wait")
else:
    print("Light is Broken ")


age = 21
if (age>=18):
    print("can vote")
else:
    print("can't vote")


mark = int(input("enter student mark "))
if (mark >= 90):
    grade = "A"
elif (mark >= 80 and mark < 90):
    grade = "B"
elif (mark >= 70 and mark < 80):
    grade = "C"
else :
    grade = "D"
print("grade of the student ->", grade)