from tkinter import *

window=Tk()
window.geometry("600x420+100+75")
window.title("Tic Tac Toe")
one=StringVar()
two=StringVar()
three=StringVar()
four=StringVar()
five=StringVar()
six=StringVar()
seven=StringVar()
eight=StringVar()
nine=StringVar()

lst=[0,0,0,0,0,0,0,0,0]
user="A"

print("player1 is A and player2 is B")
def changeUser():    
    if globals()['user']=="B":
        globals()['user']="A"
    else:
        globals()['user'] = "B"

        
def play(n):
    globals()['lst'][n-1]=user
    changeUser()
    print(globals()['lst'])
    if lst[0]==lst[1]==lst[2]=='A':
        print ("winner is A")
    elif lst[3]==lst[4]==lst[5]=='A' :
        print("winner is A")
    elif lst[6] == lst[7] == lst[8] == 'A':
        print("winner is A")
    elif lst[0]==lst[3]==lst[6]=='A' :
        print("winner is A")
    elif lst[1]==lst[4]==lst[7]=='A' :
        print("winner is A")
    elif lst[2]==lst[5]==lst[8]=='A' :
        print("winner is A")
    elif lst[0]==lst[4]==lst[8]=='A' :
        print("winner is A")
    elif lst[2]==lst[4]==lst[8]=='A' :
        print("winner is A")
    elif lst[0]==lst[1]==lst[2]=='B':
        print ("winner is B")
    elif lst[3]==lst[4]==lst[5]=='B' :
        print("winner is B")
    elif lst[6] == lst[7] == lst[8] == 'B':
        print("winner is B")
    elif lst[0]==lst[3]==lst[6]=='B' :
        print("winner is B")
    elif lst[1]==lst[4]==lst[7]=='B' :
        print("winner is B")
    elif lst[2]==lst[5]==lst[8]=='B' :
        print("winner is B")
    elif lst[0]==lst[4]==lst[8]=='B' :
        print("winner is B")
    elif lst[2]==lst[4]==lst[8]=='B' :
        print("winner is B")

    
Button(window,textvariable=one,bg="#303F9F",
           fg="#FFFFFF",font=("Arial",24,"bold"),
           width=10,height=3,
           command=lambda: play(1)).place(x=0,y=0)
Button(window,textvariable=two,bg="#303F9F",
           fg="#FFFFFF",font=("Arial",24,"bold"),
           width=10,height=3,
           command=lambda: play(2)).place(x=200,y=0)
Button(window,textvariable=three,bg="#303F9F",
           fg="#FFFFFF",font=("Arial",24,"bold"),
           width=10,height=3,
           command=lambda: play(3)).place(x=400,y=0)
Button(window,text=' ',bg="#303F9F",
           fg="#FFFFFF",font=("Arial",24,"bold"),
           width=10,height=3,
           command=lambda: play(4)).place(x=0,y=140)
Button(window,textvariable=five,bg="#303F9F",
           fg="#FFFFFF",font=("Arial",24,"bold"),
           width=10,height=3,
           command=lambda: play(5)).place(x=200,y=140)
Button(window,textvariable=six,bg="#303F9F",
           fg="#FFFFFF",font=("Arial",24,"bold"),
           width=10,height=3,
           command=lambda: play(6)).place(x=400,y=140)
Button(window,textvariable=seven,bg="#303F9F",
           fg="#FFFFFF",font=("Arial",24,"bold"),
           width=10,height=3,
           command=lambda: play(7)).place(x=0,y=280)
Button(window,textvariable=eight,bg="#303F9F",
           fg="#FFFFFF",font=("Arial",24,"bold"),
           width=10,height=3,
           command=lambda: play(8)).place(x=200,y=280)
Button(window,textvariable=9,bg="#303F9F",
           fg="#FFFFFF",font=("Arial",24,"bold"),
           width=10,height=3,
           command=lambda: play(9)).place(x=400,y=280)

window.mainloop()
