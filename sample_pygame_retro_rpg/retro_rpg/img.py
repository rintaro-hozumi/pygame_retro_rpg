import pygame, pygame.freetype, data

# 画像分割
def load(p):
    image = pygame.image.load(p)    # 画像読み込み
    w, h = image.get_size()         # 横幅、高さ取得
    unit = 16       # 画像ピクセル単位
    images = []     # 画像リスト
    for y in range(0, h, unit):
        for x in range(0, w, unit):
            # 1枚分のSurfaceを生成して貼り付ける
            piece = pygame.Surface((unit, unit), pygame.SRCALPHA)
            piece.blit(image, (0, 0), (x, y, unit, unit))

            # 拡大して画像リストに追加
            piece = pygame.transform.scale(piece, (data.U, data.U))
            images.append(piece)
    return images

chara = load("image/chara.png") # キャラクター
land  = load("image/land.png")  # 土地

fsz = 36    # フォント デフォルト サイズ
font = pygame.freetype.Font("font/PixelMplus12-Regular.ttf", fsz)   # フォント

