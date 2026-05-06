document.querySelector("form").addEventListener("submit", function (e) {
    const voterId = document.querySelector("input[name='voter_id']").value;
    const password = document.querySelector("input[name='password']").value;

    if (voterId === "" || password === "") {
        e.preventDefault();
        alert("Please fill all fields");
    } else {
        alert("Login submitted (Backend will verify)");
    }
});
