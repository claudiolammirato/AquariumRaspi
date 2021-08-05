import tkinter as tk


def grafica():
    window = tk.Tk()
    #window.wm_attributes('-fullscreen','true')
    window.geometry("%dx%d+0+0" % (window.winfo_screenwidth(), window.winfo_screenheight()))
    window.overrideredirect(1)
    window.resizable(False, False)
    #window.title("Aquarium")

    #layout
    
    #bottom frame
    bottom_frame_dx = tk.Frame(window, highlightbackground="grey", highlightcolor="black", highlightthickness=1, width=512, height=300)
    bottom_frame_dx.place(x=512, y=300)
    bottom_frame_sx = tk.Frame(window, highlightbackground="grey", highlightcolor="black", highlightthickness=1, width=512, height=300)
    bottom_frame_sx.place(x=0, y=300)
    #top_frame
    top_frame_dx = tk.Frame(window, highlightbackground="grey", highlightcolor="black", highlightthickness=1, width=512, height=300)
    top_frame_dx.place(x=512, y=0)
    top_frame_sx = tk.Frame(window, highlightbackground="grey", highlightcolor="black", highlightthickness=1, width=512, height=300)
    top_frame_sx.place(x=0, y=0)

    closebutton = tk.Button(bottom_frame_dx, text="Close App", command=window.quit)
    closebutton.place(x=400, y=250)

    #closebutton.grid(row=0, column=1)

    def quit(self):
        self.root.destroy()

    #connectionDBButton = tk.Button(text="Connetti al DB", command=database_connection)
    #connectionDBButton.grid(row=0,column=0)

    window.mainloop()