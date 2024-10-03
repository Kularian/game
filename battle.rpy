##Battle Script Probably##

init python:
    class character:
        def __init__(self, name, level = 1, max_hp=0, hp=0, max_sp=0, sp=0, str = 9, vit = 9, mag = 8, agi = 8, luc = 8, weapon = "Sword", attack = 0):
            self.name = name
            self.level = 5
            self.max_hp = 5*(level+vit)
            self.hp = 5*(level+vit)
            self.max_sp = 5*(level+mag)
            self.sp = 5*(level+mag)
            self.str = str
            self.vit = vit
            self.mag = mag
            self.agi = agi
            self.luc = luc
            self.weapon = weapon
            self.attack = attack

    class demon:
        def __init__(self, name, max_hp=10, hp=10, max_sp=5, sp=5, str=5, vit=5, mag=5, agi=5, luc=5):
            self.name = name
            self.max_hp = max_hp
            self.hp = hp
            self.max_sp = max_sp
            self.sp = sp
            str = str
            vit = vit
            mag = mag
            agi = agi
            luc = luc

label placements:
    transform char1:
        xpos 500
        ypos 580

    transform char2:
        xpos 630
        ypos 620

    transform char3:
        xpos 750
        ypos 660

    transform char4:
        xpos 890
        ypos 700

    transform enemy1:
        xpos 1000
        ypos 460

    transform enemy2:
        xpos 1100
        ypos 500

    transform enemy3:
        xpos 1200
        ypos 540

    transform enemy4:
        xpos 1300
        ypos 580

label battlers:
    $ naoya = character("Naoya")
    $ nanjo = character("Nanjo", 5, 8, 12, 7, 7, 5)
    $ mark = character("Mark", 5, 11, 8, 5, 8, 7)
    $ yukino = character("Yukino", 5, 9, 7, 8, 10, 5)
    $ mrzombie = demon("Mr. Zombie")

image mrzombie idle:
    "images/Battlers/MrZombie/MrZombieIdle1.png"
    pause 1.5
    "images/Battlers/MrZombie/MrZombieIdle2.png"
    pause 1.5
    "images/Battlers/MrZombie/MrZombieIdle3.png"
    pause 0.5
    "images/Battlers/MrZombie/MrZombieIdle4.png"
    pause 0.5
    "images/Battlers/MrZombie/MrZombieIdle3.png"
    pause 1.5
    "images/Battlers/MrZombie/MrZombieIdle2.png"
    pause 1.5
    repeat

image bg testbattle = "images/Battlers/BattleBG/BattleBG.png"

image naoya idle = "images/Battlers/Naoya/idle.png"
image nanjo idle = "images/Battlers/Nanjo/Idle.png"
image mark idle = "images/Battlers/Mark/Idle.png"
image yukino idle = "images/Battlers/Yukino/Idle.png"

label battle:
    show bg testbattle with dissolve
    show naoya idle at char4
    show nanjo idle at char2
    show mark idle at char3
    show yukino idle at char1
    show mrzombie idle at enemy2
    show mrzombie idle as mrzombie2 at enemy1
    show mrzombie idle as mrzombie3 at enemy3
    show mrzombie idle as mrzombie4 at enemy4
    with dissolve

    window hide
    pause
