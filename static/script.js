document.getElementById("send-btn").addEventListener("click", async () => {
    const userInput = document.getElementById("user-input").value;
    if (!userInput.trim()) return;

    // Display user message
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<p><b>You:</b> ${userInput}</p>`;
    document.getElementById("user-input").value = "";

    // Send to backend
    const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    });

    if (!res.ok) {
        chatBox.innerHTML += `<p><b>AI:</b> [Error: ${res.status}]</p>`;
        return;
    }

    const data = await res.json();

    // Display AI reply
    chatBox.innerHTML += `<p><b>AI:</b> ${data.reply}</p>`;
    chatBox.scrollTop = chatBox.scrollHeight;

    // Play AI audio
    if (data.audio_url) {
        const audio = new Audio(data.audio_url);
        audio.play();
    }
});
