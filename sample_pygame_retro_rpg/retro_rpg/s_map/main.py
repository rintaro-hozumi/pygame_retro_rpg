import audio
from . import draw, move, event

# 初期化
def init():
    event.init()    # イベント初期化
    audio.play(audio.FIELD) # BGM再生

# 更新
def update():
    draw.render()   # 描画
    move.manage()   # 移動管理
