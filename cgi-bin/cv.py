#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import numpy as np
import cv2
# import cv2, matplotlib
# import matplotlib.pyplot as plt

# とりあえず差分イラストでは完全一致する点が多すぎて検証にならないことはわかった
# [0.0, 0.0, 0.0, 0.0, 39943.0, 39943.0, 39943.0, 39943.0, 39943.0]
boys = list(map(lambda x : cv2.imread("boy%s.png" % x, cv2.IMREAD_GRAYSCALE), range(1, 6)))
girls = list(map(lambda x : cv2.imread("girl%s.png" % x, cv2.IMREAD_GRAYSCALE), range(1, 6)))

akaze   = cv2.AKAZE_create()
matcher = cv2.BFMatcher(cv2.NORM_HAMMING)

# kpは <KeyPoint 0x7f437ab12840> 形式の配列
# descはこんな感じの行列
# [[ 65  13  12 ... 121 255  31]
#  [ 65 136   8 ... 121 255  15]
#  [ 33 253   1 ... 254 127   0]
#  ...
#  [ 65 137  76 ... 121 255  55]
#  [193 233  11 ... 255  31  32]
#  [ 65 137  31 ... 245 238   7]] 
# desc同士をマッチさせて距離を取るのだからこれを直接DBに入れるのは微妙
# 最初にヒストグラムで絞って上位の特徴量を取得してローカルでマッチングとか？
# いずれにせよ実物で試してチューニングしないとよくわからない

# 特徴量検出
# kp, desc = akaze.detectAndCompute(boys[0], None)
boydescs = list(map(lambda x:akaze.detectAndCompute(x, None)[1], boys))
girldescs = list(map(lambda x:akaze.detectAndCompute(x, None)[1], girls))
boydesc = boydescs[0]
descs = boydescs[1:] + girldescs

# TODO 上位n件だけとかにする？
# 距離の和を計算
def sumDistance(matches):
    # return sum(map(lambda x:x.distance, sorted(matches, key = lambda x:x.distance)[:500]))
    return sum(map(lambda x:x.distance, sorted(matches, key = lambda x:x.distance)))

# ブルートフォースマッチング
# 距離でソート?
# 上位の距離の和を取って小さい方を選ぶ、とか
distances = list(map(lambda x:sumDistance(matcher.match(boydesc, x)), descs))

print(distances)

# for f in necchusyou_face_* ; do
#     mv $f ${f/necchusyou_face_/}
# done
