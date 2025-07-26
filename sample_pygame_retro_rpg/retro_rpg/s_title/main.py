import pygame, data, img, audio
from data import U, COL_W

def init():
    audio.play(audio.FIELD)     # BGM再生

# 更新
def update():
    # 文字描画
    img.font.render_to(data.screen, (U, U), "ZineQuest", COL_W, size = img.fsz * 5.5)
    img.font.render_to(data.screen, (U * 6, U * 11), "   PRESS SPACE KEY   ", COL_W)
    img.font.render_to(data.screen, (U * 6, U * 12), "Key: ↑ ← ↓ → Space", COL_W)
    img.font.render_to(data.screen, (U * 6, U * 13), "(c)2024 Masakazu Yanai", COL_W)

    # 画像描画
    image = pygame.transform.scale(img.chara[0], (U * 4, U * 4))    # 拡大画像生成
    data.screen.blit(image, (U * 8, U * 6)) # 画像描画

    # SPACEキー押し下げでマップに移動
    if data.key["down"] == pygame.K_SPACE:
        data.scene_next = "map"
