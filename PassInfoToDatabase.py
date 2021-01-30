from UTIL import *
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import sqlite3
from contextlib import *
from ToyClass import *

database = "Toys Database.db"

ToysTbl="ToysTbl"
ImageTbl="ImgTbl"

ToysTblFields="'Toy Name' TEXT, 'Toy Price' REAL, 'Toy Stock' INTEGER, 'Category' TEXT, 'Reviews' TEXT"
ImageTblFields="'Toy Image' TEXT"



createDatabase(database)

createTable(database,ToysTbl,ToysTblFields)
createTable(database,ImageTbl, ImageTblFields)


for i in range(100):
    toy = toys(f"'toy{i}'", "basketball ball.jpg", 20.7, 20, "'Ball'")
    print(toy.getInfo())
    writeImageToDatabase(database, ImageTbl,"Toy Image", toy.getImage())
    writeToTableAllFields(database, ToysTbl, f"{toy.getName()},{toy.getPrice()},{toy.getStock()}, {toy.getCategory()}, 'Great toy lasts for a very long time'")








root=Tk()







#secondFrame=AddScrollBar(root)

#button=Button(secondFrame, text="skldjfa", command=lambda: getImageInfo(secondFrame, database, ImageTbl))
#button.grid(row=1, column=1)

root.mainloop()



