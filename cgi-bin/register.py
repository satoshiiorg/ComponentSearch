#!/usr/bin/env python3
##!/usr/local/bin/python3
# coding: utf-8
import json
import cgi, cgitb

#FIXME 共通化
# FIXME STUB
# バイナリが画像かチェックする
def isimage(bin):
    return True

# FIXME STUB
# 画像の特徴量を計算
def image_to_feature(image):
    feature = image.decode(encoding="Shift_JIS")
    return feature

# FIXME STUB
# DBにタイトル(ID)・画像・特徴量を登録して結果を1行JSONで返す
# サイズチェックや重複チェックなどではじかれた場合はJSON自体に情報を記述
def register(id, image, feature):
    result = [
        {"status" : True, "title" : id, "image" : "画像URL"}
    ]
    # エスケープされる
    return json.dumps(result)

# 基本的にはAPIとして実装
# リクエストを受けて結果を返すだけ
print("Content-type: application/json; charset=UTF-8\r\n\r\n")

form = cgi.FieldStorage()
title = form["register_title"].value
id = form["register_title"].value
# FIXME
# id = form["register_id"].value
bin = form["register_file"].value

# バイナリ形式チェック
if isimage(bin):
    feature = image_to_feature(bin)
    result = register(id, bin, feature)
else:
    result = {"error" : "not an image"}

# print("Content-type: text/plain; charset=UTF-8\r\n\r\n")
# 備忘のため。text/plainな現状では不要 cgi.escape
# DBからとってきたテキストと画像をリスト表示
print(result)

# print(form)
# $ python3 -m http.server --cgi
# http://localhost:8000/cgi-bin/search.py
# $ curl 'http://localhost:8000/cgi-bin/search.py' -d 'param=world' -XPOST
# curl http://169.254.169.254/latest/meta-data/public-ipv4
# http://18.220.204.228:8000/cgi-bin/search.py?param=%E3%83%86%E3%82%B9%E3%83%88
# echo "http://$(curl http://169.254.169.254/latest/meta-data/public-ipv4 2>/dev/null):8000/index.html"
# SSL化？
