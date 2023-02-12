function check() {
    const regex = /^[a-zA-Z0-9_+-]+(.[a-zA-Z0-9_+-]+)*@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$/;
    var address = $("#mail").val()
    var subject = $("#subject").val()
    var body = $("#body").val()
    if (!regex.test(address)) {
        alert("メールアドレスが正しくありません")
        return false
    }
    if (address.length < 3) {
        alert("メールアドレスが短すぎます")
        return false
    }
    if (subject.length < 5) {
        alert("件名は5文字以上入力してください")
        return false
    }
    if (body.length < 10) {
        alert("本文は10文字以上入力してください")
        return false
    }
}