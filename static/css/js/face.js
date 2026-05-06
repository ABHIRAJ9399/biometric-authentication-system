const video = document.getElementById("video");

navigator.mediaDevices.getUserMedia({ video: true })
.then(stream => {
    video.srcObject = stream;
});

function startFace() {
    document.getElementById("status").innerText = "Face Verified ✔";
    setTimeout(() => {
        window.location.href = "/face-verify";
    }, 1500);
}
navigator.mediaDevices.getUserMedia({ video: true })
.then(stream => {
    document.getElementById("video").srcObject = stream;
});