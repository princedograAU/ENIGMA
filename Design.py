__author__ = 'Prince Dogra'

from tkinter import *
from tkinter import ttk

base = Tk()

base.title("DEGEN_ENIGMA-B8")
base.resizable(0,0)
notebook = ttk.Notebook(base)
frame_enc = ttk.Frame(notebook)
frame_dec = ttk.Frame(notebook)

screenWidth = base.winfo_screenwidth()
screenHeight = base.winfo_screenheight()
base.minsize(int(screenWidth/2 + 10),int(screenHeight/2))

'''------------------------------------------- E N C R Y P T I O N   T A B-------------------------------------------'''

frame_enc = Frame(notebook,bg="black",width=screenWidth/2,height=screenHeight/2,padx=10,pady=10)
frame_enc.pack()

img = Canvas(frame_enc,width=screenWidth/4 - 10,height=screenHeight/3,bg="#dddddd")
img.grid(row=0,padx=5,pady=5)

uploadImage = Button(frame_enc,text="Upload Image",bg="#dddddd",fg="black",font=("Verdana",12))
uploadImage.grid(row=1,padx=5,pady=5)

q1 = Label(frame_enc,fg="white",text="** Select any image from your system **",bg="black")
q1.grid(row=2,padx=5,pady=5)

textarea = Text(frame_enc,fg="white",width=int(screenWidth/28),height=int(screenHeight/48))
textarea.grid(row=0,column=1,padx=5,pady=5)

encButton = Button(frame_enc,text="Encrypt Data",bg="#dd1111",fg="white",font=("Verdana",12))
encButton.grid(row=1,column=1,padx=5,pady=5)

'''
encSaveButton = Button(frame_enc,text="Save Image",bg="#11dd11",fg="white",font=("Verdana",12))
encSaveButton.grid(row=1,column=2,padx=5,pady=5)'''

q2 = Label(frame_enc,fg="white",text="** Enter data for encryption **",bg="black")
q2.grid(row=2,column=1,padx=5,pady=5)

'''------------------------------------------- D E C R Y P T I O N   T A B-------------------------------------------'''

frame_dec = Frame(notebook,bg="#ffffff",width=screenWidth/2,height=screenHeight/2,padx=10,pady=10)
frame_dec.pack()

img_dec = Canvas(frame_dec,width=screenWidth/4 - 10,height=screenHeight/3,bg="#dddddd")
img_dec.grid(row=0,padx=5,pady=5,columnspan="2")

upload_dec = Button(frame_dec,text="Upload Image",bg="#dddddd",fg="black",font=("Verdana",12))
upload_dec.grid(row=1,column=0,padx=5,pady=5)

decData = Button(frame_dec,text="Decrypt Data",bg="#11cc11",fg="white",font=("Verdana",12))
decData.grid(row=1,column=1,pady=5)

q3 = Label(frame_dec,fg="black",text="** Decrypted data will shown in the text area **",bg="white")
q3.grid(row=2,padx=5,pady=5)

textarea_dec = Text(frame_dec,fg="#11cc11",bg="white",width=int(screenWidth/28),height=int(screenHeight/48))
textarea_dec.grid(row=0,column=2,padx=5,pady=5)

q4 = Label(frame_dec,fg="black",text="** This is the actual data **",bg="white")
q4.grid(row=2,column=2,padx=5,pady=5)

'''------------------------------------------- O T H E R   D A T A -------------------------------------------'''

notebook.add(frame_enc,text="Encrypt")
notebook.add(frame_dec,text="Decrypt")
notebook.pack(expand=1,fill="both")

statusBar = Label(base,text="Wecome to encryption toolkit",bd=2,relief=SUNKEN,anchor=W)
statusBar.pack(side=BOTTOM,fill=X)

base.mainloop()

'''-----------------------------------------H I N T  B O X-----------------------------------------------------------'''

'''
tk = tkinter.Tk()
can = tkinter.Canvas(tk)
can.pack()
img = tkinter.PhotoImg("<path/to/image_file>.gif")
can.create_image((x_coordinate, y_coordinate), img)
'''