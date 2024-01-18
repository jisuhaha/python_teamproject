container = document.getElementById('container');

toggle = () => {
  container.classList.toggle('sign-up');
}

setTimeout(() => {
  container.classList.add('sign-up')
}, 200)

$(document).ready(function () {
  $("input[name='grade']").change(function () {
    // 기사 선택 시.
    if ($("input[name='grade']:checked").val() == '10') {
      console.log(111)
      $('#info').attr("placeholder", "차량번호");
      $('#carinfo').show();
    }
    // 고객사 선택 시.
    else if ($("input[name='grade']:checked").val() == '20') {
      console.log(222)
      $('#carinfo').hide();
      $('#info').attr("placeholder", "고객사주소");
    }
  });

  function checkPassword() {
    // 비밀번호 및 확인 비밀번호 필드 값 가져오기
    var password = document.getElementById("password").value;
    var re_password = document.getElementById("re_password").value;

    // 비밀번호 일치 여부 확인
    if (password === re_password) {
      document.getElementById("pw_message").innerHTML = "";
    } else {
      document.getElementById("pw_message").style.color = "red";
      document.getElementById("pw_message").innerHTML = "패스워드가 일치하지 않습니다.";
    }
  }
  var password = document.getElementById("password")
  var re_password = document.getElementById("re_password")
  
  password.addEventListener("focusout", (event) => {
    checkPassword()
  });
  
  re_password.addEventListener("focusout", (event) => {
    checkPassword()
  });
  
  var memberid = document.getElementById("memberid")
  memberid.addEventListener("focusout", (event) => {
    check_id()
  });
  
  function check_id() {
    var id = document.getElementById("memberid").value;
    $.ajax({
      url: '/user/exists',
      type: 'GET',
      dataType: 'text',
      data: { 'id': id },
      success: function (response) {
        if(response=='0'){
          document.getElementById("id_message").innerHTML = "";
        } else {
            document.getElementById("id_message").style.color = "red";
            document.getElementById("id_message").innerHTML = "중복된 ID";
          }
        },
        error: function (error) {
          console.error('Error:', error);
        }
    });
}

});
