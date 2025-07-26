import random, data, map, hero, enemy, dialog

last_x = -1     # 最終X位置
last_y = -1     # 最終Y位置

# 初期化
def init():
    global last_x, last_y   # 代入可能に
    last_x = hero.x     # 自キャラX位置に設定
    last_y = hero.y     # 自キャラY位置に設定

# イベント発生判定
def check():
    # 同じマスで連続発生する対策
    global last_x, last_y   # 代入可能に
    if last_x == hero.x and last_y == hero.y:
        return False    # 位置が同じなら処理を終了
    last_x = hero.x     # 最終X位置を更新
    last_y = hero.y     # 最終Y位置を更新

    # 土地
    land = map.data[hero.x + hero.y * map.w]    # リストの参照位置
    if land == map.TOWN:
        # 現在の土地が街である
        hero.hp = hero.hp_max   # HP回復
        hero.mp = hero.mp_max   # MP回復
        dialog.show("街に到着しました\n休息しました")   # ダイアログ表示
        return True     # イベントありで終了

    # 敵遭遇判定
    for i, e in enumerate(enemy.ENEMIES):
        name, rate, eland = e[0:3]  # 敵データ抜き出し
        if eland != land: continue  # 土地が違う
        if random.randrange(rate) != 0: continue    # 1/rateの確率で0になる

        # モンスター遭遇
        enemy.set(i)    # 敵の設定
        dialog.show(f"{name}との\n戦闘を開始！")    # ダイアログ表示
        data.scene_next = "battle"  # シーン変更
        return True # イベントありで終了
    return False    # イベントなしで終了
