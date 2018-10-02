// 検索フォーム
let xhr;
document.getElementById("search_form").addEventListener('change', search);
function search() {
xhr = new XMLHttpRequest();
// TODO エラー処理
if (!xhr) {
  alert("エラーが発生しました");
  return false;
}
// TODO これずっと走ってるのか確認
xhr.onreadystatechange = refreshResults;
xhr.open('POST', '/cgi-bin/search.py');
xhr.send(new FormData(document.getElementById("search_form")));
}

// titleとimage文字列からtr要素を生成
// エスケープはこのメソッドで行う
function tr(title, image) {
const tr = document.createElement("tr");
const td_title = document.createElement("td");
td_title.textContent = title;
const td_image = document.createElement("td");
td_image.textContent = image;
tr.appendChild(td_title);
// TODO img要素
tr.appendChild(td_image);
return tr;
}

function refreshResults() {
if (xhr.readyState === XMLHttpRequest.DONE) {
  if (xhr.status === 200) {
    const results = JSON.parse(xhr.responseText);
    const table = document.getElementById("result");
    table.textContent = null;
    results.forEach(result => table.appendChild(tr(result.title, result.image)));
  } else {
    alert('リクエストに問題が発生しました');
  }
}
}

//TODO さすがにコピペすぎるので何かしらフレームワーク使う
document.getElementById("register_button").addEventListener('click', register);

function register() {
xhr = new XMLHttpRequest();
// TODO エラー処理
if (!xhr) {
  alert("エラーが発生しました");
  return false;
}
xhr.onreadystatechange = refreshResults;
// xhr.onreadystatechange = () => alert("登録しました");
const register_form = document.getElementById("register_form");
// FIXME STUB
register_form.register_id.value = register_form.register_title.value;
xhr.open('POST', '/cgi-bin/register.py');
xhr.send(new FormData(register_form));
}
