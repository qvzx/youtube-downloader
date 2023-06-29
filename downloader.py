import customtkinter
from pytube import YouTube

def download(): #Download function
    try:
        ytLink = url_var.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color='black')
        finishLabel.configure(text='')

        video.download()
        finishLabel.configure(text='DOWNLOADED', text_color='green')
    except:
        finishLabel.configure(text='ERROR', text_color='red')


#System Settings
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')


#App frame
app = customtkinter.CTk()
app.geometry('720x480')
app.title('Youtube Download')


#Adding UI Elements
title = customtkinter.CTkLabel(app, text='YouTube Downloader', font=('ubuntu', 50, 'bold'))
title.pack(pady=10, padx=10)


#Link input
url_var = customtkinter.StringVar()
link = customtkinter.CTkEntry(app, width=700, height=40, textvariable=url_var, font=('ubuntu', 20))
link.pack()


#Download button
download = customtkinter.CTkButton(app, text='DOWNLOAD MP4', command=download, font=('ubuntu', 20, 'bold'), width=700, height=40)
download.pack(pady=10)


#Finish Label
finishLabel = customtkinter.CTkLabel(app, text='', font=('ubuntu', 15, 'bold'))
finishLabel.pack()

app.mainloop()
