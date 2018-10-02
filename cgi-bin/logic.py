#-*- coding: utf-8 -*-
# DBアクセス/画像処理関連の共通ロジック
# ちゃんとビジネス/データアクセス/画像処理で分割する？
import json
from logging import getLogger, StreamHandler, DEBUG

# TODO 後で精査
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False
def warning(s):
    logger.warning(s)

# TODO STUB
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
    # TODO エスケープされるけど可読性微妙
    return json.dumps(result)

# FIXME STUB
# DB検索して結果のリスト(ゲーム名、画像)を返す
# DBが対応していればこの時点でJSON？
def search_by(feature):
    result = [
        {"title" : feature, "image" : "画像URL1"},
        {"title" : "サンプル2", "image" : "画像URL2"},
        {"title" : "サンプル3", "image" : "画像URL3"},
    ]
    # エスケープされる
    return json.dumps(result)
