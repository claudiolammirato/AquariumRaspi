import tkinter as tk
from sqlite import select_from_db, graph_data_sqlite
from time import strftime
from aquarium_camera import CameraON, CameraOFF
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from send_email import email

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
        window.after(290000, sensors_parameters)
    
    #time
    def time():
        string = strftime('%H:%M:%S %p')
        tk.Label(window, text = string).place(x = 920, y = 10) 
        window.after(1000, time)

    #Graph WIndows
    def openNewWindow():
        graph_window = tk.Tk()
        graph_window.title("Temperature & Humidity") 
        window_width = 1000
        window_height = 500
        
        #ceneter positioning
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = screen_width/2 - window_width/2
        y = screen_height/2 - window_height/2

        graph_window.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))
        #retrieve data from sqlite
        data = graph_data_sqlite()
        #print(data)

        #draw graph 1
        x1 = data.DATE
        x = x1.str.slice(start=11, stop=16, step=1)
        y = data.TEMP_EXT

        px = 1/plt.rcParams['figure.dpi']
        figure1 = plt.Figure(figsize=(500*px, 250*px))
        ax1 = figure1.add_subplot()
        ax1.tick_params(axis='x', labelsize=8)
        ax1.tick_params(axis='y', labelsize=8)
        ax1.set_ylim([18,35])
        ax1.plot(x,y)
        

        line1 = FigureCanvasTkAgg(figure1, graph_window)
        line1.get_tk_widget().grid(row=0,column=0)
        line1.draw()

        #draw graph 2
        x22 = data.DATE
        x2 = x22.str.slice(start=11, stop=16, step=1)
        y2 = data.HUM_EXT

        px2 = 1/plt.rcParams['figure.dpi']
        figure2 = plt.Figure(figsize=(500*px, 250*px))
        ax2 = figure2.add_subplot()
        ax2.tick_params(axis='x', labelsize=8)
        ax2.tick_params(axis='y', labelsize=8)
        ax2.set_ylim([30,80])
        ax2.plot(x,y)
        

        line2 = FigureCanvasTkAgg(figure2, graph_window)
        line2.get_tk_widget().grid(row=0,column=1)
        line2.draw()

        #draw graph 3
        x33 = data.DATE
        x3 = x33.str.slice(start=11, stop=16, step=1)
        y3 = data.TEMP_EXT

        px3 = 1/plt.rcParams['figure.dpi']
        figure3 = plt.Figure(figsize=(500*px, 250*px))
        ax3 = figure3.add_subplot()
        ax3.tick_params(axis='x', labelsize=8)
        ax3.tick_params(axis='y', labelsize=8)
        ax3.set_ylim([18,35])
        ax3.plot(x,y)
        

        line3 = FigureCanvasTkAgg(figure3, graph_window)
        line3.get_tk_widget().grid(row=1,column=0)
        line3.draw()

        #draw graph 4
        x44 = data.DATE
        x4 = x44.str.slice(start=11, stop=16, step=1)
        y4 = data.TEMP_EXT

        px4 = 1/plt.rcParams['figure.dpi']
        figure4 = plt.Figure(figsize=(500*px, 250*px))
        ax4 = figure4.add_subplot()
        ax4.tick_params(axis='x', labelsize=8)
        ax4.tick_params(axis='y', labelsize=8)
        ax4.set_ylim([18,35])
        ax4.plot(x,y)
        

        line4 = FigureCanvasTkAgg(figure4, graph_window)
        line4.get_tk_widget().grid(row=1,column=1)
        line4.draw()


    window = tk.Tk()

    #window.wm_attributes('-fullscreen','true')
    window.geometry("%dx%d+0+0" % (window.winfo_screenwidth(), window.winfo_screenheight()))
    #window.overrideredirect(1)
    window.wm_attributes('-fullscreen','true')
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

    #camera
    tk.Button(window, text='Start Camera', command=CameraON).place(x = 620, y = 280)
    tk.Button(window, text='Stop Camera', command=CameraOFF).place(x = 790, y = 280)

    #closebutton.grid(row=0, column=1)

    #Graph Button

    btn = tk.Button(window, text ="Open Graph", command = openNewWindow).place(x = 10, y = 280)
    btn1 = tk.Button(window, text ="send email", command = email).place(x = 10, y = 400)
    
    
        

    #connectionDBButton = tk.Button(text="Connetti al DB", command=database_connection)
    #connectionDBButton.grid(row=0,column=0)


    sensors_parameters()
    time()
    window.mainloop()