#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import logic
import cgi
# TODO DEBUG
# import cgitb; cgitb.enable()

# フラグで判別
form = cgi.FieldStorage()
action = form["action"].value
if action == "search":
    # 検索
    file = form["search_file"].value
    # バイナリ形式チェックして特徴量計算して検索
    if logic.isimage(file):
        feature = logic.image_to_feature(file)
        result = logic.search_by(feature)
    else:
        result = {"error" : "not an image"}
elif action == "register":
    # 登録
    title = form["register_title"].value
    file = form["register_file"].value
    # TODO 登録処理
    # result = 
else:
    result = {"error" : "invalid action"}

# 結果を出力
print("Content-type: application/json; charset=UTF-8\r\n\r\n")
print(result)
