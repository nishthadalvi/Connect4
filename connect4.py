from tkinter import *
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
from tkinter import messagebox
import tkinter

root = Tk()
root.title('Connect 4 - Nishtha and Surya')
#root.geometry("480x150")

#Red starts so True
clicked = True
count = 0

def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36,b37,b38,b39,b40,b41,b42
    global clicked, count
    clicked = True
    count = 0
    buttons_matrix = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],]

    b1 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b1))
    b1.grid(column = 0, row = 0)
    b2 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b2))
    b2.grid(column = 0, row = 1)
    b3 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b3))
    b3.grid(column = 0, row = 2)
    b4 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b4))
    b4.grid(column = 0, row = 3)
    b5 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b5))
    b5.grid(column = 0, row = 4)
    b6 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b6))
    b6.grid(column = 0, row = 5)

    b7 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b7))
    b7.grid(column = 1, row = 0)
    b8 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b8))
    b8.grid(column = 1, row = 1)
    b9 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b9))
    b9.grid(column = 1, row = 2)
    b10 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b10))
    b10.grid(column = 1, row = 3)
    b11 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b11))
    b11.grid(column = 1, row = 4)
    b12 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b12))
    b12.grid(column = 1, row = 5)

    b13 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b13))
    b13.grid(column = 2, row = 0)
    b14 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b14))
    b14.grid(column = 2, row = 1)
    b15 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b15))
    b15.grid(column = 2, row = 2)
    b16 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b16))
    b16.grid(column = 2, row = 3)
    b17 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b17))
    b17.grid(column = 2, row = 4)
    b18 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b18))
    b18.grid(column = 2, row = 5)

    b19 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b19))
    b19.grid(column = 3, row = 0)
    b20 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b20))
    b20.grid(column = 3, row = 1)
    b21 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b21))
    b21.grid(column = 3, row = 2)
    b22 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b22))
    b22.grid(column = 3, row = 3)
    b23 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b23))
    b23.grid(column = 3, row = 4)
    b24= Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b24))
    b24.grid(column = 3, row = 5)

    b25 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b25))
    b25.grid(column = 4, row = 0)
    b26 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b26))
    b26.grid(column = 4, row = 1)
    b27 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b27))
    b27.grid(column = 4, row = 2)
    b28 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b28))
    b28.grid(column = 4, row = 3)
    b29 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b29))
    b29.grid(column = 4, row = 4)
    b30= Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b30))
    b30.grid(column = 4, row = 5)

    b31 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b31))
    b31.grid(column = 5, row = 0)
    b32 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b32))
    b32.grid(column = 5, row = 1)
    b33 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b33))
    b33.grid(column = 5, row = 2)
    b34 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b34))
    b34.grid(column = 5, row = 3)
    b35 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b35))
    b35.grid(column = 5, row = 4)
    b36= Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b36))
    b36.grid(column = 5, row = 5)

    b37 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b37))
    b37.grid(column = 6, row = 0)
    b38 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b38))
    b38.grid(column = 6, row = 1)
    b39 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b39))
    b39.grid(column = 6, row = 2)
    b40 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b40))
    b40.grid(column = 6, row = 3)
    b41 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b41))
    b41.grid(column = 6, row = 4)
    b42= Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b42))
    b42.grid(column = 6, row = 5)

    matrix = [[b1,b7,b13,b19,b25,b31,b37], [b2,b8,b14,b20,b26,b32,b38], [b3,b9,b15,b21,b27,b33,b39] , [b4,b10,b16,b22,b28,b34, b40], [b5,b11,b17,b23,b29,b35,b41],[b6,b12,b18,b24,b30,b36, b42]]


def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)
    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)
    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)
    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)
    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)
    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)
    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)
    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)

# Build our buttons
buttons_matrix = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],]

b1 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b1))
b1.grid(column = 0, row = 0)
b2 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b2))
b2.grid(column = 0, row = 1)
b3 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b3))
b3.grid(column = 0, row = 2)
b4 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b4))
b4.grid(column = 0, row = 3)
b5 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b5))
b5.grid(column = 0, row = 4)
b6 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b6))
b6.grid(column = 0, row = 5)


b7 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b7))
b7.grid(column = 1, row = 0)
b8 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b8))
b8.grid(column = 1, row = 1)
b9 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b9))
b9.grid(column = 1, row = 2)
b10 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b10))
b10.grid(column = 1, row = 3)
b11 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b11))
b11.grid(column = 1, row = 4)
b12 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b12))
b12.grid(column = 1, row = 5)

b13 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b13))
b13.grid(column = 2, row = 0)
b14 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b14))
b14.grid(column = 2, row = 1)
b15 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b15))
b15.grid(column = 2, row = 2)
b16 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b16))
b16.grid(column = 2, row = 3)
b17 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b17))
b17.grid(column = 2, row = 4)
b18 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b18))
b18.grid(column = 2, row = 5)

b19 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b19))
b19.grid(column = 3, row = 0)
b20 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b20))
b20.grid(column = 3, row = 1)
b21 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b21))
b21.grid(column = 3, row = 2)
b22 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b22))
b22.grid(column = 3, row = 3)
b23 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b23))
b23.grid(column = 3, row = 4)
b24= Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b24))
b24.grid(column = 3, row = 5)

b25 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b25))
b25.grid(column = 4, row = 0)
b26 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b26))
b26.grid(column = 4, row = 1)
b27 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b27))
b27.grid(column = 4, row = 2)
b28 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b28))
b28.grid(column = 4, row = 3)
b29 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b29))
b29.grid(column = 4, row = 4)
b30= Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b30))
b30.grid(column = 4, row = 5)

b31 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b31))
b31.grid(column = 5, row = 0)
b32 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b32))
b32.grid(column = 5, row = 1)
b33 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b33))
b33.grid(column = 5, row = 2)
b34 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b34))
b34.grid(column = 5, row = 3)
b35 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b35))
b35.grid(column = 5, row = 4)
b36= Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b36))
b36.grid(column = 5, row = 5)

b37 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b37))
b37.grid(column = 6, row = 0)
b38 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b38))
b38.grid(column = 6, row = 1)
b39 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b39))
b39.grid(column = 6, row = 2)
b40 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b40))
b40.grid(column = 6, row = 3)
b41 = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b41))
b41.grid(column = 6, row = 4)
b42= Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", command=lambda: b_click(b42))
b42.grid(column = 6, row = 5)
matrix = [[b1,b7,b13,b19,b25,b31,b37], [b2,b8,b14,b20,b26,b32,b38], [b3,b9,b15,b21,b27,b33,b39] , [b4,b10,b16,b22,b28,b34, b40], [b5,b11,b17,b23,b29,b35,b41],[b6,b12,b18,b24,b30,b36, b42]]
#Button is clicked: Checks if spot is available and if it is the bottommost spot available
def b_click(b):
    bRow = int(b.grid_info()['row'])
    bCol = int(b.grid_info()['column'])

    global clicked, count

    if (buttons_matrix[bRow])[bCol] == 0 and (bRow == 5 or (buttons_matrix[bRow + 1])[bCol] != 0):
        buttons_matrix[bRow][bCol] = 1
        if(clicked == True): #It is Red's Turn
            clicked = False
            b.config(bg = 'red', text = "X")
            matrix[bRow][bCol].config(text = "X")
            count+=1
            # call checkifwon and pass in text and row and col
            checkifwon(bRow, bCol, "X")
            # add 1 to count global var
            
        else:
            clicked = True
            b.config(bg = 'yellow', text = "O")
            matrix[bRow][bCol].config(text = "O")
            # call checkifwon and pass in text and row and col
            count +=1
            checkifwon(bRow, bCol, "O")
            #add 1 to count global var
            
       #print(buttons_matrix)
    elif (buttons_matrix[bRow])[bCol] == 1:
        messagebox.showerror("Connect 4 - Nishtha and Surya", "Hey! That spot has already been selected\nPick another spot..." )
    elif (buttons_matrix[bRow + 1])[bCol] == 0:
        messagebox.showerror("Connect 4 - Nishtha and Surya", "Whoops! The spot you have pick defies gravity.\nPlease pick the bottomost button in a column...")

def checkifwon(row, col, sym):
    inRow = 1
    if (row - 1 > -1) and matrix[row-1][col]["text"] is sym:
        inRow+=1
        if row-2 > -1 and matrix[row -2][col]["text"] is sym:
            inRow +=1
            if row-3 > -1 and matrix[row-3][col]["text"] is sym:
                inRow +=1
                declareWinner(sym)
                return True
    if (row +1 <6) and matrix[row+1][col]["text"] is sym:
        inRow +=1
        if(inRow==4):
            declareWinner(sym)
        if row +2 <6 and matrix[row+2][col]["text"] is sym:
            inRow+=1
            if(inRow==4):
                declareWinner(sym)
            if row+3 < 6 and matrix[row+3][col]["text"] is sym:
                declareWinner(sym)
    inRow=1
    if (col - 1 > -1) and matrix[row][col-1]["text"] is sym:
        inRow+=1
        if col-2 > -1 and matrix[row][col-2]["text"] is sym:
            inRow +=1
            if col-3 > -1 and matrix[row][col-3]["text"] is sym:
                inRow +=1
                declareWinner(sym)
    inRow=1
    if (col +1 <7) and matrix[row][col+1]["text"] == sym:
        inRow +=1
        if(inRow==4):
            declareWinner(sym)
        if col +2 <7 and matrix[row][col+2]["text"] is sym:
            inRow+=1
            if(inRow==4):
                declareWinner(sym)
            if col+3 < 7 and matrix[row][col+3]["text"] is sym:
                declareWinner(sym)
    inRow = 1
    if (row-1 > -1 and col + 1 < 7) and matrix[row-1][col+1]["text"] is sym:
        inRow+=1
        if inRow == 4:
            declareWinner(sym)
        if (row - 2 > -1 and col + 2 < 7) and matrix[row-2][col+2]["text"] is sym:
            inRow+=1
            if inRow == 4:
                declareWinner(sym)
            if (row - 3 > -1 and col + 3 < 7) and matrix[row-3][col+3]["text"] is sym:
                declareWinner(sym)
    inRow = 1
    if (row + 1 < 6 and col - 1 > -1) and matrix[row+1][col-1]["text"] is sym:
        inRow+=1
        if inRow == 4:
            declareWinner(sym)
        if (row + 2 < 6 and col - 2 > -1) and matrix[row+2][col-2]["text"] is sym:
            inRow+=1
            if inRow == 4:
                declareWinner(sym)
            if (row + 3 < 6 and col - 3 > -1) and matrix[row+3][col-3]["text"] is sym:
                declareWinner(sym)
    inRow = 1
    if (row - 1 > -1 and col - 1 > -1) and matrix[row-1][col-1]["text"] is sym:
        inRow+=1
        if inRow == 4:
            declareWinner(sym)
        if (row - 2 > -1 and col - 2 > -1) and matrix[row-2][col-2]["text"] is sym:
            inRow+=1
            if inRow == 4:
                declareWinner(sym)
            if (row - 3 > -1 and col - 3 > -1) and matrix[row-3][col-3]["text"] is sym:
                declareWinner(sym)
    inRow = 1
    if (row + 1 < 6 and col + 1 < 7) and matrix[row+1][col+1]["text"] is sym:
        inRow+=1
        if inRow == 4:
            declareWinner(sym)
        if (row + 2  < 6  and col + 2 < 7) and matrix[row+2][col+2]["text"] is sym:
            inRow+=1
            if inRow == 4:
                declareWinner(sym)
            if (row + 3  < 6  and col + 3 < 7) and matrix[row+3][col+3]["text"] is sym:
                declareWinner(sym)
    # Check if tie
    if count == 42:
        messagebox.showinfo("Connect 4 - Nishtha and Surya", "It's A Tie!\n No One Wins!")
        disable_all_buttons()


def declareWinner(sym):
    messagebox.showinfo("Connect 4 - Nishtha and Surya", "CONGRATULATIONS!" + sym +  "Wins!!")
    disable_all_buttons()

# add reset method
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()

root.mainloop()