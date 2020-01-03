import argparse
import curses
parser = argparse.ArgumentParser()
parser.add_argument('-lvl', action='store', dest='version_arg', type=int)
parsed_args = parser.parse_args()
LEVEL = parsed_args.version_arg or 1
import random
import time
'''
Above argparse and curses are imported and set up.#and numpy
Below I will establish the Classes before getting into the different LEVELs.
'''

class Sprite():
    def __init__(self, y, x, uni):
        self.y = y
        self.x = x
        self.uni = uni
    def __str__(self):
        return self.uni

class Item(Sprite):
    def __init__(self, y, x, uni, id):
        super().__init__(y, x, uni)
        self.id = id
    def __repr__(self):
        return self.uni

class Character(Sprite):
    def __init__(self, y, x, uni):
        super().__init__(y, x, uni)
        self.inv = []

    def __str__(self):
        return self.uni
    
    def move(self, direction, steps):
        # change the y/x position of the character
        pass

    def attack(self, direction, weapon):
        #attack and everything
        pass

hero = Character(10, 15, '😶')

enemies = [
    Character(7, 7, '👿'),
    Character(7, 23, '😈'),
    Character(13, 7, '😈'),
    Character(13, 23, '👿'),
]

items = [
    Item(11, 16, '🏹', 'bow'),
    Item(19, 5, '🔫', 'gun')
]

unicode_storage_list = ['🗡', '⚔', '🔫', '🏹', '🛡', '🔑', '🗝', '❤', '☠', '☠', '⬆', '➡', '⬇', '⬅']

moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

key_list = ['KEY_UP', 'KEY_DOWN', 'KEY_RIGHT', 'KEY_LEFT']

def fix_pos(sprite):
    if sprite.y < 0:
        sprite.y = 0
    if sprite.y > 20:
        sprite.y = 20
    if sprite.x < 0:
        sprite.x = 0
    if sprite.x > 30:
        sprite.x = 30

def aim(hero, wasd):
    if wasd == 'w':
        game_screen.addstr(hero.y - 1, hero.x, '⬆')
    elif wasd == 'a':
        game_screen.addstr(hero.y, hero.x - 1, '⬅')
    elif wasd == 's':
        game_screen.addstr(hero.y + 1, hero.x, '⬇')
    elif wasd == 'd':
        game_screen.addstr(hero.y, hero.x + 2, '➡')
    # draw_screen(draw_screen(hero, enemies, items, game_screen)

def shoot(hero, enemies, aim_dir, game_screen):
    if hero.inv:
        for enemy in enemies:
            if (aim_dir == 'w' and hero.x == enemy.x and hero.y > enemy.y) or (aim_dir == 'a' and hero.y == enemy.y and hero.x > enemy.x) or (aim_dir == 's' and hero.x == enemy.x and hero.y < enemy.y) or (aim_dir == 'd' and hero.y == enemy.y and hero.x < enemy.x):
                enemy.uni = '☠'
                draw_screen(hero, enemies, items, game_screen)
                time.sleep(1)
                enemies.remove(enemy)




def draw_screen(hero, enemies, items, game_screen):
    game_screen.clear()
    [game_screen.addstr(item.y, item.x, str(item)) for item in items]
    [game_screen.addstr(enemy.y, enemy.x, str(enemy)) for enemy in enemies]
    game_screen.addstr(hero.y, hero.x, str(hero))
    game_screen.addstr(21, 5, f"Inventory: {hero.inv}")

game_screen = curses.initscr()
curses.curs_set(0)

game_screen.keypad(True)
game_screen.clear()

game_screen.addstr(hero.y, hero.x, str(hero))
[game_screen.addstr(item.y, item.x, str(item)) for item in items]
[game_screen.addstr(enemy.y, enemy.x, str(enemy)) for enemy in enemies]
game_screen.addstr(21, 5, f"Inventory: {hero.inv}")

# for enemy in enemies:
#     game_screen.addstr(enemy.y, enemy.x, str(enemy))
print(game_screen.getmaxyx())
while True:
    in_key = game_screen.getkey()
    if in_key == 'q':
        curses.endwin()
        break
    

    if in_key in ['KEY_UP', 'KEY_DOWN', 'KEY_RIGHT', 'KEY_LEFT']:
        for enemy in enemies:
            y_or_x = random.choice(['y', 'x'])
            if y_or_x == 'y':
                enemy.y += random.randrange(-1, 2, 2)
            else:
                y_or_x == 'x'
                enemy.x += random.randrange(-1, 2, 2)
            fix_pos(enemy)
        if in_key == key_list[0]:
            hero.y -= 1
        elif in_key == key_list[1]:
            hero.y += 1
        elif in_key == key_list[2]:
            hero.x += 1
        elif in_key == key_list[3]:
            hero.x -= 1
        fix_pos(hero)
        for item in items:
            if item.y == hero.y and item.x == hero.x:
                hero.inv.append(item)
                items.remove(item)
        # if hero 
        # if in_key 
    if in_key in ['w', 'a', 's', 'd']:
        aim(hero, in_key)
        aim_dir = in_key
        draw_screen(hero, enemies, items, game_screen)
    if in_key == ' ':
        shoot(hero, enemies, aim_dir, game_screen)

    draw_screen(hero, enemies, items, game_screen)
    # game_screen.addstr(21, 31, '')