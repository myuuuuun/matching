from __future__ import division
import numpy as np
import random


m = 59
f = 30

males = list(range(m))
females = list(range(f))
female_choice = list(range(m+1))
male_choice = list(range(f+1))
f_prefs = [random.sample(female_choice, m+1) for i in females]
m_prefs = [random.sample(male_choice, f+1) for i in males]
caps = list(range(f))
for i in caps:
    caps[i]=random.randint(0,m)


def array_to_dict(array):
    dict = {}
    for x, y in enumerate(array):
        dict[x] = list(y)
    return dict


def deferred_acceptance(m_prefs, f_prefs, caps=None):
    # 辞書に変換
    males = array_to_dict(m_prefs)
    females = array_to_dict(f_prefs)
    #男性に対し、ペアの女性を返す辞書。とりあえずペアがないから、空の状態
    matches = {}
    for i in range(len(m_prefs)):
        matches[i] = ""
    # 独身男性の集合
    unsettled = list(range(len(m_prefs)))
    # 独身男性がいる限り、繰り返す。
    while len(unsettled) != 0:
        for i in unsettled:
            # プロポーズ済の人を候補者から消す
            # 好みランクが最も高い人にプロポーズする。
            candidate = males[i].pop(0)
            # 好みランクが最も高い人にプロポーズする。
            # 好みの人がもうおらず、一人でいたい場合
            """
            if candidate == (len(f_prefs)):
                matches[i] = candidate
                unsettled.remove(i)
            """
            
            if caps[candidate] == 0:
                matches[i] =""
                unsettled.append(i)
                
            elif 0 <= matches.values().count(candidate) < caps[candidate]:
                matches[i] = candidate
                unsettled.remove(i)
                if matches.values().count(candidate) == caps[candidate]:
                    matches_inv = {v:k for k, v in sort(matches.items())}
                    
                    

prop_prefs=m_prefs
resp_prefs=f_prefs
n=f
prop_choice=male_choice
resp_choice=female_choice
props=males
resps=females
