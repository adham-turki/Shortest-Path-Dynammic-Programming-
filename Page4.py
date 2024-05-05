import tkinter as tk
from tkinter import Scrollbar
import customtkinter as ctk
from PIL import Image

#For make results page
class page4(ctk.CTkFrame):   
    def __init__(self, root, controller):
        ctk.CTkFrame.__init__(self, root)
        self.controller = controller
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        #design shape in form
        self.canvas = tk.Canvas(self, width=10000, height=2000, scrollregion=(0, 0, 10000,500),highlightthickness=0)

        h_scro = ctk.CTkScrollbar(self,width=800,orientation="horizontal", command=self.canvas.xview)
        h_scro.place(x=520, y=970)
        self.canvas.configure(xscrollcommand=h_scro.set)

        frame=ctk.CTkFrame(self.canvas, width=10000, height=2000)   
        
        label = ctk.CTkLabel(frame, text="Results Page",font=("Times", 30, "bold")) 

        numOfCities_label = ctk.CTkLabel(frame, text="# of Cities:",font=("Times", 17, "bold")) 
        self.numOfCities_label2= ctk.CTkLabel(frame, text="",font=("Times", 22, "bold")) 
        start_label = ctk.CTkLabel(frame, text="Start City:",font=("Times", 17, "bold")) 
        self.start_label2= ctk.CTkLabel(frame, text="",font=("Times", 22, "bold"))

        end_label = ctk.CTkLabel(frame, text="End City:",font=("Times", 17, "bold")) 
        self.end_label2= ctk.CTkLabel(frame, text="",font=("Times", 22, "bold"))         

        numOfS_label = ctk.CTkLabel(frame, text="Number of Solution :",font=("Times", 17, "bold")) 
        self.numOfS_label2= ctk.CTkLabel(frame, text="",font=("Times", 22, "bold")) 
        
        
        
        
        self.img5 = ctk.CTkImage(Image.open("img/back.png"),size=(30,30)) 
        button = ctk.CTkButton(frame,text="Back",cursor='hand2',command=lambda:self.controller("Page2"),image=self.img5, compound="left",corner_radius=10,font=ctk.CTkFont(size=15, weight="bold"))
        
    #place entity in page
        button.place(x=20,y=20)
        label.place(x=710,y=20)
        
        numOfCities_label.place(x=520,y=120)
        self.numOfCities_label2.place(x=705,y=120)
        
        start_label.place(x=830,y=120)
        self.start_label2.place(x=970,y=120)

        end_label.place(x=830,y=170)
        self.end_label2.place(x=970,y=170)

        numOfS_label.place(x=520,y=220)
        self.numOfS_label2.place(x=705,y=220)

        self.canvas.create_window((0, 0), window=frame,anchor="nw")
        self.canvas.pack()

    #method to get data form page2 "n,order" and display it
    def get_data(self,numOFCities, startingCity, destination, alt_paths, alt_costs):
        self.numOfCities_label2.configure(text=f"{numOFCities}" , text_color = "GREEN")  # Update the label with the number of cities
        self.start_label2.configure(text=startingCity ,text_color = "GREEN")  # Update the label with the start city
        self.end_label2.configure(text=destination, text_color = "GREEN")  # Update the label with the end city
        text =""
        for i in range(len(alt_paths)) :
            text = text + str(alt_paths[i]) + " : " + str(alt_costs[i]) + "\n" 
        self.numOfS_label2.configure(text=text, text_color = "GREEN")  # Update the label with the end city
   
