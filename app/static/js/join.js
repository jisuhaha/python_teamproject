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
      document.getElementById("repw_message").innerHTML = "";
    } else {
      document.getElementById("repw_message").style.color = "red";
      document.getElementById("repw_message").innerHTML = "패스워드가 일치하지 않습니다.";
      return false;
    }
  }
  var password = document.getElementById("password")
  var re_password = document.getElementById("re_password")
  
  function password_reg(){
    var password = document.getElementById("password");
    var pwdCheck = /^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,25}$/;
    if(!pwdCheck.test(password.value)){
      document.getElementById("pw_message").style.color = "red";
      document.getElementById("pw_message").innerHTML = "비밀번호는 영문자+숫자+특수문자 조합으로 8~25자리 사용해야 합니다.";
      return false;
    }else{
      document.getElementById("pw_message").innerHTML = "";
    }
  }

  password.addEventListener("focusout", (event) => {
    password_reg()
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
        if (response == '0' && id.length!=0 ) {
          document.getElementById("id_message").innerHTML = "";
        } else {
          document.getElementById("id_message").style.color = "red";
          document.getElementById("id_message").innerHTML = "사용 불가능한 ID";
          return false;
        }
      },
      error: function (error) {
        console.error('Error:', error);
      }
    });
  }

  function phoneNumberCheck() {
    var number = document.getElementById("telphone").value;
    const phoneNumberRegex = /^(0\d{1,2}-\d{3,4}-\d{4})$/;
    if (phoneNumberRegex.test(number)) {
      document.getElementById("tel_message").innerHTML = "";
      
    } else {
      document.getElementById("tel_message").innerHTML = "유효하지 않은 전화번호입니다";
      document.getElementById("tel_message").style.color = "red";
      return false;
    }
  }
  
  var telphone = document.getElementById("telphone")
  telphone.addEventListener("focusout", (event) => {
    phoneNumberCheck()
  });
  
  function nameCheck(){
    var name = document.getElementById("name");
    if(name.length!=0){
      document.getElementById("name_message").innerHTML = "";
    }else{
      document.getElementById("name_message").innerHTML = "이름을 입력해주세요";
      document.getElementById("name_message").style.color = "red";
      return false;
    }
  }
  
  
  function joinform_check() {
    var memberid = document.getElementById("memberid");
    var password = document.getElementById("password");
    var re_password = document.getElementById("re_password");
    var telphone = document.getElementById("telphone");
    var name = document.getElementById("name");
    var info = document.getElementById("info");
    var carinfo = document.getElementById("carinfo");
    if (memberid.value==false) { 
      memberid.focus();
      return false;
    };
    
    if (password.value == "") {
      password.focus();
      return false;
    };
    
    if (check_id==false) { 
      memberid.focus();
      return false;
    };
    
    if (password.value == "") {
      password.focus();
      return false;
    };
    
    //비밀번호 영문자+숫자+특수조합(8~25자리 입력) 정규식
    var pwdCheck = /^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,25}$/;
    
    if (password_reg()==false) {
      password.focus();
      return false;
    };
    
    if (password.value !== re_password.value) {
      re_password.focus();
      return false;
    };
    
    if (phoneNumberCheck() == false) {
      telphone.focus();
      return false;
    };
    if (nameCheck()==false) {
      name.focus();
      return false;
    };
    if (info.value == "") {
      if($("input[name='grade']:checked").val() == '10'){
        document.getElementById("info_message").innerHTML = "차량번호를 입력하세요.";
        document.getElementById("info_message").style.color = "red";
        info.focus();
        return false;
      }else{
        document.getElementById("info_message").innerHTML = "고객사 이름을 입력하세요.";
        document.getElementById("info_message").style.color = "red";
        info.focus();
        return false;
      }
    }else{
      document.getElementById("info_message").innerHTML = "";
    };
    
    if($("input[name='grade']:checked").val() == '10'){
      if(carinfo.value==""){
        document.getElementById("carinfo_message").innerHTML = "차량정보를 입력하세요.";
        carinfo.focus();
        return false
      }
    }else{
      document.getElementById("carinfo_message").innerHTML = "";
    };
    //입력 값 전송
    document.join_form.submit(); //유효성 검사의 포인트   
  }
  
  var submit_button = document.getElementById('submit_button');
  submit_button.addEventListener("click", joinform_check);
  

});
