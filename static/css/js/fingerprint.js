function startFingerprint() {
    const status = document.getElementById("status");
    const btn = document.getElementById("scanBtn");

    btn.disabled = true;
    status.innerText = "Scanning fingerprint...";

    setTimeout(() => {
        status.innerText = "Fingerprint Verified ✔";
        window.location.href = "/fingerprint-verify";
    }, 2000);
}
