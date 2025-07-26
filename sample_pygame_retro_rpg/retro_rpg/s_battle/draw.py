import pygame, data, hero, enemy, img
from data import U, W, H, COL_W, COL_G

RECT_HERO  = pygame.Rect(U,      U, W // 2 - U, H // 2 + U)     # 領域自
RECT_ENEMY = pygame.Rect(W // 2, U, W // 2 - U, H // 2 + U)     # 領域敵
RECT_MENU  = pygame.Rect(U, H // 2 + U * 2, W - U * 2, H // 2 - U * 3)  # 領域メニュー

# 描画
def render():
    t_hero = f"HP:{hero.hp}/{hero.hp_max} MP:{hero.mp}/{hero.mp_max}"   # ステータス自
    t_enemy = f"{enemy.name}　HP:{enemy.hp}/{enemy.hp_max}"             # ステータス敵
    render_stat(RECT_HERO,  t_hero)     # ステータスの描画
    render_stat(RECT_ENEMY, t_enemy)    # ステータスの描画
    render_char(RECT_HERO,  hero.iref,  data.ef_hero)   # キャラクターの描画
    render_char(RECT_ENEMY, enemy.iref, data.ef_enemy)  # キャラクターの描画
    render_menu()   # メニューの描画
    render_frame()  # 枠の描画

# ステータスの描画
def render_stat(rect, text):
    # 文字
    size = img.font.get_rect(text)  # 描画領域四角形
    x = rect.x + rect.w / 2 - size.w / 2    # 中央になるX位置
    y = rect.y + U * 0.5    # Y位置
    img.font.render_to(data.screen, (x, y), text, COL_W)    # 文字描画

# キャラクターの描画
def render_char(rect, iref, is_ef):
    # 拡大画像準備
    time = pygame.time.get_ticks()  # ゲーム開始からの経過時間
    ref = iref + time // 500 % 2    # 画像参照位置
    image = pygame.transform.scale(img.chara[ref], (U * 6, U * 6))  # 拡大画像

    # キャラ画像の描画
    x = rect.x + U * 1.5    # キャラX位置
    y = rect.y + U * 2      # キャラY位置
    if is_ef:   # 演出の有無
        pygame.draw.rect(data.screen, (255, 0, 0), rect)    # 背景塗りつぶし
        data.screen.blit(image, (x, y))     # キャラ画像描画

        # 50ミリ秒ごとにガタガタと揺らす
        x += - U // 2 + int(U * (time // 50 * 11 % 13 / 13))    # X位置修正
        y += - U // 2 + int(U * (time // 50 * 11 % 17 / 17))    # Y位置修正
    data.screen.blit(image, (x, y))     # キャラ画像描画

# メニューの描画
def render_menu():
    line_h = img.fsz * 1.25     # 行の高さ
    for i, text in enumerate(data.menu_texts):
        size = img.font.get_rect(text)  # 描画領域四角形
        x = RECT_MENU.x + RECT_MENU.w / 2 - size.w / 2  # 中央になるX位置
        y = RECT_MENU.y + U * 0.75 + line_h * i     # Y位置
        if i == data.menu_sel:
            # 選択メッセージ背景
            rect = (RECT_MENU.x, y - img.fsz * 0.25, RECT_MENU.w, line_h) # 背景の四角形
            pygame.draw.rect(data.screen, COL_G, rect)      # 四角形の塗りつぶし
        img.font.render_to(data.screen, (x, y), text, COL_W)    # 文字描画

# 枠の描画
def render_frame():
    line_w = U // 8     # 線の太さ
    pygame.draw.rect(data.screen, COL_W, RECT_HERO, line_w)     # 自
    pygame.draw.rect(data.screen, COL_W, RECT_ENEMY, line_w)    # 敵
    pygame.draw.rect(data.screen, COL_W, RECT_MENU, line_w)     # メニュー
