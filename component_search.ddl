-- https://paiza.io/projects/A-EwutZ7-LsY1J28WtGg9g

create schema Board_Game;

-- BGGとか外部からとる？
-- 画像登録時はこれから選択or新規追加で
-- ゲームマスタ
create table Board_Game.Games(
    game_id  integer not null,
    title    text    not null,
    comment  text,
    primary key(game_id)
);

-- 画像マスタ
create table Board_Game.Images(
    game_id  integer not null,
    image_id integer not null,
    image    blob    not null,
    comment  text,
    primary key(game_id, image_id),
    foreign key(game_id) references Board_Game.Games(game_id)
);

-- FIXME 実際には特徴点もキーにして複数レコードに分割する感じになる？
-- 検索時は多対多でマッチングしてヒット数が多いゲームから表示するとか

-- コンポーネント/特徴点
-- ここを使って検索して画像マスタ・ゲームマスタの情報を表示する
-- バッチで機械学習させて画像マスタからここを定期的に生成しなおす？
create table Board_Game.Components(
    game_id      integer not null,
    -- image_id integer, -- 画像単位で抽出する意味がないが結果表示上はあった方がいい？
    component_id integer not null,
    feature      blob    not null, -- 形式未定
    -- comment text, 
    primary key(game_id, component_id),
    foreign key(game_id) references Board_Game.Games(game_id)
    -- foreign key(image_id) references Board_Game.Images(image_id)
);

insert into Board_Game.Games(game_id, title) values (1, "ツォルキン");
insert into Board_Game.Games(game_id, title) values (2, "プエルトリコ");
insert into Board_Game.Games(game_id, title) values (3, "カタン");

select * from Board_Game.Games;
