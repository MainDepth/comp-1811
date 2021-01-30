import sqlite3
from contextlib import *
from  ToyClass import *
from tkinter import  *
from tkinter import ttk
from PIL import Image,ImageTk

def createDatabase(database):
    with closing(sqlite3.connect(database=database)):
      return database

def createTable(database, tableName, Fields):
    with closing(sqlite3.connect(database=database)) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tableName} ({Fields}) """)



def writeToTableAllFields(database, table, content):
    with closing(sqlite3.connect(database=database)) as connection:
        with closing(connection.cursor()) as cursor:
            sqlQuery=f"""INSERT INTO {table} VALUES ({content})"""
            cursor.execute(sqlQuery)
        connection.commit()

def readAllFromTable(database,table):
    with closing(sqlite3.connect(database=database)) as connection:
        with closing(connection.cursor()) as cursor:
            sqlQuery=f"SELECT * FROM {table}"
            data=cursor.execute(sqlQuery).fetchall()
            return data

def convertDataToBlobData(filePath):
    with open(filePath,"rb") as BinaryReader:
        BlobData=BinaryReader.read()
    return BlobData



def BlobToStandard(filepath, data):
    with open(filepath, "wb") as writer:
       standardData= writer.write(data)
       return standardData


def writeImageToDatabase (database, table, Field,ToyImageFile):
    with closing(sqlite3.connect(database)) as connection:
        with closing(connection.cursor()) as cursor:
            sqlQuery=f"""INSERT INTO {table} ([{Field}]) VALUES (?)"""
            image=f"Images/{ToyImageFile}"
            dataTuple = image
            cursor.execute(sqlQuery,[dataTuple])

        connection.commit()



def AddScrollBar(master):
    # create Main frame
    MainFrame=Frame(master)
    MainFrame.pack(fill=BOTH, expand=1)

    # create canvas
    scrollCanvas=Canvas(MainFrame)
    scrollCanvas.pack(side=LEFT, fill=BOTH, expand=1)

    # add scroll bar
    myScrossBar=ttk.Scrollbar(MainFrame,orient=VERTICAL, command=scrollCanvas.yview)
    myScrossBar.pack(side=RIGHT, fill=Y)

    # configure the canvas
    scrollCanvas.configure(yscrollcommand=myScrossBar.set)
    scrollCanvas.bind('<Configure>',lambda e: scrollCanvas.configure(scrollregion=scrollCanvas.bbox("all")))

    # create another frame inside the canvas
    secondFrame=Frame(scrollCanvas)

    # add that new frame to a window in the canvas
    scrollCanvas.create_window((0,0),window=secondFrame, anchor="nw")
    return secondFrame


def getImageInfo(master,database, table):
    with closing(sqlite3.connect(database)) as connnection:
        with closing(connnection.cursor()) as cursor:
            sqlQuery=f"""SELECT * FROM {table}"""
            data=cursor.execute(sqlQuery).fetchall()
            print(data)

            i=0
            for rows in data:
                for j in range(len(rows)):
                    myImg=ImageTk.PhotoImage(Image.open(rows[j]))
                    imgLbl=Label(master, image=myImg)
                    imgLbl.saved_image=myImg
                    imgLbl.grid(row=i, column=j)
                i+=1


def showDatabaseContent(master,database, table,width):
    with closing(sqlite3.connect(database=f"{database}")) as connection:
        with closing(connection.cursor()) as cursor:
            record = cursor.execute(f'''SELECT * FROM {table} ''')
            i = 0
            for items in record:
                for j in range(len(items)):
                    TextField = Entry(master, width=width, fg="black")
                    TextField.grid(row=i, column=3 + j)
                    TextField.insert(END, items[j])
                    TextField.configure(state="readonly")
                i += 1