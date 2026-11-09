const protocol = location.protocol === "https:" ? "wss" : "ws";
const socket = new WebSocket(`${protocol}://${location.host}/ws`);

const form = document.getElementById("chat-form");
const input = document.getElementById("message-input");
const messages = document.getElementById("messages");

function addMessage(text) {
    const li = document.createElement("li");
    li.textContent = text;  // textContent avoids HTML injection
    messages.appendChild(li);
    messages.scrollTop = messages.scrollHeight;
}

socket.addEventListener("open", () => addMessage("[Connected]"));
socket.addEventListener("close", () => addMessage("[Disconnected]"));
socket.addEventListener("message", (event) => addMessage(event.data));

form.addEventListener("submit", (event) => {
    event.preventDefault();
    const text = input.value.trim();
    if (!text || socket.readyState !== WebSocket.OPEN) {
        return;
    }
    socket.send(text);
    input.value = "";
});
