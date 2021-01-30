from UTIL import *
import sqlite3
from ToyClass import *
from tkinter import *

class GUI(toys):
    database = "Toys Database.db"
    ToysTable="ToysTbl"
    ImageTable="ImgTbl"

    def __init__(self,master):
        self.categoryVariable=StringVar()
        master.title("CustomerFeatures")
        master.configure(bg="#242424")
        
        # create a main frame inside the scroll wheel frame allows the user to scroll through objects
        # all widgets will be in this frame
        MainFrame=AddScrollBar(master)

        self.showWidgets(MainFrame)

    def showWidgets(self, master):
        # frame to store all input aspects of the application
        InputFrame=Frame(master)
        InputFrame.configure(padx=2)
        InputFrame.grid(row=0, column=9)


        # shows all database content in a table format
        showDatabaseContent(master=master, database=self.database, table=self.ToysTable, width=25)
        getImageInfo(master,self.database, self.ImageTable)

        # creates button 
        self.button = Button(InputFrame, text="Search By Category", command=lambda: self.searchCategory(InputFrame,self.database, self.ToysTable))
        self.button.grid(row=0, column=1)

        # SEARCH BY NAME
        # creates name entry Field
        self.nameTxtBox=Entry(InputFrame)
        self.nameTxtBox.grid(row=1,column=1)

        # name EntryField Label
        nameEntryLbl=Label(InputFrame, text="Enter Name Of toy")
        nameEntryLbl.grid(row=1,column=0)

        # name Entry Button
        nameEntryBtn=Button(InputFrame,text="Search", command=lambda: self.searchByName(InputFrame, self.database, self.ToysTable,"Toy Name"))
        nameEntryBtn.grid(row=1, column=2)


        # Select by Category
        # Drop down menu
        categories=["Wooden", "Metallic", "Soft Toy", "Mechanic", "Ball"]
        self.categoryVariable.set("Categories")
        CategoryDropDownMenu=OptionMenu(InputFrame,self.categoryVariable,*categories)
        CategoryDropDownMenu.grid(row=0, column=0)




    def searchCategory(self,master,database, table):
        categoryWindow=self.createCategoryDisplayWindow(master)

        # finds and displays the content based on category the user input
        with closing(sqlite3.connect(database)) as connection:
            with closing(connection.cursor()) as cursor:
                sqlQuery=f"""SELECT * FROM {table} WHERE [Category] LIKE '%'||?||'%' """
                sqlParameter=self.categoryVariable.get()
                records=cursor.execute(sqlQuery,[sqlParameter]).fetchall()

                i=0
                for items in records:
                    for j in range (len(items)):
                       cell=Entry(categoryWindow,width=25)
                       cell.insert(END, items[j])
                       cell.configure(state="readonly")
                       cell.grid(row=i, column=j)
                    i+=1


    def searchByName(self, master,database,table,field):
        resultsWindow=self.createCategoryDisplayWindow(master)
        #finds the content based on the user input
        with closing(sqlite3.connect(database)) as connection:
            with closing(connection.cursor()) as cursor:
                userInput=self.nameTxtBox.get();
                sqlQuery=f"""SELECT * FROM {table} WHERE [{field}] LIKE '%'||?||'%'"""
                parameters=[userInput]

                records=cursor.execute(sqlQuery,parameters).fetchall()

                i=0
                for items in records:
                    for j in range(len(items)):
                        cell=Entry(resultsWindow,width=25)
                        cell.insert(END,items[j])
                        cell.configure(state="readonly")
                        cell.grid(row=i, column=j)
                    i+=1

        return records



    def createCategoryDisplayWindow(self,master):
        newWindow=Toplevel(master=master)
        MainFrame=AddScrollBar(newWindow)
        return MainFrame


root=Tk()
gui=GUI(root)
root.mainloop()
