from fastapi import APIRouter
from Controller.StudentController import CreateStudent 
from Model.StudentModel import StudentStruct
from Model.studentupdate import updateStruct
from DataBase.dbconnection import collection

router = APIRouter()



@router.post("/createStudent")
def CreateStudent(student:StudentStruct):
    sroll = student.roll
    sname = student.name
    sage = student.age
    smail = student.mail


    sinfo = {

        "roll" : sroll,
        "name" : sname,
        "age" : sage,
        "mail": smail
    }

    collection.insert_one(sinfo)

    return {"message":"student created"}


@router.get("/allstudents")
def GetStudent():
    alldata = list(collection.find({},{"_id":0}))
    return alldata


@router.put("/edit/{roll}")
def UpdateStudent(roll:int,student:updateStruct):
    alldata = list(collection.find({},{"_id":0}))

    updatedstudent = {}

    for i in alldata:
        if i["roll"]==roll:

            if student.name != None:
                updatedstudent["name"]=student.name

            if student.age != None:
                updatedstudent["age"] = student.age

            if student.mail != None:
                updatedstudent["mail"] = student.mail

            collection.update_one(
                {"roll":roll},
                {"$set":updatedstudent}
            )

            return {"message":"student Updated"}



@router.delete("/delet/{roll}")
def Deletstudent(roll:int):
    alldata = list(collection.find({},{"_id":0}))

    for i in alldata:
        if i["roll"]==roll:
            collection.delete_one({"roll":roll})
            return {"message":"student deleted"}
    



