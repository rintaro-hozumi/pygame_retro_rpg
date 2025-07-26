import pygame, data, hero, enemy, dialog, audio
from random import randrange

# 開始
def start():
    action = data.menu_texts[data.menu_sel]     # 選択行動取得

    # 逃走
    if action == "ESCAPE":  # 選択行動が ESCAPE の場合
        if randrange(2) == 0:   # 1/2の確率
            dialog.show("逃げるのに\n成功しました") # ダイアログ表示
            data.scene_next = "map"     # シーンをマップに
        else:
            dialog.show("逃げるのに\n失敗しました") # ダイアログ表示
            data.proc = "enemy_start"   # 進行を敵開始に
        return  # 処理を打ち切る

    # 通常攻撃
    at = randrange(hero.at // 2, hero.at)   # 半分以上、1倍未満

    # 魔法
    if action == "MAGIC":   # 選択行動が MAGIC の場合
        if hero.mp == 0:    # MPが0
            dialog.show("MPが足りません")   # ダイアログ表示
            return  # 処理を打ち切る
        at = randrange(hero.at * 2, hero.at * 4)    # 2倍以上、4倍未満
        hero.mp -= 1

    # ダメージ適用
    df = randrange(enemy.df)    # 0以上、1倍未満
    damage = max(1, at - df)    # ダメージ（最小1）
    enemy.hp = max(0, enemy.hp - damage)    # HP減少（HPの最低値は0）

    # 演出と進行
    audio.damage.play()     # ダメージSE再生
    data.ef_enemy = True    # 敵演出ありに
    data.ef_time_start = pygame.time.get_ticks()    # 演出開始時間記録
    data.proc = "hero_draw" # 進行を自描画に

# 描画
def draw():
    time = pygame.time.get_ticks()  # ゲーム開始からの経過時間
    if time >= data.ef_time_start + 500:    # 500ミリ秒以上経過したか
        data.ef_enemy = False   # 敵演出なしに
        end()   # 終了

# 終了
def end():
    data.proc = "enemy_start"   # 進行を敵開始に
    if enemy.hp == 0:   # HPが0か確認
        if enemy.boss:  # ラスボスか確認
            # ラスボス時はエンディング
            audio.play(audio.ENDING)    # エンディングのBGM再生
            dialog.show(f"{enemy.name}を\n倒しました")  # ダイアログ表示
            dialog.show("あなたは王国を\n救いました")   # ダイアログ表示
            dialog.show("Congratulations!") # ダイアログ表示
            data.scene_next = "title"       # シーンをタイトルに
        else:
            audio.play(audio.WIN)   # 勝利のBGM再生
            dialog.show(f"{enemy.name}を\n倒しました")  # ダイアログ表示
            mes = f"経験値 {enemy.exp} 獲得"    # 経験値獲得メッセージ
            if hero.add_exp(enemy.exp):         # 経験値追加（レベルアップ判定）
                mes += f"\nレベル {hero.level} に上昇"  # レベルアップ時メッセージ
            dialog.show(mes)        # ダイアログ表示
            data.scene_next = "map" # シーンをマップに
