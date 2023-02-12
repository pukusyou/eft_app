function check() {
    const regex = /^[a-zA-Z0-9_+-]+(.[a-zA-Z0-9_+-]+)*@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$/;
    var address = $("#mail").val()
    var subject = $("#subject").val()
    var body = $("#body").val()
    if (!regex.test(address)) {
        alert("Incorrect email address")
        return false
    }
    if (address.length < 3) {
        alert("Email address is too short")
        return false
    }
    if (subject.length < 5) {
        alert("Please enter at least 5 characters in the subject line")
        return false
    }
    if (body.length < 10) {
        alert("Please enter at least 10 characters for the body text")
        return false
    }
}