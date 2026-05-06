document.querySelector("form").addEventListener("submit", function (e) {
    const selected = document.querySelector("input[name='party']:checked");

    if (!selected) {
        e.preventDefault();
        alert("Please select a party before submitting your vote");
        return;
    }

    const confirmVote = confirm(
        "Are you sure you want to vote for " + selected.value + "?"
    );

    if (!confirmVote) {
        e.preventDefault();
    }
});
