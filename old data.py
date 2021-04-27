import json
def filewriting(filename,dic1):
    with open(filename,"w")as f:
        data=json.dumps(dic1)
        f=json.dump(dic1,f,indent=3)
def filereding(filename):
    with open(filename,"r")as f:
        data=json.load(f)
        return data
student_name=input("enter student name---")
room_no=int(input("enter current room number----"))
bed_no=int(input("enter  current bed number---"))
dict1={"name":student_name,"room_no":room_no,"Bed":bed_no}
a=filereding("student_data.json")
print(a)
a["student"].append(dict1)
filewriting("student_data.json",a)


