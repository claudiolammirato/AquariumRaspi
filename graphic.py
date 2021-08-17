import tkinter as tk
from sqlite import select_from_db
from time import strftime

def grafica():

    def quit():
        window.destroy()
        
    #retrieve parameters
    def sensors_parameters():
        rows = select_from_db()
        #print (rows[len(rows)-1])
        ext_temp = str("{:5.1f}".format(rows[len(rows)-1][1]))
        ext_hum = str("{:5.1f}".format(rows[len(rows)-1][2]))
        ext_date = rows[len(rows)-1][3][11:16]
        tk.Label(window, text = "External Temperature is: " + ext_temp + "°C @ " +ext_date).place(x = 10, y = 80) 
        tk.Label(window, text = "External Humidity is: " + ext_hum + "% @ "+ext_date).place(x = 10, y = 100) 
        window.after(600000, sensors_parameters)
    
    #time
    def time():
        string = strftime('%H:%M:%S %p')
        tk.Label(window, text = string).place(x = 920, y = 10) 
        window.after(1000, time)

    window = tk.Tk()

    #window.wm_attributes('-fullscreen','true')
    window.geometry("%dx%d+0+0" % (window.winfo_screenwidth(), window.winfo_screenheight()))
    window.overrideredirect(1)
    window.resizable(False, False)
    #window.title("Aquarium")

    #Title
    title_frame = tk.Frame(window, highlightbackground="grey", highlightcolor="black", highlightthickness=1, width=1024, height=40)
    title_frame.place(x=0, y=0)
    
    #bottom frame
    bottom_frame_dx = tk.Frame(window, highlightbackground="grey", highlightcolor="black", highlightthickness=1, width=512, height=280)
    bottom_frame_dx.place(x=512, y=320)
    bottom_frame_sx = tk.Frame(window, highlightbackground="grey", highlightcolor="black", highlightthickness=1, width=512, height=280)
    bottom_frame_sx.place(x=0, y=320)
    #top_frame
    top_frame_dx = tk.Frame(window, highlightbackground="grey", highlightcolor="black", highlightthickness=1, width=512, height=280)
    top_frame_dx.place(x=512, y=40)
    top_frame_sx = tk.Frame(window, highlightbackground="grey", highlightcolor="black", highlightthickness=1, width=512, height=280)
    top_frame_sx.place(x=0, y=40)

    closebutton = tk.Button(bottom_frame_dx, text="Close App", command=quit)
    closebutton.place(x=400, y=230)

    Label1 = tk.Label(text="Parameters")
    Label1.place(x=10, y=50)
    Label2 = tk.Label(text="Video")
    Label2.place(x=522, y=50)
    Label3 = tk.Label(text="Relay")
    Label3.place(x=10, y=330)
    Label4 = tk.Label(text="Settings")
    Label4.place(x=522, y=330)
    Labeltitle = tk.Label(text="Aquarium")
    Labeltitle.place(x=480, y=10)

    #closebutton.grid(row=0, column=1)
    
    
        

    #connectionDBButton = tk.Button(text="Connetti al DB", command=database_connection)
    #connectionDBButton.grid(row=0,column=0)


    sensors_parameters()
    time()
    window.mainloop()