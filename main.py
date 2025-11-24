@namespace
class SpriteKind:
    PlayerShot = SpriteKind.create()
    LifeBar = SpriteKind.create()
    sprite = SpriteKind.create()
def moveSpriteInTime(sprite2: Sprite, x: number, y: number, t: number):
    global globalX, globalY, dx, dy
    globalX = x
    globalY = y
    dx = x - sprite2.x
    dy = y - sprite2.y
    sprite2.set_velocity(dx / t, dy / t)

def on_b_pressed():
    global small_hitbox, mySprite2
    controller.move_sprite(mySprite, 50, 50)
    mySprite.set_image(assets.image("""
        player_projectile
        """))
    mySprite.z = 1
    small_hitbox = True
    mySprite2 = sprites.create(assets.image("""
        Player
        """), SpriteKind.sprite)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def spell1():
    enemyShootAimingPlayer(boss, 90, 5)
def moveSpriteRandom(sprite3: Sprite, yLowerBound: number, outerBound: number, v: number):
    moveSprite(sprite3,
        randint(outerBound, scene.screen_width() - outerBound),
        randint(outerBound, yLowerBound),
        v)

def on_a_pressed():
    shootBulletFromSprite(mySprite, 200, -90)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite4, otherSprite2):
    global iframe
    if not (iframe):
        info.change_life_by(-1)
        scene.camera_shake(3, 200)
        music.play_tone(139, music.beat(BeatFraction.EIGHTH))
        otherSprite2.destroy()
        iframe = True
        for index in range(5):
            mySprite.set_image(assets.image("""
                Player_Iframe
                """))
            pause(50)
            mySprite.set_image(assets.image("""
                Player
                """))
            pause(50)
        iframe = False
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

def nonSpell1():
    global index2, offset
    while index2 <= MAX - 1:
        shootBulletFromSprite(boss, 60, 360 / MAX * index2 + offset)
        index2 += 1
    offset += 13
def init_boss(difficulty: number):
    global bossLife, boss, lifeBarPic, lifeBar, offset, MAX, bossCanMove
    bossLife = 48
    boss = sprites.create(assets.image("""
        Boss
        """), SpriteKind.enemy)
    boss.set_position(-16, -16)
    lifeBarPic = image.create(96, 5)
    lifeBar = sprites.create(lifeBarPic, SpriteKind.LifeBar)
    lifeBar.set_position(80, 5)
    lifeBar.set_flag(SpriteFlag.GHOST, True)
    offset = 0
    MAX = 10
    bossCanMove = True
    preSetBossPosition(80, 30)
def spell2():
    global offset
    for index3 in range(5):
        shootBulletFromSprite(boss, 60, offset + index3 * 30)
    offset += 23
def Spell3():
    global index4
    while index4 <= MAX - 1:
        shootBulletFromSprite(boss, 60, 360 / MAX + index4 + offset)
        index4 += 1
def init(difficulty: number):
    music.set_volume(20)
def framedMenu():
    global myMenu
    myMenu = miniMenu.create_menu(miniMenu.create_menu_item("Modo Rai"),
        miniMenu.create_menu_item("Fácil"),
        miniMenu.create_menu_item("Normal"),
        miniMenu.create_menu_item("Difícil"),
        miniMenu.create_menu_item("Imposible"))
    myMenu.set_menu_style_property(miniMenu.MenuStyleProperty.WIDTH, 100)
    myMenu.set_menu_style_property(miniMenu.MenuStyleProperty.HEIGHT, 60)
    myMenu.y = 60
    myMenu.x = 80
    myMenu.set_frame(img("""
        88888..8888888888888888....88888.
        87768888777877787778777888867778.
        87777686767876767678767688777778.
        87767767667676676676766786776768.
        8677676767767767677677678676778..
        .877768777686767776867678667768..
        .886668888888888888888888886688..
        .888888866666666666666668877768..
        88677786666666666666666668766778.
        87766686666666666666666668776678.
        87667786666666666666666668677778.
        87777686666666666666666668866888.
        88866886666666666666666668677778.
        87777686666666666666666668776678.
        87667786666666666666666668666778.
        87766786666666666666666668777688.
        88677786666666666666666668766778.
        87766686666666666666666668776678.
        87667786666666666666666668677778.
        87777686666666666666666668866888.
        88866886666666666666666668677778.
        87777686666666666666666668776678.
        87667786666666666666666668666778.
        87766786666666666666666668777688.
        .867778866666666666666668888888..
        .886688888888888888888888866688..
        .867766876768677767686777867778..
        .8776768767767767677677676767768.
        86767768766767667667676676776778.
        87777788676787676767876768677778.
        87776888877787778777877788886778.
        88888..88888888888888888....8888.
        .................................
        """))
    myMenu.set_style_property(miniMenu.StyleKind.DEFAULT,
        miniMenu.StyleProperty.BACKGROUND,
        6)
    myMenu.set_style_property(miniMenu.StyleKind.DEFAULT,
        miniMenu.StyleProperty.FOREGROUND,
        1)
    
    def on_button_pressed(selection, selectedIndex):
        myMenu.close()
        if selectedIndex == 0:
            pass
        elif selectedIndex == 1:
            pass
        elif selectedIndex == 2:
            pass
        elif selectedIndex == 3:
            pass
        elif selectedIndex == 4:
            pass
    myMenu.on_button_pressed(controller.A, on_button_pressed)
    

def on_on_overlap2(sprite22, otherSprite):
    global bossLife
    if started:
        info.change_score_by(20)
        bossLife += -1
        music.play_tone(208, music.beat(BeatFraction.EIGHTH))
        lifeBarPic.fill_rect(bossLife * 2, 0, 96 - bossLife * 2, 5, 15)
        lifeBar.set_image(lifeBarPic)
        if bossLife <= 0:
            game.over(True)
        elif bossLife % 12 == 0:
            preSetBossPosition(80, 30)
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.enemy, SpriteKind.PlayerShot, on_on_overlap2)

def preSetBossPosition(x2: number, y2: number):
    global started, ready, offset
    started = False
    ready = False
    offset = 0
    moveSpriteInTime(boss, x2, y2, 1)

def on_b_released():
    global small_hitbox
    controller.move_sprite(mySprite)
    mySprite.set_image(assets.image("""
        Player_Iframe
        """))
    sprites.destroy(mySprite2)
    small_hitbox = False
controller.B.on_event(ControllerButtonEvent.RELEASED, on_b_released)

def moveSpriteRandomFixedTime(sprite5: Sprite, yLowerBound2: number, outerBound2: number, u: number):
    moveSpriteInTime(sprite5,
        randint(outerBound2, scene.screen_width() - outerBound2),
        randint(outerBound2, yLowerBound2),
        u)
def nonSpell2():
    global index32
    while index32 <= MAX - 1:
        shootBulletFromSprite(boss, 60, 360 / MAX * index32 + offset)
        shootBulletFromSprite(boss, 100, 360 / MAX * (index32 + 0.5) + offset)
        index32 += 1
def init_player(difficulty: number):
    global mySprite, iframe, small_hitbox
    info.set_life(20)
    info.set_score(0)
    mySprite = sprites.create(assets.image("""
        Player
        """), SpriteKind.player)
    mySprite.set_position(80, 105)
    mySprite.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
    controller.move_sprite(mySprite)
    iframe = False
    small_hitbox = False
def shootBulletFromSprite(sourceSprite: Sprite, speed: number, angle: number):
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        sourceSprite,
        speed * Math.cos(angle / 57.3),
        speed * Math.sin(angle / 57.3))
    projectile.set_flag(SpriteFlag.AUTO_DESTROY, True)
    if sourceSprite.kind() == SpriteKind.player:
        projectile.set_kind(SpriteKind.PlayerShot)
        projectile.set_image(assets.image("""
            player_bullet
            """))
    else:
        projectile.set_image(assets.image("""
            boss_bullet
            """))
def moveSprite(sprite6: Sprite, x3: number, y3: number, w: number):
    global globalX, globalY, dx, dy, speed3
    globalX = x3
    globalY = y3
    dx = x3 - sprite6.x
    dy = y3 - sprite6.y
    speed3 = Math.sqrt(dx * dx + dy * dy)
    if speed3 != 0:
        sprite6.set_velocity(dx / speed3 * w, dy / speed3 * w)
def enemyShootAimingPlayer(sprite7: Sprite, speed2: number, spread: number):
    shootBulletFromSprite(sprite7,
        speed2,
        Math.atan2(mySprite.y - sprite7.y, mySprite.x - sprite7.x) * 57.3 + randint(0 - spread, spread))
lifeBarProgress = 0
bossProgress = 0
speed3 = 0
projectile: Sprite = None
index32 = 0
ready = False
started = False
myMenu: miniMenu.MenuSprite = None
index4 = 0
bossCanMove = False
lifeBar: Sprite = None
lifeBarPic: Image = None
bossLife = 0
offset = 0
MAX = 0
index2 = 0
iframe = False
boss: Sprite = None
mySprite2: Sprite = None
small_hitbox = False
mySprite: Sprite = None
dy = 0
dx = 0
globalY = 0
globalX = 0
difficulty = 0
scene.set_background_color(10)
framedMenu()

def on_on_update():
    global bossProgress, bossCanMove, MAX, ready
    if abs(boss.x - globalX) + abs(boss.y - globalY) <= 2:
        boss.set_velocity(0, 0)
        if not (ready):
            bossProgress += 1
            if bossProgress == 2:
                bossCanMove = False
            else:
                if bossProgress == 2:
                    MAX = 8
                bossCanMove = True
        ready = True
    if small_hitbox:
        mySprite2.set_position(mySprite.x, mySprite.y)
game.on_update(on_on_update)

def on_update_interval():
    if started:
        if bossProgress == 3:
            nonSpell2()
game.on_update_interval(750, on_update_interval)

def on_update_interval2():
    if started and bossCanMove:
        moveSpriteRandom(boss, 40, 8, 60)
game.on_update_interval(2500, on_update_interval2)

def on_update_interval3():
    if started:
        if bossProgress == 2:
            spell1()
        elif bossProgress == 4:
            spell2()
game.on_update_interval(150, on_update_interval3)

def on_update_interval4():
    if started:
        if bossProgress == 1:
            Spell3()
game.on_update_interval(500, on_update_interval4)

def on_update_interval5():
    global lifeBarProgress, started
    if ready and not (started):
        if lifeBarProgress < 4:
            lifeBarPic.fill_rect(24 * lifeBarProgress, 0, 24, 5, 14 - lifeBarProgress % 2 * 6)
            lifeBarPic.fill_rect(24 * lifeBarProgress, 1, 24, 3, lifeBarProgress % 2 * 5 + 4)
            lifeBar.set_image(lifeBarPic)
            lifeBarProgress += 1
        else:
            started = True
game.on_update_interval(100, on_update_interval5)
