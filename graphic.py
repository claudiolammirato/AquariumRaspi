import tkinter as tk
import tkinter as ttk

def grafica():
    window = tk.Tk()
    #window.wm_attributes('-fullscreen','true')
    window.geometry("%dx%d+0+0" % (window.winfo_screenwidth(), window.winfo_screenheight()))
    window.overrideredirect(1)
    window.resizable(False, False)
    #window.title("Aquarium")

    #layout
    

    closebutton = tk.Button(window, text="My Button2", command=window.quit)
    closebutton.grid(row=0, column=1)

    def quit(self):
        self.root.destroy()

    #connectionDBButton = tk.Button(text="Connetti al DB", command=database_connection)
    #connectionDBButton.grid(row=0,column=0)

    window.mainloop()