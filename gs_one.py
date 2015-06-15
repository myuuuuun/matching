#-------------------------------------------------------------------------------
# Name:        gs_one.py
# Purpose:     GS Algorithm; "one-to-one" case
#
# Author:      Hanami Maeda, Atsushi Yamagishi
#
# Created:     13/06/2015
#-------------------------------------------------------------------------------

# coding: UTF-8
from __future__ import division

#ウィキペディアの例を使用
males = {"m1":[1, 2, 3, 4],\
        "m2":[3, 2, 1, 4],\
        "m3":[1, 2, 4, 3],\
        "m4":[3, 1, 4, 2]}

females = {"f1":[1, 2, 3, 4],\
        "f2":[2, 1, 4, 3],\
        "f3":[2, 3, 1, 4],\
        "f4":[1, 4, 3, 2]}

def deferred_acceptance(males, females):
    #男性に対し、ペアの女性を返す辞書。とりあえずペアがないから、空の状態
    matches = {}
    for i in males.keys():
        matches[i] = ""
    # 独身男性の集合
    singles = males.keys()
    # 独身男性がいる限り、繰り返す。
    while len(singles) != 0:
        for i in singles:
            # プロポーズ済の人を候補者から消す
            candidate = males[i].pop(0)
            # 好みランクが最も高い人にプロポーズする。
            proposed = "f{0}".format(candidate)
            # まだ誰とも結婚してなければ自分のもの
            if proposed not in matches.values():
                matches[i] = proposed
                singles.remove(i)
            # 誰かと結婚していれば、女性の好みにより成否が決定
            else:
                # ペアについて、女性から男性を返す辞書
                matches_inv = {v:k for k, v in matches.items()}
                # 今の夫
                matched_male = matches_inv[proposed]
                # 女性の好み
                pref = females[proposed]
                # より好み＝好みで上位にランクされてるなら、略奪成功
                if pref.index(int(i[1:])) < pref.index(int(matched_male[1:])):
                    matches[i] = proposed
                    singles.remove(i)
                    # 妻を奪われ独身に戻る
                    matches[matched_male] = ""
                    singles.append(matched_male)

    print matches






