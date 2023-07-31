import os
import tkinter as tk
from PIL import ImageTk, Image
import qrcode

def on_enter(e):
    convert_button.config(bg='#80C8FF', fg='white')

def on_leave(e):
    convert_button.config(bg='#2F2F2F', fg='#D5D5D5')

def fade_in(label, image):
    label.config(image=image, bg='#2F2F2F')
    label.image = image

    alpha = 0
    while alpha < 1:
        label.update()
        label.update_idletasks()
        label.config(bg=adjust_color('#2F2F2F', alpha))
        alpha += 0.02

def adjust_color(color, alpha):
    return '#%02x%02x%02x' % tuple(int(alpha * int(color[i:i+2], 16)) + int((1 - alpha) * int(color[i:i+2], 16)) for i in (1, 3, 5))

def main():
    try:
        qrcode_installed_label.pack_forget()
    except Exception as e:
        print(e)

    link = str(link_input.get())
    qrcode_img = qrcode.make(link)

    if os.path.exists('qrcode.jpg'):
        os.remove('qrcode.jpg')

    qrcode_img.save('qrcode.jpg') # Save the image directly using save() method

    img = Image.open("qrcode.jpg")
    img = img.resize((200, 200), Image.ANTIALIAS)

    global image_qr
    image_qr = ImageTk.PhotoImage(img)

    fade_in(qr_image_label, image_qr)

root = tk.Tk()
root.title('Link to QR Code Converter')
root.geometry('700x500')
root.config(bg='#2F2F2F')

root.bind('<Return>', lambda event=None: main())

title = tk.Label(root, text='Link to QR Code Converter', font='Helvetica 24 bold', bg='#2F2F2F', fg='#D5D5D5')
title.pack(pady=10)

link_input_label = tk.Label(root, text='Enter Link:', font='Helvetica 14', bg='#2F2F2F', fg='#D5D5D5')
link_input_label.pack()

link_input = tk.Entry(root, font='Helvetica 14', width=40, bg='#3F3F3F', fg='#D5D5D5', relief=tk.FLAT)
link_input.pack(pady=5)

convert_button = tk.Button(root, text='Convert', command=main, font='Helvetica 14', bg='#2F2F2F', fg='#D5D5D5', relief=tk.FLAT)
convert_button.pack(pady=10)

convert_button.bind("<Enter>", on_enter)
convert_button.bind("<Leave>", on_leave)

qr_image_label = tk.Label(root, bg='#2F2F2F')
qr_image_label.pack()

qrcode_installed_label = tk.Label(root, text="[ERROR]", fg='red', font='Helvetica 50')
qrcode_installed_label.pack_forget()

root.mainloop()
