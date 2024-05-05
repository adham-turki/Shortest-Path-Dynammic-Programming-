import tkinter as tk
import customtkinter as ctk
from PIL import Image
from Page2 import page2
from Page3 import page3
from dpTable import dpTable
from Page4 import page4

# For making the Welcome page
class Main(ctk.CTkFrame):
    def __init__(self, root, controller):
        ctk.CTkFrame.__init__(self, root)
        self.controller = controller
        
        # Welcome labels
        label = ctk.CTkLabel(self, text="Welcome to our application ", font=("Times", 40, "bold"))
        label.pack(side="top", pady=20)
        label = ctk.CTkLabel(self, text=" ' Optimal Strategy for Minimum cost from city to city using Dynamic Programming ' ", font=("Times", 30, "bold"))
        label.pack(side="top", pady=20)
      


        self.img = tk.PhotoImage(file='img/Dynamic.png')
        my_image_label = tk.Label(self, image=self.img, width=800, height=400)
        my_image_label.pack()

        self.img1 = ctk.CTkImage(Image.open("img/arrow.png"), size=(40, 40))
        # Button to enter the application
        button = ctk.CTkButton(self, text="Enter", cursor='hand2', image=self.img1, compound="left", corner_radius=10,
                                font=ctk.CTkFont(size=20, weight="bold"), width=220, height=40,
                                command=lambda: self.controller.show_page("Page2"))  
        button.pack(side="bottom", pady=5, expand=True)

# to connect pages and move between them
class MainApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Programming")
        self.root.geometry("1600x2000")
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.pages = {}

        # Creating and adding pages
        self.pages["Page1"] = Main(self.root, self)
        self.pages["Page2"] = page2(self.root, self.show_page)
        self.pages["Page3"] = page3(self.root, self.show_page)
        self.pages["dpTable"] = dpTable(self.root, self.show_page)
        self.pages["Page4"] = page4(self.root, self.show_page)



        
        self.show_page("Page1")

    def show_page(self, page_name,*args):
        for page in self.pages.values():
            page.pack_forget()
           
        page=self.pages[page_name]
        page.pack(expand=True,fill="both") #let the content fill the page

        
        if page_name == "dpTable" : page.printDP(*args)  
        if page_name == "Page3" and len(args) == 9 : page.get_data(*args)  
        if page_name == "Page4" and len(args) == 5 : page.get_data(*args)  

if __name__ == "__main__":
    root = ctk.CTk()
    app = MainApp(root)
    root.after(0, lambda:root.state('zoomed'))
    root.mainloop()
