import shortner
import tkinter as tk
import tkinter.font as tkFont


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        #Window Configurations
        self.title("URL Shrinker")
        self.geometry("300x400")
        self.resizable(height=False, width=False)

        #StrVariables
        self.long_url = tk.StringVar(self)
        self.provider = tk.StringVar(self)
        self.provider.set("cuttly") #Default Option

        #Setting up frames
        self.main_frame = tk.Frame()
        self.main_frame.pack()

        #URL Input Box
        self.entry_label = tk.Label(self.main_frame, text="Enter your long url:", font=('Roboto', 12))
        self.entry_label.grid(row=0, column=0, padx=0, pady=10)
        self.long_url_in = tk.Entry(self.main_frame, width=40, textvariable=self.long_url)
        self.long_url_in.grid(row=1, column=0, padx=0, pady=3)

        #Shrink Button
        self.shrinkButton = tk.Button(self.main_frame, text="Shrink!", command=self.shrink_url)
        self.shrinkButton.grid(row=2, column=0, padx=0, pady=0)

        #Shortened URL
        self.shortened_url = tk.Label(self.main_frame, text='Shortened URL :')
        self.shortened_url.grid(row=3, column=0, padx=0, pady=0)
        

    def shrink_url(self):
        self.long_url_str = self.long_url.get()
        self.shrink_url = shortner.select_host(host='cuttly', url=self.long_url_str)
        self.shortened_url.configure(text=f"Shortened URL: {self.shrink_url}")

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()