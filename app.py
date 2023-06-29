import customtkinter
from customtkinter import CTkLabel, CTkButton, CTkFrame, CTkOptionMenu, CTkEntry

#Color Palette

label_color = "#E8F5E9"
background_color = "#263238"
btn_fg_color = "#FFFFFF"
btn_bg_color = "#43A047"
btn_hover_color = "#81C784"
btn_border_color = "#43A047"
dropdown_color = "#37474F"
dropdown_selected_color = "#4CAF50"
dropdown_fg_color = "#FFFFFF"
dropdown_text_color = "#FFFFFF"
dropdown_hover_color = "#546E7A"


#######

light_yellow =  "#f8ffe5"
spring_green =  "#00e77e"
mauve =  "#dabfff"
air_force_blue =  "#537d8d"
dark_purple =  ""
lemon_chiffon = "#FAF0CA"



customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

providers = ['Cuttly', 'ShrinkMe', 'ShrinkEarn', 'AdFocus', 'V2Links']
class MainFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=15) #fg_color=background_color 
        


        # StringVar List
        self.provider = customtkinter.StringVar(value="Cuttly")
        self.link = customtkinter.StringVar(value="")

        self.titleLabel = CTkLabel(self, text="Linkify", font=('Montserrat', 32), pady=15) #text_color=label_color)
        self.titleLabel.pack()

        #----------PADDING----------#

        self.container_label_1 = CTkLabel(self, text="", height=20)
        self.container_label_1.pack()

        #----------PADDING----------#

        #Provider Selector

        self.host_selecter = CTkOptionMenu(
            self,
            values=providers,
            variable=self.provider,
            #dropdown_hover_color=dropdown_hover_color,
            #dropdown_fg_color=dropdown_color,
            #dropdown_text_color=dropdown_text_color,
            #button_color=btn_hover_color,
            #button_hover_color=air_force_blue,
            font=('Roboto', 18),
            dropdown_font=('Roboto', 13),
            height=32
        )
        self.host_selecter.pack()

        #----------PADDING----------#

        self.container_label_2 = CTkLabel(self, text="", height=35)
        self.container_label_2.pack()

        #----------PADDING----------#

        #URL Input Field

        self.url_entry = CTkEntry(
            self,
            width=300,
            corner_radius=10,
            #border_color=btn_border_color,
            placeholder_text="https://google.com",
            textvariable=self.link,
            font=('Sans serif', 15)
        )
        self.url_entry.pack()

        #----------PADDING----------#

        self.container_label_3 = CTkLabel(self, text="", height=25)
        self.container_label_3.pack()

        #----------PADDING----------#

        #Shrink Button and Copy Button

        self.button_container = CTkFrame(self)
        self.button_container.pack()

        self.shrink_btn = CTkButton(
            self.button_container,
            text="Shrink!",
            font=('Roboto', 20),
            #fg_color=btn_bg_color,
            #border_color="#ffffff",
            #hover_color=btn_hover_color,
            corner_radius=10
        )
        self.shrink_btn.grid(row=0, column=0, padx=4) #Need to Work on columns and rows in pack!!

        self.copy_btn = CTkButton(
            self.button_container,
            text="Copy",
            font=('Roboto', 20),
            #fg_color=btn_bg_color,
            #border_color="#ffffff",
            #hover_color=btn_hover_color,
            corner_radius=10
        )
        self.copy_btn.grid(row=0, column=2, padx=4) #Need to Work on columns and rows in pack!!

        

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #Window Configurations
        
        self.title("Linkify URL Shrinker")
        self.geometry("350x400")
        self.resizable(width=False, height=False)
        self.iconbitmap("icon.ico")
        

        self.main_frame = MainFrame(master=self)
        self.main_frame.pack(fill="both", expand=True)

        
if __name__ == "__main__":
    app = App()
    app.mainloop()