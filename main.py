import os
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image 
import qrcode


root = tk.Tk()
###################
screen_width = str(root.winfo_screenwidth())
screen_height = str(root.winfo_screenheight())
root.geometry('700x800')
root.config(bg='#d4d4d4')
root.maxsize(700,800)
root.minsize(600,700)

def error():
    problem_label.pack_forget()
    canvass.pack_forget()
    qrcode_installed_label.pack(side=TOP)
    problem_label.pack()
    canvass.pack()


def main():
    try:
        qrcode_installed_label.pack_forget()
    except Exception as e:
        print(e)
    


    # Assuming you have a link_input and canvass already defined

    # Get the link from the input
    link = str(link_input.get())

    # Generate the QR code image
    qrcode_img = qrcode.make(link)

    # Save the image directly using save() method
    qrcode_img.save('qrcode.jpg')

    # Define maximum width and height
    max_width = 500
    max_height = 500

    # Open the QR code image
    img = Image.open("qrcode.jpg")

    # Get the current dimensions of the image
    width, height = img.size

    # Calculate the new dimensions while maintaining the aspect ratio
    if width > max_width or height > max_height:
        ratio = min(max_width / width, max_height / height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        img = img.resize((new_width, new_height), Image.ANTIALIAS)

    # Save the resized image
    img.save('qrcode.jpg')

    # Load the resized image into a PhotoImage
    global image_qr
    image_qr = ImageTk.PhotoImage(file='qrcode.jpg')

    # Create a canvas and display the image
    canvass.create_image(80, 10, anchor=tk.NW, image=image_qr)

    # Remember to start the Tkinter main loop if you haven't already
    root.mainloop()



title = Label(root, text='link to qr code converter', font='Helvetica 30', bg='#d4d4d4')
title.pack()

link_input_label = Label(root, text='link:', font='link_input 15', bg='#d4d4d4')
link_input_label.pack()
link_input = Entry(root, font='Helvetica 16', width=50, bg='#1c1c1c', fg = 'white')
link_input.pack()

convert_button = Button(root, text='convert', command=main, font='Helvetica 16', bg='#1c1c1c', fg = 'white')
convert_button.pack()


problem_label = Label(root, text='qr code not working? link might be too long!', font='verdana 10')




canvass = Canvas(root, width=1300, height = 800, bg= '#1c1c1c')
canvass.pack()
problem_label.pack()
qrcode_installed_label = Label(root, text="[ERROR]", fg='red', font='verdana 50')


root.mainloop()
