#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import logic
import cgi
# TODO DEBUG
# import cgitb; cgitb.enable()

# 検索API
form = cgi.FieldStorage()
file = form["search_file"].value

# バイナリ形式チェックして特徴量計算して検索
if logic.isimage(file):
    feature = logic.image_to_feature(file)
    result = logic.search_by(feature)
else:
    result = {"error" : "not an image"}

# 結果を出力
print("Content-type: application/json; charset=UTF-8\r\n\r\n")
print(result)
