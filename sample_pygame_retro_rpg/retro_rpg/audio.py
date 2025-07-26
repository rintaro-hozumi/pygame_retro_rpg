from pygame.mixer import Sound, music

FIELD       = "audio/bgm/maou_bgm_8bit01.mp3"   # 野原
BATTLE      = "audio/bgm/maou_bgm_8bit18.mp3"   # 戦闘
LOSE        = "audio/bgm/maou_bgm_8bit20.mp3"   # 敗北
ENDING      = "audio/bgm/maou_bgm_8bit22.mp3"   # エンディング
WIN         = "audio/bgm/maou_bgm_8bit24.mp3"   # 勝利
BATTLE_LAST = "audio/bgm/maou_bgm_8bit25.mp3"   # 最終戦闘

# BGM再生
def play(p):
    music.load(p)   # ロード
    music.play(-1)  # 繰り返し(-1)で再生

damage = Sound("audio/se/maou_se_8bit22.wav")   # ダメージ
