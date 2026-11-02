const socket = new WebSocket("ws://127.0.0.1:8000/ws");
const messagesDiv = document.getElementById("messages");
const messageInput = document.getElementById("messageInput");
const sendBtn = document.getElementById("sendBtn");

socket.onmessage = (event) => {
  const p = document.createElement("p");
  p.textContent = event.data;
  messagesDiv.appendChild(p);
};

sendBtn.addEventListener("click", () => {
  const text = messageInput.value;
  if (text) {
    socket.send(text);
    messageInput.value = "";
  }
});
