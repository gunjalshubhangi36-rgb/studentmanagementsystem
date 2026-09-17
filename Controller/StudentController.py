from Model.StudentModel import StudentStruct
from DataBase.dbconnection import collection


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
