namespace SpriteKind {
    export const PlayerShot = SpriteKind.create()
    export const LifeBar = SpriteKind.create()
    export const sprite = SpriteKind.create()
}
function moveSpriteInTime (sprite2: Sprite, x: number, y: number, t: number) {
    globalX = x
    globalY = y
    dx = x - sprite2.x
    dy = y - sprite2.y
    sprite2.setVelocity(dx / t, dy / t)
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    controller.moveSprite(mySprite, 50, 50)
    mySprite.setImage(assets.image`
                player_projectile
                `)
    mySprite.z = 1
    small_hitbox = true
    mySprite2 = sprites.create(assets.image`Player`, SpriteKind.sprite)
})
function spell1 () {
    enemyShootAimingPlayer(boss, 90, 5)
}
function moveSpriteRandom (sprite3: Sprite, yLowerBound: number, outerBound: number, v: number) {
    moveSprite(sprite3, randint(outerBound, scene.screenWidth() - outerBound), randint(outerBound, yLowerBound), v)
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    shootBulletFromSprite(mySprite, 200, -90)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite4, otherSprite2) {
    if (!(iframe)) {
        info.changeLifeBy(-1)
        scene.cameraShake(3, 200)
        music.playTone(139, music.beat(BeatFraction.Eighth))
        otherSprite2.destroy()
        iframe = true
        for (let index = 0; index < 5; index++) {
            mySprite.setImage(assets.image`Player_Iframe`)
            pause(50)
            mySprite.setImage(assets.image`Player`)
            pause(50)
        }
        iframe = false
    }
})
function nonSpell1 () {
    while (index2 <= MAX - 1) {
        shootBulletFromSprite(boss, 60, 360 / MAX * index2 + offset)
        index2 += 1
    }
    offset += 13
}
function init_boss (difficulty: number) {
	
}
function spell2 () {
    for (let index3 = 0; index3 <= 4; index3++) {
        shootBulletFromSprite(boss, 60, offset + index3 * 30)
    }
    offset += 23
}
function Spell3 () {
    while (index4 <= MAX - 1) {
        shootBulletFromSprite(boss, 60, 360 / MAX + index4 + offset)
        index4 += 1
    }
}
function init (difficulty: number) {
	
}
function framedMenu () {
    myMenu = miniMenu.createMenu(
    miniMenu.createMenuItem("Modo Rai"),
    miniMenu.createMenuItem("Fácil"),
    miniMenu.createMenuItem("Normal"),
    miniMenu.createMenuItem("Difícil"),
    miniMenu.createMenuItem("Imposible")
    )
    myMenu.setMenuStyleProperty(miniMenu.MenuStyleProperty.Width, 100)
    myMenu.setMenuStyleProperty(miniMenu.MenuStyleProperty.Height, 60)
    myMenu.y = 60
    myMenu.x = 80
    myMenu.setFrame(img`
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
        `)
    myMenu.setStyleProperty(miniMenu.StyleKind.Default, miniMenu.StyleProperty.Background, 6)
    myMenu.setStyleProperty(miniMenu.StyleKind.Default, miniMenu.StyleProperty.Foreground, 1)
    myMenu.onButtonPressed(controller.A, function (selection, selectedIndex) {
        myMenu.close()
        if (selectedIndex == 0) {
            init(0)
        } else if (selectedIndex == 1) {
            init(1)
        } else if (selectedIndex == 2) {
            init(2)
        } else if (selectedIndex == 3) {
            init(3)
        } else if (selectedIndex == 4) {
            init(4)
        }
    })
}
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.PlayerShot, function (sprite22, otherSprite) {
    if (started) {
        info.changeScoreBy(20)
        bossLife += -1
        music.playTone(208, music.beat(BeatFraction.Eighth))
        lifeBarPic.fillRect(bossLife * 2, 0, 96 - bossLife * 2, 5, 15)
        lifeBar.setImage(lifeBarPic)
        if (bossLife <= 0) {
            game.over(true)
        } else if (bossLife % 12 == 0) {
            preSetBossPosition(80, 30)
        }
    }
    otherSprite.destroy()
})
function preSetBossPosition (x2: number, y2: number) {
    started = false
    ready = false
    offset = 0
    moveSpriteInTime(boss, x2, y2, 1)
}
controller.B.onEvent(ControllerButtonEvent.Released, function () {
    controller.moveSprite(mySprite)
    mySprite.setImage(assets.image`Player_Iframe`)
    sprites.destroy(mySprite2)
    small_hitbox = false
})
function moveSpriteRandomFixedTime (sprite5: Sprite, yLowerBound2: number, outerBound2: number, u: number) {
    moveSpriteInTime(sprite5, randint(outerBound2, scene.screenWidth() - outerBound2), randint(outerBound2, yLowerBound2), u)
}
function nonSpell2 () {
    while (index32 <= MAX - 1) {
        shootBulletFromSprite(boss, 60, 360 / MAX * index32 + offset)
        shootBulletFromSprite(boss, 100, 360 / MAX * (index32 + 0.5) + offset)
        index32 += 1
    }
}
function init_player (difficulty: number) {
	
}
function shootBulletFromSprite (sourceSprite: Sprite, speed: number, angle: number) {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, sourceSprite, speed * Math.cos(angle / 57.3), speed * Math.sin(angle / 57.3))
    projectile.setFlag(SpriteFlag.AutoDestroy, true)
    if (sourceSprite.kind() == SpriteKind.Player) {
        projectile.setKind(SpriteKind.PlayerShot)
        projectile.setImage(assets.image`player_bullet`)
    } else {
        projectile.setImage(assets.image`boss_bullet`)
    }
}
function moveSprite (sprite6: Sprite, x3: number, y3: number, w: number) {
    globalX = x3
    globalY = y3
    dx = x3 - sprite6.x
    dy = y3 - sprite6.y
    speed3 = Math.sqrt(dx * dx + dy * dy)
    if (speed3 != 0) {
        sprite6.setVelocity(dx / speed3 * w, dy / speed3 * w)
    }
}
function enemyShootAimingPlayer (sprite7: Sprite, speed2: number, spread: number) {
    shootBulletFromSprite(sprite7, speed2, Math.atan2(mySprite.y - sprite7.y, mySprite.x - sprite7.x) * 57.3 + randint(0 - spread, spread))
}
let lifeBarProgress = 0
let bossProgress = 0
let speed3 = 0
let projectile: Sprite = null
let index32 = 0
let ready = false
let started = false
let myMenu: miniMenu.MenuSprite = null
let index4 = 0
let index2 = 0
let mySprite2: Sprite = null
let dy = 0
let dx = 0
let globalY = 0
let globalX = 0
let MAX = 0
let offset = 0
let lifeBar: Sprite = null
let lifeBarPic: Image = null
let boss: Sprite = null
let bossLife = 0
let mySprite: Sprite = null
let small_hitbox = false
let iframe = false
scene.setBackgroundColor(10)
init(0)
music.setVolume(20)
iframe = false
small_hitbox = false
info.setLife(20)
info.setScore(0)
mySprite = sprites.create(assets.image`Player`, SpriteKind.Player)
mySprite.setPosition(80, 105)
mySprite.setFlag(SpriteFlag.StayInScreen, true)
controller.moveSprite(mySprite)
bossLife = 48
boss = sprites.create(assets.image`Boss`, SpriteKind.Enemy)
boss.setPosition(-16, -16)
lifeBarPic = image.create(96, 5)
lifeBar = sprites.create(lifeBarPic, SpriteKind.LifeBar)
lifeBar.setPosition(80, 5)
lifeBar.setFlag(SpriteFlag.Ghost, true)
offset = 0
MAX = 10
let bossCanMove = true
preSetBossPosition(80, 30)
game.onUpdate(function () {
    if (Math.abs(boss.x - globalX) + Math.abs(boss.y - globalY) <= 2) {
        boss.setVelocity(0, 0)
        if (!(ready)) {
            bossProgress += 1
            if (bossProgress == 2) {
                bossCanMove = false
            } else {
                if (bossProgress == 2) {
                    MAX = 8
                }
                bossCanMove = true
            }
        }
        ready = true
    }
    if (small_hitbox) {
        mySprite2.setPosition(mySprite.x, mySprite.y)
    }
})
game.onUpdateInterval(750, function () {
    if (started) {
        if (bossProgress == 3) {
            nonSpell2()
        }
    }
})
game.onUpdateInterval(2500, function () {
    if (started && bossCanMove) {
        moveSpriteRandom(boss, 40, 8, 60)
    }
})
game.onUpdateInterval(150, function () {
    if (started) {
        if (bossProgress == 2) {
            spell1()
        } else if (bossProgress == 4) {
            spell2()
        }
    }
})
game.onUpdateInterval(500, function () {
    if (started) {
        if (bossProgress == 1) {
            Spell3()
        }
    }
})
game.onUpdateInterval(100, function () {
    if (ready && !(started)) {
        if (lifeBarProgress < 4) {
            lifeBarPic.fillRect(24 * lifeBarProgress, 0, 24, 5, 14 - lifeBarProgress % 2 * 6)
            lifeBarPic.fillRect(24 * lifeBarProgress, 1, 24, 3, lifeBarProgress % 2 * 5 + 4)
            lifeBar.setImage(lifeBarPic)
            lifeBarProgress += 1
        } else {
            started = true
        }
    }
})
