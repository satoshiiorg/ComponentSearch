#!/usr/bin/env python3
##!/usr/local/bin/python3
# coding: utf-8
import logic
import cgi, cgitb

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

# print(form)
# $ python3 -m http.server --cgi
# http://localhost:8000/cgi-bin/search.py
# $ curl 'http://localhost:8000/cgi-bin/search.py' -d 'param=world' -XPOST
# curl http://169.254.169.254/latest/meta-data/public-ipv4
# http://18.220.204.228:8000/cgi-bin/search.py?param=%E3%83%86%E3%82%B9%E3%83%88
# echo "http://$(curl http://169.254.169.254/latest/meta-data/public-ipv4 2>/dev/null):8000/index.html"
# SSL化？
