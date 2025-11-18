import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))



def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_img = pg.transform.rotozoom(kk_img,10,1.0)

    bg_x = 0
    speed = 5

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        #背景を左に流す
        bg_x -= speed
        if bg_x <= -800:  # 背景画像の幅分ずれたらリセット
            bg_x = 0
        #背景を二枚準備
        screen.blit(bg_img, [bg_x, 0])
        #残像の補正
        screen.blit(bg_img, [bg_x + 800, 0])
        #こうかとんを表示
        screen.blit(kk_img, [300, 200]) 

        pg.display.update()
        tmr += 1        
        clock.tick(200)
        




if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()