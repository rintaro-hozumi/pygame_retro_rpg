import data, enemy, audio
from . import proc, draw

# 初期化
def init():
    data.proc = "menu"  # 進行
    data.menu_sel = 0   # メニュー選択位置
    if enemy.boss:
        audio.play(audio.BATTLE_LAST)   # ラスボス戦闘BGM再生
    else:
        audio.play(audio.BATTLE)    # 通常戦闘BGM再生

# 更新
def update():
    draw.render()   # 描画
    proc.manage()   # 進行管理
