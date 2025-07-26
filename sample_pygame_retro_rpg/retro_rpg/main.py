import pygame, data

pygame.init()   # Pygameを初期化
data.screen = pygame.display.set_mode((data.W, data.H)) # 画面作成

import s_title.main, s_map.main, s_battle.main

# ゲームループ
running = True  # 実行継続フラグ
while running:
    # キーの受け付け
    data.key = {"down": None, "keep": pygame.key.get_pressed()}
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:    # キー押し下げ
            data.key["down"] = event.key    # キー種類

    pygame.display.update()     # 画面を更新
    data.screen.fill((0, 0, 0)) # 画面を塗りつぶす

    # シーン変更
    if data.scene != data.scene_next:
        data.scene = data.scene_next    # シーン変更
        if data.scene == "title":
            s_title.main.init()     # タイトル初期化
        if data.scene == "map":
            s_map.main.init()       # マップ初期化
        if data.scene == "battle":
            s_battle.main.init()    # バトル初期化

    # シーン更新
    if data.scene == "title":
        s_title.main.update()   # タイトル更新
    if data.scene == "map":
        s_map.main.update()     # マップ更新
    if data.scene == "battle":
        s_battle.main.update()  # バトル更新

    pygame.display.flip()   # 画面フリップ

# 終了
pygame.quit()
