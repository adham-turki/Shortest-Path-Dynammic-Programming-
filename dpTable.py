# dpTable.py
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image


class dpTable(ctk.CTkFrame):
    def __init__(self, root, controller):
        ctk.CTkFrame.__init__(self, root)
        self.controller = controller
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.frame=ctk.CTkFrame(self, width=2500, height=2500)
        # Create a custom style for the Treeview
        style = ttk.Style()
        style.configure("Treeview.Treeview", font=("Times",15) , background = "" )  
        
        self.img5 = ctk.CTkImage(Image.open("img/back.png"),size=(30,30)) 
        button = ctk.CTkButton(self.frame,text="Back",cursor='hand2',command=lambda:self.controller("Page3"),image=self.img5, compound="left",corner_radius=10,font=ctk.CTkFont(size=15, weight="bold"))
        
        self.label_table = ctk.CTkLabel(self.frame, text="", font=("Times", 24, "bold")) 

        self.tree_table = ttk.Treeview(self.frame, columns=(), show="headings",style="Treeview.Treeview"  )

        self.label_next = ctk.CTkLabel(self.frame, text="", font=("Times", 24, "bold")) 

        self.tree_next = ttk.Treeview(self.frame,height=20, columns=(), show="headings",style="Treeview.Treeview")
        
        button.place(x=20,y=20)
        self.label_next.place(x=600,y=20)
        self.tree_table.place(x=600,y=80)
        self.label_table.place(x=580,y=360)
        self.tree_next.place(x=600,y=520)
        self.frame.pack()

    def printDP(self, cities, table, next,fromCity,toCity):
        print(fromCity, toCity)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Times", 15,"bold"))
        self.label_table.configure(text="Dynamic Table:") 
        self.label_next.configure(text="Path Table:") 

        self.tree_table.delete(*self.tree_table.get_children())
        self.tree_next.delete(*self.tree_next.get_children())

        # Insert columns for table and next
        # Set column headings for table
        newCities = []
        newCities.append("City")
        for i , city in enumerate(cities) : 
            if i>= fromCity and i<= toCity:
                newCities.append(city)
                
        self.tree_table["columns"] = newCities
        for i,city in enumerate(newCities):
            self.tree_table.heading(city, text=city )
            self.tree_table.column(city, width=70,anchor="center")  

        # Set column headings for next
        self.tree_next["columns"] = newCities
        for i,city in enumerate(newCities):
            self.tree_next.heading(city, text=city)
            self.tree_next.column(city, width=70,anchor="center")  
        newCities.remove("City")

        # Insert rows for table
        for i, (city, row) in enumerate(zip(newCities, table)):
            self.tree_table.insert("", "end", values=[city] + row, iid=f"row_{i}")

    # Insert rows for next
        for i, (city, row) in enumerate(zip(newCities, next)):
            self.tree_next.insert("", "end", values=[city] + row, iid=f"row_{i}")
