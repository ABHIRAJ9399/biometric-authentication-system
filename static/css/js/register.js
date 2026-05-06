document.querySelector("form").addEventListener("submit", function (e) {
    const name = document.querySelector("input[name='name']").value.trim();
    const voterId = document.querySelector("input[name='voter_id']").value.trim();
    const password = document.querySelector("input[name='password']").value.trim();

    if (name === "" || voterId === "" || password === "") {
        e.preventDefault();
        alert("All fields are required");
        return;
    }

    if (password.length < 4) {
        e.preventDefault();
        alert("Password must be at least 4 characters");
        return;
    }

    alert("Registration submitted (data will be stored in database)");
});
