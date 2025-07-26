import pygame, data, img
from data import U, W, H, COL_W, COL_G

def show(text):
    # 土台描画
    rect = (U, U, W - U * 2, H - U * 2)
    pygame.draw.rect(data.screen, COL_G, rect)  # 四角形塗りつぶし

    # 文字描画
    fsz = img.fsz * 2    # フォント サイズ
    texts = text.splitlines()   # 改行でリストに分割
    y = (H - fsz * len(texts)) // 2 # 行開始位置
    for line in texts:
        rect = img.font.get_rect(line, size=fsz)    # 描画四角形取得
        x = (W - rect.w) // 2       # 中央揃え
        img.font.render_to(data.screen, (x, y), line, COL_W, size=fsz)  # 文字描画
        y += fsz    # 行位置更新

    # 画面の反映と待機
    pygame.display.flip()   # 画面フリップ
    pygame.time.wait(1200)  # 待機
    pygame.event.get()      # イベントの消費
