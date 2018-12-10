// import Vue from 'vue';
// import axios from 'axios';

const resultVue = new Vue({
  el: "#result",
  data: {
    items: []
  }
});

// const searchVue = 
new Vue({
  el: '#search_form',
  methods: {
    search_file: function(e) {
      e.preventDefault();
      const params = new FormData();
      params.append('action', 'search');
      params.append('search_file', e.target.files[0]);
      axios.post('/cgi-bin/api.py', params)
          .then(response => resultVue.items = response.data);
    }
  }
});

// const registerVue = 
// new Vue({
//   el: '#register_form',
//   data: {
//     title: null
//   }
//   // FIXME onSubmit
// });


// titleとimage文字列からtr要素を生成
// エスケープはこのメソッドで行う
// function tr(title, image) {
// const tr = document.createElement("tr");
// const td_title = document.createElement("td");
// td_title.textContent = title;
// const td_image = document.createElement("td");
// td_image.textContent = image;
// tr.appendChild(td_title);
// // TODO img要素
// tr.appendChild(td_image);
// return tr;
// }
// //TODO さすがにコピペすぎるので何かしらフレームワーク使う
// document.getElementById("register_button").addEventListener('click', register);

// function register() {
// xhr = new XMLHttpRequest();
// // TODO エラー処理
// if (!xhr) {
//   alert("エラーが発生しました");
//   return false;
// }
// xhr.onreadystatechange = refreshResults;
// // xhr.onreadystatechange = () => alert("登録しました");
// const register_form = document.getElementById("register_form");
// // FIXME STUB
// register_form.register_id.value = register_form.register_title.value;
// xhr.open('POST', '/cgi-bin/register.py');
// xhr.send(new FormData(register_form));
// }
