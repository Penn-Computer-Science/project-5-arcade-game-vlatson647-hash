import tkinter as tk

WIDTH = 600
HEIGHT = 450
SCORE_LEFT = 0
SCORE_RIGHT = 0

# Build window
root = tk.Tk()
root.title("Block Shooterz")

label_left = tk.Label(root, text= 'PLAYER 1 SCORE: 0')
label_left.pack()
label_right = tk.Label(root, text= 'PLAYER 2 SCRORE: 0')
label_right.pack()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
canvas.pack()

# player creation
player1 = canvas.create_rectangle(50, 160, 60, 250, fill= 'red')
player2 = canvas.create_rectangle(540, 150, 550, 250, fill= 'blue')

# enemy list
enemies = []


# status booleans
alive1 = True
alive2 = True


# movement
def one_up(event):
    canvas.move(player1, 0,  -25)

def one_down(event):
    canvas.move(player1, 0, 25)

def two_up(event):
    canvas.move(player2, 0, -25)

def two_down(event):
    canvas.move(player2, 0, 25)


# binds
canvas.bind_all('<w>', one_up)
canvas.bind_all('<s>', one_down)
canvas.bind_all('<Up>', two_up)
canvas.bind_all('<Down>', two_down)













# runs game/shows window
root.mainloop()