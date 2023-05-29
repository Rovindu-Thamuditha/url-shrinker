import shortner
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        #Window Configurations
        self.title("URL Shrinker")
        self.geometry("372x150")
        self.resizable(height=False, width=False)

        #StrVariables
        self.long_url = tk.StringVar(self)
        self.long_url.set("")
        self.selected_provider = tk.StringVar(self)
        self.selected_provider.set("cuttly") #Default Option

        host_providers = ["cuttly", "adfocus", "shrinkearn", "v2links", "bitly"]

        #Setting up frames
        self.main_frame = tk.Frame()
        self.main_frame.pack()


        self.entry_label = tk.Label(self.main_frame, text="Enter your long url:", font=('Roboto', 12))
        self.entry_label.grid(row=0, column=0, padx=0, pady=11)

        #Host Provider
        self.host_menu = tk.OptionMenu(self.main_frame, self.selected_provider, *host_providers)
        self.host_menu.grid(row=1, column=0, padx=0, pady=0)

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
    

    def check_url(self, url):
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        return url

    def shrink_url(self):
        self.long_url_str = self.long_url.get() #getting the URL input
        
        if self.long_url_str == '':
            messagebox.showerror("Error", "Enter the URL that you want to shrink.")
            pass
        
        elif len(self.long_url_str) > 1:  
            self.url = self.check_url(self.long_url_str)
            self.provider = self.selected_provider.get() #getting the host input    
            if self.provider == 'cuttly':
                self.short_url, self.status = shortner.cuttly(self.url)
                if self.status == 7:
                    self.long_url_in.delete(0, tk.END)
                    self.long_url_in.insert(0, self.short_url)
                    window.clipboard_clear()
                    window.clipboard_append(self.short_url)
                    messagebox.showinfo("URL Copied", "URL has been copied to the clipboard.")
                    
                elif self.status == 5 or self.status == 2:
                    messagebox.showerror("Invalid Link", "The provided url is invalid")

                elif self.status == 1:
                    messagebox.showerror("Error", "The link has already been shortened")

                elif self.long_url_str == None:
                    messagebox.showwarning("Warning!", "Enter the url.")
                else:
                    messagebox.showerror("Error", "An error occured when contacting with the server.")

            
            elif self.provider == 'adfocus':
                shortner.adfocus()
                
            elif self.provider == 'shrinkearn':
                shortner.shrinkearn()

            elif self.provider == 'v2link':
                shortner.v2links()

            elif self.provider == 'bitly':
                shortner.bitly()

            else:
                messagebox.showwarning(f"Invalid Host" , "Please choose a valid hosting provider.")
                
        else:
            messagebox.showerror("Error", "An unknown error occured.")
        
    '''def copy_url(self, event):
        self.long_url_str = self.long_url.get()
        self.shrink_url = self.get_url()'''
    
    def press_enter(self, event):
        self.shrinkButton.invoke()
        

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()