import tkinter as tk
from tkinter import Scrollbar,filedialog,messagebox
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image

#For make results page
class page3(ctk.CTkFrame):   
    def __init__(self, root, controller):
        self.numOfCities = 0
        self.fromCity = 0
        self.toCity = 0
        self.startingCity = ""
        self.destination = ""
        self.next = []
        self.table = []
        self.cities = []
        ctk.CTkFrame.__init__(self, root)
        self.controller = controller
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        #design shape in form
        self.canvas = tk.Canvas(self, width=10000, height=2000, scrollregion=(0, 0, 10000,500),highlightthickness=0)

        h_scro = ctk.CTkScrollbar(self,width=800,orientation="vertical", command=self.canvas.xview)
        h_scro.place(x=520, y=970)
        self.canvas.configure(xscrollcommand=h_scro.set)
       

        frame=ctk.CTkFrame(self.canvas, width=10000, height=2000)   
        
        main_label = ctk.CTkLabel(frame, text="Results Page",font=("Times", 30, "bold")) 

        numOfCities_label = ctk.CTkLabel(frame, text="# of Cities:",font=("Times", 17, "bold")) 
        self.numOfCities_label2= ctk.CTkLabel(frame, text="",font=("Times", 20, "bold")) 
        
        start_label = ctk.CTkLabel(frame, text="Start City:",font=("Times", 17, "bold")) 
        self.start_label2= ctk.CTkLabel(frame, text="",font=("Times", 20, "bold"))

        end_label = ctk.CTkLabel(frame, text="End City:",font=("Times", 17, "bold")) 
        self.end_label2= ctk.CTkLabel(frame, text="",font=("Times", 20, "bold"))         

        solution_label = ctk.CTkLabel(frame, text="Best Solution :",font=("Times", 17, "bold")) 
        self.solution_label2= ctk.CTkLabel(frame, text="",font=("Times", 20, "bold")) 
        
        cost_label = ctk.CTkLabel(frame, text="Cost :",font=("Times", 17, "bold")) 
        self.cost_label2= ctk.CTkLabel(frame, text="",font=("Times", 20, "bold"))
        
        dp_label = ctk.CTkLabel(frame, text="DP Table :",font=("Times", 17, "bold")) 
        self.text_box = ctk.CTkTextbox(frame, wrap=tk.WORD,width=600,height=275,border_width=4, corner_radius=10,) 
        dpButton = ctk.CTkButton(frame,text="View clearly",command=lambda:self.controller("dpTable",self.cities,self.table,self.next,self.fromCity,self.toCity))
        
        self.img5 = ctk.CTkImage(Image.open("img/back.png"),size=(30,30)) 
        button = ctk.CTkButton(frame,text="Back",cursor='hand2',command=lambda:self.controller("Page2"),image=self.img5, compound="left",corner_radius=10,font=ctk.CTkFont(size=15, weight="bold"))
        
    #place entity in page
        button.place(x=20,y=20)
        main_label.place(x=710,y=20)
        
        numOfCities_label.place(x=520,y=120)
        self.numOfCities_label2.place(x=620,y=120)
        
        start_label.place(x=830,y=120)
        self.start_label2.place(x=930,y=120)

        end_label.place(x=830,y=170)
        self.end_label2.place(x=930,y=170)

        solution_label.place(x=630,y=220)
        self.solution_label2.place(x=750,y=220)

        cost_label.place(x=630,y=270)
        self.cost_label2.place(x=700,y=270)

        dp_label.place(x=630,y=330)
        dpButton.place(x=750,y=330)
        self.text_box.place(x=710,y=390)


        self.canvas.create_window((0, 0), window=frame,anchor="nw")
        self.canvas.pack()

    # Method to get data from page2 "v1, v2" and display it
    def get_data(self, num_of_cities, start_city, end_city, table,next,path,cities,fromCity,toCity):
        self.numOfCities_label2.configure(text=f"{num_of_cities}" , text_color = "GREEN")  # Update the label with the number of cities
        self.start_label2.configure(text=start_city ,text_color = "GREEN")  # Update the label with the start city
        self.end_label2.configure(text=end_city, text_color = "GREEN")  # Update the label with the end city
        self.solution_label2.configure(text=path, text_color = "GREEN")  # Update the label with the end city
        self.cost_label2.configure(text=table[0][num_of_cities-1], text_color = "GREEN")  # Update the label with the end city
        table_text = ""
        self.next = table
        self.table = next
        self.cities = cities
        self.fromCity = fromCity
        self.toCity = toCity
        

        if table:    
            for i, row in enumerate(table):
                if i == 0:
                    table_text += f"{'   '}{'    '.join(map(str, row))}\n"
                else :
                    table_text += f"{'   '}{'    '.join(map(str, row))}\n"
        
        # Display the table in the text_box
        self.text_box.delete("1.0", tk.END)  # Clear existing text
        self.text_box.insert(tk.END, table_text)


