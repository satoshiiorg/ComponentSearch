#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import logic
import cgi, cgitb

# 登録API
# TODO 検索と統合する？

form = cgi.FieldStorage()
title = form["register_title"].value
id = form["register_id"].value
file = form["register_file"].value

# バイナリ形式チェックして特徴量計算して登録
if logic.isimage(file):
    feature = logic.image_to_feature(file)
    result = logic.register(id, file, feature)
else:
    result = {"error" : "not an image"}

# 結果を出力
print("Content-type: application/json; charset=UTF-8\r\n\r\n")
print(result)
