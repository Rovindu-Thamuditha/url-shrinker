import shortner
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        #Window Configurations
        self.title("URL Shrinker")
        self.geometry("370x150")
        self.resizable(height=False, width=False)

        #StrVariables
        self.long_url = tk.StringVar(self)
        self.selected_provider = tk.StringVar(self)
        self.selected_provider.set("cuttly") #Default Option

        host_providers = ["cuttly", "adfocus", "shrinkearn", "v2links", "bitly"]

        #Setting up frames
        self.main_frame = tk.Frame()
        self.main_frame.pack()


        self.entry_label = tk.Label(self.main_frame, text="Enter your long url:", font=('Roboto', 12))
        self.entry_label.grid(row=0, column=0, padx=0, pady=12)

        #Host Provider
        self.host_menu = tk.OptionMenu(self.main_frame, self.selected_provider, *host_providers)
        self.host_menu.grid(row=1, column=0, padx=0, pady=3)

        #URL Input Box
        self.long_url_in = tk.Entry(self.main_frame, width=40, textvariable=self.long_url, font=('Roboto', 12))
        #self.long_url_in.bind("<Button-1>", self.copy_url)
        self.long_url_in.grid(row=2, column=0, padx=0, pady=6)

        #Shrink Button
        self.shrinkButton = tk.Button(self.main_frame, text="Shrink!", command=self.shrink_url, font=('Roboto', 11))
        self.shrinkButton.bind("Enter", self.press_enter)
        self.shrinkButton.grid(row=3, column=0, padx=0, pady=5)
        
        '''
        #Shortened URL
        self.shortened_url = tk.Label(self.main_frame, text='Shortened URL :')
        self.shortened_url.grid(row=3, column=0, padx=0, pady=0)
        '''
        

    def get_url(self):
        self.long_url_str = self.long_url.get()
        self.provider = self.selected_provider.get()
        self.shrinked_url = shortner.select_host(host=self.provider, url=self.long_url_str)
        return self.shrinked_url

    def shrink_url(self):
        self.shrink_url = self.get_url()
        self.long_url_in.delete(0, tk.END)
        self.long_url_in.insert(0, self.shrinked_url)
        window.clipboard_clear()
        window.clipboard_append(self.shrinked_url)
        messagebox.showinfo("URL Copied", "URL has been copied to the clipboard.")

    '''def copy_url(self, event):
        self.long_url_str = self.long_url.get()
        self.shrink_url = self.get_url()'''
    
    def press_enter(self, event):
        self.shrinkButton.invoke()
        

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()