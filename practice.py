import Tkinter
import requests
from Tkinter import *
import tkMessageBox
from PIL import Image,ImageTk
import urllib2


root=Tkinter.Tk()
root.geometry("600x400")

player1=Label(root,text="player1")
player2=Label(root,text="player2")

name1=Entry(root)
name2=Entry(root)

player1.grid(row=0,column=0)
player2.grid(row=1,column=0)

name1.grid(row=0,column=1)
name2.grid(row=1,column=1)

img=PhotoImage(file="index.png")


label=Label(root,image=img)
label.grid(row=0,column=2,columnspan=2,rowspan=2,padx=25,pady=5)


def codeforce():
	str1=name1.get()
	str2=name2.get()

	URL="http://codeforces.com/api/user.info?handles="+str1+";"+str2

	response=requests.get(URL,verify=True)

	if response.status_code!=200:
		root.iconify()
		MSG=tkMessageBox.showerror('Warning','Wrong credential')
		#root.deiconify()
	else:
		

		win=Toplevel()
		

		

		data=response.json()

		rating1=data['result'][0]['rating']
		dp1=Image.open(urllib2.urlopen(data['result'][0]['titlePhoto']))
		dp1=ImageTk.PhotoImage(dp1)
		maxrating1=data['result'][0]['maxRating']
		maxrank1=data['result'][0]['maxRank']

		rating2=data['result'][1]['rating']
		dp2=ImageTk.PhotoImage(Image.open(urllib2.urlopen(data['result'][1]['titlePhoto'])))
		maxrating2=data['result'][1]['maxRating']
		maxrank2=data['result'][1]['maxRank']



		label1=Label(win,image=dp1)
		label1.grid(row=0,column=0,columnspan=2,padx=25,pady=5)

		label2=Label(win,image=dp2)
		label2.grid(row=0,column=2,columnspan=2)

		label3=Label(win,text="Current Rating="+str(rating1),width=100,fg="red")
		label3.grid(row=1,column=0)

		label4=Label(win,text="Current Rating="+str(rating2),pady=20,width=100,fg="red")
		label4.grid(row=1,column=3)

		label5=Label(win,text="Max Rating="+str(maxrating1),pady=20,width=100,fg="blue")
		label5.grid(row=2,column=0)

		label6=Label(win,text="Max Rating="+str(maxrating2),pady=20,width=100,fg="blue")
		label6.grid(row=2,column=3)

		label7=Label(win,text="Max Rank="+str(maxrank1),pady=20,width=100,fg="green")
		label7.grid(row=3,column=0)

		label8=Label(win,text="Max Rank="+str(maxrank2),pady=20,width=100,fg="green")
		label8.grid(row=3,column=3)
        
        
		win.mainloop()
		




		









comp=Button(root,text="Battle Begin",command=codeforce)
comp.grid(row=2,column=1)





root.resizable(False,False)
root.mainloop()
