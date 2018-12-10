# メモ

画像処理関連
・OpenCV
・特徴点を正規化して点ごとにDB登録
・検索時は同様に特徴点を正規化して点ごとに in で検索？
・実際にこれでうまくいくのかどうか
・精度あげるにはML？どのように？
・特徴点の検出の精度をMLでやる感じ？
・物体検出は？
・形状マッチング
・文字認識も使うかどうか
    ・検索キーに使えるので取れればとる

IF
・ウェブベース
・カメラAPI
・のちのち必要になるかもしれないのでPythonベース？

DB/DDL
何らかの特徴量を何らかの形式で正規化してDBに格納
検索ソースとなる画像の特徴量を使ってその特徴量の近傍にあるレコードを検索
あるいは特徴量の距離を取ってソート上位を表示（距離の*和*の小さいもの）
最初に輪郭で部品を切り分けて部品ごとに特徴量を取る

特徴量が配列で返るなら (ゲーム, コンポーネント, 特徴量) をPKにして
多対多で特徴量をマッチングさせゲームでグルーピングして件数順に表示とか


BGG/Amazon辺りをAPI使ってクロールしてML

ヒストグラムで絞ってからマッチングするとか？
でも背景とかコンポーネント丸ごと撮ってるかどうかとかで微妙
背景白にしてとか指定できるものか 照明でも違ってくるだろうし
単体でやるのでない限り物体検出はどうしても必要になる


# 画像のアップロードについて
axiosデフォルトのフォーム送信はJSONらしく、
単に画像をファイルとしてアップロードするならBASE64などでエンコードして詰めるのがよさそう
ただ今回はサーバ側でOpenCVを使う関係上エンコード/デコードを繰り返すのは無駄なので
通常のmulti-partとして送信した方がよさそう




# インストール
OpenCV
sudo pip-3.6 install numpy opencv-python 

alike/Ant/Ivy
wget http://ftp.meisei-u.ac.jp/mirror/apache/dist//ant/binaries/apache-ant-1.10.5-bin.zip
wget http://ftp.riken.jp/net/apache//ant/ivy/2.5.0-rc1/apache-ivy-2.5.0-rc1-bin.zip
unzip
ant/binにパスを通す
ant/libにivy.jarのリンクを張る
ln -s ../../apache-ivy-2.5.0-rc1/ivy-2.5.0-rc1.jar ivy.jar
svn export http://svn.apache.org/repos/asf/labs/alike
cd alike/trunk
java10だとビルドエラー出る
ant
scala



# あとで見る
https://hazm.at/mox/machine-learning/computer-vision/recipes/similar-image-retrieval.html
とりあえず特徴量ベースでDBなし検索で一致度見てから考える
キーワード: CBIR Content-Based Image Retrieval
https://www.rondhuit.com/oss%E3%81%AE%E9%A1%9E%E4%BC%BC%E7%94%BB%E5%83%8F%E6%A4%9C%E7%B4%A2%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88-apache-alike-%E3%81%AE%E3%81%94%E7%B4%B9%E4%BB%8B.html

# TODO 
画像で画像検索の略称なんだっけ
スマホ最適化
DnDインタフェース
登録フォーム折りたたみ
