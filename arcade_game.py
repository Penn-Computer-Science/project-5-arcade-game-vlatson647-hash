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
        "01201110210",
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
                img.put('red', (x,y))
            if pattern[y][x] == '2':
                img.put('lime green', (x,y))
    return img
def enemy_projectile():
    
    pattern = [
        "00111111100",
        "00011111000",
        "00001410000",
        "00001410000",
        "00001410000",
        "00001410000",
        "00001410000",
        "00001410000",
        "00000100000",
    ]
    h = len(pattern)
    w = len(pattern[0])

    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == '1':
                img.put('lime green', (x,y))
            if pattern[y][x] == '2':
                img.put('cyan', (x,y))
    return img





# Build window
root = tk.Tk()
root.title("BLOCK SHOOTERZ")

label = tk.Label(root, text= 'SCORE: 0')
label.pack()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
canvas.pack()

enemy_img = enemy_sprite()
project_img = enemy_projectile()

# player creation
player = canvas.create_rectangle(60, 50, 70, 100, fill= 'white')

# enemy lists
enemies = []
projectiles = []
lasers = []

def create_laser():
    img = tk.PhotoImage(width=4, height=10)

    for y in range(10):
        for x in range(4):
            img.put('cyan', (x,y))
    return img
laser_img = create_laser()

def shoot(event):
    px1, py1, px2, py2 = canvas.bbox(player)
    l = canvas.create_image((px1+px2)//2, py1, image=laser_img, anchor='sw')

    lasers.append(l)

root.bind('<space>', shoot)

def collision(e,l):
    ex1, ey1, ex2, ey2 = canvas.bbox(e)
    lx1, ly1, lx2, ly2 = canvas.bbox(l)

    return ex1 < lx2 and ex2 > lx1 and ey1 < ly2 and ey2 > ly1






# movement
def move_up(event):
    canvas.move(player, 0,  -25)

def move_down(event):
    canvas.move(player, 0, 25)

def move_left(event):
    canvas.move(player, -15,  0)

def move_right(event):
    canvas.move(player, 15, 0)



# binds
root.bind('<Up>', move_up)
root.bind('<Down>', move_down)
root.bind('<Left>', move_left)
root.bind('<Right>', move_right)



# spawns enemies
def spawn_enemy():
    x = random.randint(WIDTH-200, WIDTH-20)
    enemy = canvas.create_image(x,0, image=enemy_img)
    enemies.append(enemy)
def spawn_projectile():
    x = random.randint(0, 399)
    projectile = canvas.create_image(x,0, image=project_img)
    projectiles.append(projectile)


alive = True
# runs game
def game_loop():
    global SCORE
    global alive
    global collision


    if not alive:
        canvas.delete('all')
        root.unbind('<Up>')
        root.unbind('<Down>')
    if not alive:
        canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER", fill='red', font=('arial',24))
        return
    
    px1, py1, px2, py2 = canvas.bbox(player)

    if py1 < 1 or py2 > 451:
        alive = False
    if random.randint(1,1)==1:
        spawn_enemy()
    # if random.randint(1,5)==1 and SCORE > 4:
    #     spawn_projectile()
    # if random.randint(1,5)==1:
    #     spawn_projectile()

    for enemy in enemies:
        canvas.move(enemy, 0, 8)
    for projectile in projectiles:
        canvas.move(projectile, 0, 10)

        if canvas.bbox(projectile) and canvas.bbox(player):
            ex1, ey1, ex2, ey2 = canvas.bbox(projectile)
            px1, py1, px2, py2 = canvas.bbox(player)
        if ex1 < px2 and ex2 > px1 and ey1 < py2 and ey2 > py1:
            alive = False
    for l in lasers:
        canvas.move(l, 20, 0)
        x1, y1, x2, y2 = canvas.bbox(l)
        if y2 < 0:
            canvas.delete(l)
            lasers.remove(l)
    


    root.after(30, game_loop)

for l in lasers:
    for e in enemies:
        if collision(e,l):
            SCORE+=1
            label.config(text=f"SCORE: {SCORE}")
            canvas.delete(l)
            canvas.delete(e)
        if l in lasers:
            lasers.remove(l)
        if e in enemies:
            enemies.remove(e)

        break



# runs game/shows window
game_loop()
root.mainloop()