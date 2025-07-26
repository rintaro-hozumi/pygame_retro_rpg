import pygame, data, map, hero, img
from data import U, W, H, COL_W, COL_BT

def render():
    # オフセット位置の計算
    origin_x = (W - U) // 2     # 原点X
    origin_y = (H - U) // 2     # 原点Y
    hero_x = hero.x * U         # 自キャラX
    hero_y = hero.y * U         # 自キャラY
    move_x = (hero.x - hero.next_x) * hero.move_rate * U    # 移動途中X
    move_y = (hero.y - hero.next_y) * hero.move_rate * U    # 移動途中Y
    offset_x = int(origin_x - hero_x + move_x)  # オフセットX
    offset_y = int(origin_y - hero_y + move_y)  # オフセットY

    # マップの描画
    for y in range(map.h):
        for x in range(map.w):
            # 描画位置
            dx = x * U + offset_x   # 描画X位置
            dy = y * U + offset_y   # 描画Y位置

            # 画面外なら飛ばす
            if dx + U < 0: continue     # 描画X位置＋描画単位が0未満なら
            if dx >= W:    continue     # 描画X位置が横幅以上なら
            if dy + U < 0: continue     # 描画Y位置＋描画単位が0未満なら
            if dy >= H:    continue     # 描画Y位置が高さ以上なら

            # 土地の種類を得て、対応する画像を描画
            land = map.data[x + y * map.w]
            data.screen.blit(img.land[land], (dx, dy))

    # キャラクターの描画
    time = pygame.time.get_ticks()      # ゲーム開始からの経過時間
    ref = hero.iref + time // 250 % 2   # 画像参照位置
    data.screen.blit(img.chara[ref], (origin_x, origin_y))  # 画像描画

    # ステータスの描画
    text = f" hp:{hero.hp}/{hero.hp_max} hp:{hero.mp}/{hero.mp_max} " \
         + f"AT:{hero.at} DF:{hero.df} EXP:{hero.exp} LV:{hero.level} "
    img.font.render_to(data.screen, (U // 2, U // 2), text, COL_W, COL_BT)  # 文字描画
