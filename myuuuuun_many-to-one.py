# -*- encoding: utf-8 -*-
from __future__ import division, print_function
import numpy as np
import random
import math


# セッティングを関数化
def settings(m, f):
    # 受験者(=proposer)の人数(m), 大学(=respondent ?)の数(f)

    # 受験者, 大学のリスト
    props = list(range((m)))
    resps = list(range((f)))

    # 受験者と大学の選好表を作成
    prop_choice = list(range((f+1)))
    resp_choice = list(range((m+1)))
    prop_prefs = [random.sample(prop_choice, f+1) for i in props]
    resp_prefs = [random.sample(resp_choice, m+1) for i in resps]
    
    # 大学の収容可能人数を(0 〜 proposerの総人数 までの範囲で適当に決める)
    caps = list(range((f)))
    for i in caps:
        caps[i]=random.randint(0, m)

    return prop_prefs, resp_prefs, caps


def array_to_dict(array):
    dict = {}
    for x, y in enumerate(array):
        dict[x] = list(y)
    return dict


def deferred_acceptance(prop_prefs, resp_prefs, caps=None):
    # 選好表を辞書に変換
    props = array_to_dict(prop_prefs)
    resps = array_to_dict(resp_prefs)

    # 選好表の行数、列数をチェック（それぞれの選好表毎の行数・列数は揃っていると信じる） 
    prop_row = len(prop_prefs)
    prop_col = len(prop_prefs[0])
    resp_row = len(resp_prefs)
    resp_col = len(resp_prefs[0])

    # 受験者、大学の数を代入（アンマッチ・マークは含まない数）
    prop_size = prop_row
    resp_size = resp_row

    if (prop_row != resp_col - 1) or (resp_row != prop_col - 1):
        print("2つの選好表の行列数が不適切です")
        exit(-1)

    # アンマッチ・マーク（これよりも選好表の後ろ側にいる大学には入らない！というマーク）
    # は、選好表の1列の中で一番大きな数字を採用（m列なら、配列は0から始まるので、m-1がアンマッチ・マーク）
    prop_unmatched_mark = prop_col - 1
    resp_unmatched_mark = resp_col - 1

    # 受験者側をkeyとしたマッチングリストだけだと辛いので、大学側をkeyとしたマッチングリストも作りましょう
    # prop_matchesは、受験者をkey、大学をvalueとした、{prop1: resp3, prop2: resp1,...} という辞書。
    # resp_matchesは、大学をkey、受験者（のリスト）をvalueとした、{resp1: [prop0, prop2, prop3,...], ...}という辞書。
    # 最初はそれぞれ空文字をいれておく。未マッチングの場合はアンマッチ・マークが入る。
    prop_matches = {}
    resp_matches = {}
    for i in range(prop_size):
        prop_matches[i] = ""

    for i in range(resp_size):
        resp_matches[i] = []


    # 未処理の受験者の集合（初期状態では、全ての受験者）
    # 入学先が見つかるか、行きたい大学全てに申し込んで断られたら、消去する
    unsettled = list(range(prop_size))

    # 未処理の受験者がいる限り、繰り返す。
    while len(unsettled) != 0:

        # 未処理の受験者の集合から1人ずつとりだして、処理をする
        for i in unsettled:

            # iの選好表から、（今までフラれていない中で）一番好きな大学をとり出す
            candidate = props[i].pop(0)
            print("受験者 " + str(i) + " が、大学 " + str(candidate) + " に応募します")

            # もし取り出したcandidateがアンマッチ・マークなら、iはアンマッチで処理終了
            # マッチングにはprop_unmatched_markをいれる
            if candidate == prop_unmatched_mark:
                prop_matches[i] = prop_unmatched_mark
                unsettled.remove(i)

            # これは何をやっている処理でしょうか……？
            """
            if caps[candidate] == 0:
                matches[i] =""
                unsettled.append(i)

            elif 0 <= matches.values().count(candidate) < caps[candidate]:
                matches[i] = candidate
                unsettled.remove(i)
                if matches.values().count(candidate) == caps[candidate]:
                    matches_inv = {v:k for k, v in sort(matches.items())}
            """

            # この先の処理を擬似コードで書きます。

            # If 大学（candidate）の現在の仮入学者（resp_matches[candidate]）の人数が、
            # 受入可能人数（caps[candidate]）未満なら:
            #     If 大学の選好リストで、自分がアンマッチ・マークよりも上位にいるなら: 
            #        iを未処理リスト（unsettled）から消す
            #        prop_matchesに{i: candidate}を加える
            #        resp_matches[candidate]に iを追加する（resp_matchesのvalueはリストなので、appendを使えばよい）
            #     Else:
            #        処理終了。unsettledから次のiをとってくる
            #

            # Else:（大学の現在の仮入学者数が、定員と同じなら）
            #     大学の現在の仮入学者（resp_matches[candidate]）の中で、一番大学にとって選好順序の低い受験者(worst_matchedとする)をとり出す
            #     If 自分とその受験者のランクを比べて、自分のほうが上なら:
            #        (※この場合、自分がアンマッチ・マークより上位であることも保証される)
            #        iを未処理リスト（unsettled）から消す
            #        worst_matchedを未処理リストに追加する
            #        prop_matchesから{worst_matched: candidate}を削除する
            #        resp_matches[candidate]からworst_matchedを削除する
            #        prop_matchesに{i: candidate}を加える
            #        resp_matches[candidate]に iを追加する
            
            # 処理終了。forループを進めて次のiをとり出す

                                

if __name__ == "__main__":

    #prop_prefs, resp_prefs, caps = settings(59, 30)
    m_unmatched = 3
    prop_prefs = [[0, 1, 2, m_unmatched],
                  [2, 0, 1, m_unmatched],
                  [1, 2, 0, m_unmatched],
                  [2, 0, 1, m_unmatched]]

    f_unmatched = 4
    resp_prefs = [[2, 0, 1, 3, f_unmatched],
                  [0, 1, 2, 3, f_unmatched],
                  [2, f_unmatched, 1, 0, 3]]


    caps = [2, 1, 1]
    
    print("受験者の選好表は")
    print(prop_prefs)

    print("大学の選好表は")
    print(resp_prefs)

    print("大学の受け入れ可能人数は")
    print(caps)

    deferred_acceptance(prop_prefs, resp_prefs, caps)








