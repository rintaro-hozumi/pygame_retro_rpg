import pygame, data, map, hero
from . import event

MOVE_CYCLE = 250    # 移動サイクル
last_move = -1      # 最終移動時間

# 移動管理
def manage():
    global last_move    # 代入可能に
    time = pygame.time.get_ticks()  # ゲーム開始からの経過時間
    if time < last_move + MOVE_CYCLE:   # 移動サイクルを経過したか判定
        # 移動中処理
        hero.move_rate = (time - last_move) / MOVE_CYCLE    # 移動比率を更新
    else:
        # 到着処理
        last_move = time        # 最終移動時間を更新
        hero.move_rate = 0      # 移動比率を初期化
        hero.x = hero.next_x    # 到着でX位置を反映
        hero.y = hero.next_y    # 到着でY位置を反映
        if event.check() == False:  # イベント発生判定
            next()  # 次回移動処理

# 次回移動処理
def next():
    x = hero.x  # 仮のX位置
    y = hero.y  # 仮のY位置
    if data.key["keep"][pygame.K_LEFT ]: x -= 1     # 左ならXを1減らす
    if data.key["keep"][pygame.K_RIGHT]: x += 1     # 右ならXを1増やす
    if data.key["keep"][pygame.K_UP]:    y -= 1     # 上ならYを1減らす
    if data.key["keep"][pygame.K_DOWN]:  y += 1     # 下ならYを1増やす

    # マップの範囲外なら終了
    if x < 0:      return   # xが0未満
    if x >= map.w: return   # xがマップの横幅以上
    if y < 0:      return   # yが0未満
    if y >= map.h: return   # yがマップの高さ以上

    # 移動先が水なら終了
    if map.data[x + y * map.w] == map.WATER: return

    # 次回XY位置を更新
    hero.next_x = x     # 次回X位置
    hero.next_y = y     # 次回Y位置
