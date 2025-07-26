import pygame, data, hero, enemy, dialog, audio
from random import randrange

# 開始
def start():
    # 攻撃
    at = randrange(enemy.at // 2, enemy.at) # 半分以上、1倍未満
    df = randrange(hero.df)     # 0以上、1倍未満
    damage = max(1, at - df)    # ダメージ（最小1）
    hero.hp = max(0, hero.hp - damage)  # HP減少（HPの最低値は0）

    # 演出と進行
    audio.damage.play()     # ダメージSE再生
    data.ef_hero = True     # 自演出ありに
    data.ef_time_start = pygame.time.get_ticks()    # 演出開始時間記録
    data.proc = "enemy_draw"    # 進行を敵描画に

# 描画
def draw():
    time = pygame.time.get_ticks()  # ゲーム開始からの経過時間
    if time >= data.ef_time_start + 500:    # 500ミリ秒以上経過したか
        data.ef_hero = False    # 自演出なしに
        end()   # 終了

# 終了
def end():
    data.proc = "menu"  # 進行をメニューに
    if hero.hp == 0:    # HPが0か確認
        audio.play(audio.LOSE)  # 敗北のBGM再生
        dialog.show("あなたは死にました\nそして復活しました")   # ダイアログ表示
        mes = "経験値 20 獲得"  # 経験値獲得メッセージ
        if hero.add_exp(20):    # 経験値追加（レベルアップ判定）
            mes += f"\nレベル {hero.level} に上昇"  # レベルアップ時メッセージ
        dialog.show(mes)    # ダイアログ表示

        # スタート位置に移動して回復
        hero.x = hero.next_x = hero.start_x # X位置、次回X位置を開始X位置に
        hero.y = hero.next_y = hero.start_y # Y位置、次回Y位置を開始Y位置に
        hero.hp = hero.hp_max   # HP回復
        hero.mp = hero.mp_max   # MP回復
        data.scene_next = "map" # シーンをマップに
