# 主人公
start_x = 4     # 開始X位置
start_y = 3     # 開始Y位置
x = start_x     # X位置
y = start_y     # Y位置
next_x = x      # 次回X位置
next_y = y      # 次回Y位置
move_rate = 0.0 # 移動到達比率
hp = 100        # HP
hp_max = 100    # HP最大値
mp = 4          # MP
mp_max = 4      # MP最大値
at = 10         # 攻撃力
df = 10         # 防御力
exp = 0         # 経験値
level = 1       # レベル
iref = 0        # 画像参照

# 経験値獲得
def add_exp(n):
    global exp, level, hp   # 代入可能に
    exp = min(exp + n, 999)     # 経験値獲得
    level_tmp = 1 + exp // 50   # レベル計算
    if level != level_tmp:  # レベルが更新されているか確認
        # レベルアップ
        level = level_tmp   # レベル反映
        calc()          # 能力値の計算
        hp = hp_max     # HPのみ回復
        return True     # レベルアップあり
    return False    # レベルアップなし

# 能力値の計算
def calc():
    global hp_max, mp_max, at, df   # 代入可能に
    hp_max = 100 + (level - 1) * 50 # HP最大値
    mp_max = 4 + (level - 1) * 2    # MP最大値
    at = 10 + (level - 1) * 5       # 攻撃力
    df = 10 + (level - 1) * 5       # 防御力
