import pygame

# システム
U = 16 * 3      # 描画単位
W = 20 * U      # 横幅
H = 15 * U      # 高さ
screen = pygame.Surface((0, 0))     # スクリーン
key = {"down": None, "keep": {}}    # キー

# シーン  title, map, battle
scene = ""              # シーン
scene_next = "title"    # 次回更新

# 色
COL_B = (0, 0, 0)           # 黒
COL_BT = (0, 0, 0, 128)     # 黒半透明
COL_W = (255, 255, 255)     # 白
COL_G = (64, 64, 64)        # 灰

# 戦闘
proc = "menu"   # 進行  menu, hero_draw, enemy_start, enemy_draw
menu_texts = ["SWORD", "MAGIC", "ESCAPE"]   # メニュー文字列
menu_sel = 0    # メニュー選択位置
ef_hero = False     # エフェクト自
ef_enemy = False    # エフェクト敵
ef_time_start = 0   # エフェクト開始時間
