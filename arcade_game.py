import tkinter as tk
import random

WIDTH = 600
HEIGHT = 450
SCORE = 0

# enemy creation
def enemy_sprite():
    pattern = [
        "00111111100",
        "00111111100",
        "00111111100",
        "01101111010",
        "11111111111",
        "10111111101",
        "10100000101",
        "00011011000",
    ]
    h = len(pattern)
    w = len(pattern[0])

    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == '1':
                img.put('purple', (x,y))





# Build window
root = tk.Tk()
root.title("BLOCK SHOOTERZ")

label = tk.Label(root, text= 'SCORE: 0')
label.pack()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
canvas.pack()

enemy_img = enemy_sprite()

# player creation
player = canvas.create_rectangle(60, 100, 70, 200, fill= 'white')

# enemy list
enemies = []

alive = True


# movement
def move_up(event):
    canvas.move(player, 0,  -25)

def move_down(event):
    canvas.move(player, 0, 25)



# binds
root.bind('<Up>', move_up)
root.bind('<Down>', move_down)



# spawns enemies
def spawn_enemy():
    x = random.randint(0, WIDTH-20)
    enemy = canvas.create_image(x,50, image=enemy_img, anchor = 'nw')
    enemies.append(enemy)


# runs game
def run_game():
    global SCORE
    global alive

    if not alive:
        canvas.delete('all')
        root.unbind('<Up>')
        root.unbind('<Down>')
    if not alive:
        canvas.create_text(WIDTH//2, HEIGHT//2, text="DO NOT MOVE OUT!", fill='red', font=('arial',24))
        return
    
    px1, py1, px2, py2 = canvas.bbox(player)

    if py1 < 1 or py2 > 451:
        alive = False
    if random.randint(1,5)==1:
        spawn_enemy()

    for enemy in enemies:
        canvas.move(enemy, 0, 10)


    root.after(30, run_game)





# runs game/shows window
run_game()
root.mainloop()