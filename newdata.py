def filereding2(filename):
    with open(filename,"r")as f:
        data=json.load(f)
        val=data["student"]
        student=[]
        list1=[]
        for i in val:
            for j in i.keys():
                if j=="name":
                    student.append(i[j])
        list1.append(student)
        return list1
def filereding(filename):
    with open(filename,"r")as f:
        data=json.load(f)
        return data
def filewriting(filename,dic1):
    with open(filename,"w")as f:
        data=json.dumps(dic1)
        f=json.dump(dic1,f,indent=3)
import json
filereding_2=filereding2("student_data.json")

import random
list_student=[]
i=0
while i<len(filereding_2):
    if i==0:
        list_student.extend(filereding_2[i])
    i=i+1
j=1
list_n=[]
dict1={"student":[]}
while j<=2:
    bedNumbers=[1,2,3,4,5,6,7,8,9,10]
    for k in range(0,10):
        new_bed=random.choice(bedNumbers)
        bedNumbers.remove(new_bed)
        new_student=random.choice(list_student)
        list_student.remove(new_student)
        dict2={"name":new_student,"Bed":new_bed,"room":j}
        dict1["student"].append(dict2)
        filewriting_1=filewriting("new_data.json",dict1) 
    j+=1
filereding_2=filereding("new_data.json")
print(filereding_2)
