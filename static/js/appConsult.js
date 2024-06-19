function consult_user() {
    let id_user = document.getElementById("ident").value
    let obj_user = {
        "id":id_user,
        "passw":"123456"
    }
    fetch("/consult_user", {
        "method":"post",
        "header":{"Content-Type":"application/json"},
        "body":JSON.stringify(obj_user)
    })
}