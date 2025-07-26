import pygame, data
from . import proc_hero, proc_enemy

# 進行管理
def manage():
    if data.proc == "menu":
        if data.key["down"] == pygame.K_SPACE:
            # メニュー決定
            proc_hero.start()   # 自開始
        elif data.key["down"] == pygame.K_DOWN:
            # メニュー下移動
            data.menu_sel += 1
            if data.menu_sel >= len(data.menu_texts):
                data.menu_sel = 0
        elif data.key["down"] == pygame.K_UP:
            # メニュー上移動
            data.menu_sel -= 1
            if data.menu_sel < 0:
                data.menu_sel = len(data.menu_texts) - 1
    elif data.proc == "hero_draw":
        proc_hero.draw()    # 自描画
    elif data.proc == "enemy_start":
        proc_enemy.start()  # 敵開始
    elif data.proc == "enemy_draw":
        proc_enemy.draw()   # 敵描画
