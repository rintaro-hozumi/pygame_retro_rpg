import map

# 敵
name = ""   # 名前
rate = 0    # 出現頻度
land = 0    # 土地
iref = 0    # 画像参照
hp = 0      # HP
hp_max = 0  # HP最大値
at = 0      # 攻撃力
df = 0      # 防御力
exp = 0     # 経験値
boss = False    # ボス

ENEMIES = (
    # 名前   出現頻度   土地   画像参照 HP 最大 攻撃 防御 EXP ボス
    ("ゴブリン", 15, map.PLAIN,    2,   40,  40, 20,  5, 30, False),
    ("エルフ",   10, map.FOLEST,   4,   60,  60, 30, 10, 50, False),
    ("ロック",   5,  map.MOUNTAIN, 6,  200, 200, 40, 30, 80, False),
    ("魔王",     1,  map.CASTLE,   8,  999, 999, 99, 99, 99, True)
)

# 敵の設定
def set(i):
    global name, rate, land, iref, hp, hp_max, at, df, exp, boss    # 代入可能に
    name, rate, land, iref, hp, hp_max, at, df, exp, boss = ENEMIES[i]

set(0)  # 仮設定
