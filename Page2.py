import tkinter as tk 
from tkinter import  filedialog
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image
from tkinter import ttk
from Algo import apply_algorithm , print_path,alt_path




#For make Main page
class page2(ctk.CTkFrame):
    def __init__(self, root, controller):
        self.numOFCities = 0
        self.fromCity = 0
        self.toCity = 0
        self.startingCity = ""
        self.destination = ""
        self.table = []
        self.alt_table = []
        self.next = []
        self.d = 0
        self.input_data = ""
        self.cities = []
        self.stages = []
        self.stage_copy = []
        self.main_path  = ""
        self.alt_paths= []
        self.alt_costs = []
        self.error = False
        ctk.CTkFrame.__init__(self, root)
        self.controller = controller
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        #design shape in form
        frame=ctk.CTkFrame(self, width=2000, height=2000)
        
        label = ctk.CTkLabel(frame,text="Home",font=("Times", 30, "bold"))
        
        label1 = ctk.CTkLabel(frame, text="# of Cities:",font=("Arial", 16, "bold"))
        self.num_Cities_entry1 = ctk.CTkEntry(frame,placeholder_text="eg.3", width=200,border_width=4, corner_radius=20,validate="key",font=("Arial",16))
        
        self.img1 = ctk.CTkImage(Image.open("img/writing.png"),size=(30,30))
        execute_Btn=ctk.CTkButton(frame,text="Execute",command = self.run,cursor='hand2',image=self.img1, compound="left",corner_radius=10,font=ctk.CTkFont(size=15, weight="bold"))
        
        self.img2 = ctk.CTkImage(Image.open("img/folder.png"),size=(30,30))
        file_Btn=ctk.CTkButton(frame,text="File",command= self.read_from_file,cursor='hand2',image=self.img2, compound="left",corner_radius=10,font=ctk.CTkFont(size=15, weight="bold"))
        
        self.img3 = ctk.CTkImage(Image.open("img/dices.png"),size=(30,30))
        alternative_Btn=ctk.CTkButton(frame,text="Alternative",command= self.goto_alternative,cursor='hand2',image=self.img3, compound="left",corner_radius=10,font=ctk.CTkFont(size=15, weight="bold"))

        label2 = ctk.CTkLabel(frame, text="Start City:",font=("Arial", 16, "bold"))
        label3 = ctk.CTkLabel(frame, text="End City:",font=("Arial", 16, "bold"))
       
        # Create the comboboxes with the configured style
        self.start_combo = ttk.Combobox(frame, width=15, state="readonly", font=("Arial", 16))
        self.end_combo = ttk.Combobox(frame, width=15, state="readonly", font=("Arial", 16))
        

        combostyle = ttk.Style()
        combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': 'none',
                                       'fieldbackground': 'darkgrey',
                                       'background': 'darkgrey',
                                       'selectforeground':'black'
                                       }}}
                         )
        combostyle.theme_use('combostyle') 

        

        self.img4 = ctk.CTkImage(Image.open("img/map.png"),size=(30,30))
        self.result_button = ctk.CTkButton(frame,text="Result",command=self.goto_result,cursor='hand2',image=self.img4, compound="left",corner_radius=10,font=ctk.CTkFont(size=15, weight="bold"))

        self.img5 = ctk.CTkImage(Image.open("img/back.png"),size=(30,30)) 

        label4 = ctk.CTkLabel(frame, text="List of adjacent cities : ",font=("Arial", 16, "bold"))
        self.text_area = ctk.CTkTextbox(frame, width=500, height=300, border_width=4, corner_radius=10, font=("Arial", 14))

        self.img = tk.PhotoImage(file='img/graph.png')
        image_label = tk.Label(frame,image=self.img,width=680,height=540)

        self.infoLabel = ctk.CTkLabel(frame, text="",text_color="RED",font=("Arial", 16, "bold"))

        #place entity in page
        label.place(x=758,y=20)
        label1.place(x=525,y=120)
        self.num_Cities_entry1.place(x=790,y=120)
        execute_Btn.place(x=1040,y=115)
        label2.place(x=525,y=220)
        self.start_combo.place(x=990,y=280)
        label3.place(x=525,y=270)
        self.end_combo.place(x=990,y=340)
        file_Btn.place(x=1040,y=215)
        self.result_button.place(x=1040,y=300)
        alternative_Btn.place(x=1200,y=300)
        image_label.place(x=250,y=440)
        label4.place(x=800,y=370)
        self.text_area.place(x=800, y=400)  

        self.infoLabel.place(x=990,y=370)

        frame.pack()

    #go to the result page
    def goto_result(self):
        if(self.error == False) :
            try:
                self.controller("Page3", self.numOFCities, self.startingCity, self.destination,self.table,self.next,self.main_path,self.cities ,self.d,self.get_index(self.end_combo.get()))
            except Exception as e:
                # Handle error
                self.infoLabel.configure(text=e,text_color="RED")
                return

       
    # To read data order from file O(n log n)
    def read_from_file(self):
        # Open file dialog to select the file
        file_path = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

        if file_path:
            try:
                # Open the selected file for reading
                with open(file_path, 'r') as file:
                    # Read the data from the file
                    self.input_data = ""
                    data= file.read()

                      # Extract the number of cities, start city, and end city from the data
                    lines = data.strip().split('\n')
                    num_cities = int(lines[0])
                    self.numOFCities = int(lines[0])
                    start_city, end_city = map(str.strip, lines[1].split(','))#extract the start and end cities from line 2
                    # Clear initial values of combo boxes
                    self.start_combo['values'] = []
                    self.end_combo['values'] = []
                    # Set the number of cities in the entry field
                    self.num_Cities_entry1.delete(0, tk.END)
                    self.num_Cities_entry1.insert(tk.END, num_cities)
                    self.cities = []  # Initialize the list of cities with "End"
                    # Fill the combo boxes with the cities
                    for line in lines[2:]:
                        self.input_data += line + "\n"
                        parts = line.split(',')
                        self.cities.append(parts[0].strip())  # Add the city to the list
                        

                    # Display the data in the text area
                    self.text_area.delete("1.0", tk.END)  # Clear existing text
                    self.text_area.insert(tk.END, self.input_data) # Insert the data into the text area
                    self.cities.append(end_city) 
                    self.start_combo['values'] = self.cities
                    self.end_combo['values'] = self.cities
                    

                    # Set initial values for the combo boxes
                    self.start_combo.set(start_city)
                    self.end_combo.set(end_city)
                    a, b, b, d, g, f, h, self.stages= apply_algorithm(self.start_combo.get().strip(),self.end_combo.get().strip(),self.cities,self.input_data)
                    self.stage_copy = self.stages 


                    self.infoLabel.configure(text="File loaded successfully!",text_color="GREEN")
            except Exception as e:
                self.infoLabel.configure(text=e,text_color="RED")  # Display error message if file reading fails
           
    
    def goto_alternative(self):
        if(self.error == False) :
            try:
                self.controller("Page4",self.numOFCities, self.startingCity, self.destination, self.alt_paths, self.alt_costs) 
            except Exception as e:
                # Handle error
                self.infoLabel.configure(text=e,text_color="RED")   
    def run(self)  :
        if(len(self.cities) != 0) :
            if(self.start_combo.get().strip() == self.end_combo.get().strip() or self.get_index(self.start_combo.get().strip()) > self.get_index(self.end_combo.get().strip())) :
                self.error = True
                self.infoLabel.configure(text="The Start City must be before the end city",text_color="RED")
            else:
                print(self.get_stage(self.start_combo.get().strip()), self.get_stage(self.end_combo.get().strip()))
                if (self.get_stage(self.start_combo.get().strip()) == self.get_stage(self.end_combo.get().strip())) :
                    self.error = True
                    self.infoLabel.configure(text="The Start and End City in the same stage",text_color="RED")
                else :
                    if(int(self.num_Cities_entry1.get()) != len(self.cities)) : 
                        self.error = True
                        self.infoLabel.configure(text="The number of cities is Wrong",text_color="RED")
                    else :
                        self.error = False
                        self.fromCity = 0
                        self.toCity = 0
                        self.startingCity = ""
                        self.destination = ""
                        self.table = []
                        self.next = []
                        self.stages = []
                        self.d = 0
                        self.last = 0
                        self.main_path  = ""
                        self.alt_paths= []
                        self.alt_costs = []
                        self.input_data = self.text_area.get("1.0", tk.END).strip()
                        self.fromCity, self.toCity, self.startingCity, self.destination, self.table, self.next, self.d, self.stages= apply_algorithm(self.start_combo.get().strip(),self.end_combo.get().strip(),self.cities,self.input_data)
                        for i, city in enumerate(self.cities):
                            if city == self.end_combo.get().strip():
                                self.last=i
                        self.last=self.last-self.d 
                        self.numOFCities = self.toCity- self.fromCity +1
                        self.main_path = print_path(self.next,self.toCity,self.fromCity,self.d,self.cities,self.end_combo.get(),self.start_combo.get(),self.next[0][self.last])
                        for i in range(3) :
                            path , cost = alt_path(self.stages,self.table,self.startingCity,self.destination,self.cities,self.d)
                            self.alt_costs.append(cost)
                            self.alt_paths.append(path)
                        # for i in range(len(self.alt_paths)): 
                        #     for j in range(len(self.alt_paths)) :
                        #         if self.alt_paths[i] == self.alt_paths[j] :
                        #             self.alt_paths.pop(i)
                        #             self.alt_costs.pop(i)
                    
                        print(self.table)
                        self.infoLabel.configure(text="Executed Successfuly",text_color="GREEN")                       
        else : 
            self.infoLabel.configure(text="please enter a file",text_color="red")                       

    def get_index(self, city_name):#O(n)
        for i, city in enumerate(self.cities):
            if city == city_name:
                return i
        return -1

    def get_stage(self, city_name) :
        if city_name == self.cities[0]  : 
            return -1
        if city_name == self.cities[len(self.cities)-1] :
            return -2
        for i in range (len(self.stage_copy)):
            for j in range (len(self.stage_copy[i])):
                if self.stage_copy[i][j] == city_name:
                    return i
        
    

