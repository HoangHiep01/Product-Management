window.addEventListener("DOMContentLoaded", () => {


  const socket = new WebSocket("ws://localhost:5678/");

  // Connection opened
  socket.onopen = function() {
    console.log("Open.")
  }

  // const messages = document.createElement("ul");
  // document.body.appendChild(messages);
  socket.onmessage = function(event) {
    console.log("Message.");
    document.getElementById("idInput").value = event.data;
    // document.getElementById('scanForm').submit();
    // const message = document.createElement("li");
    // const content = document.createTextNode(event);
    // message.appendChild(content);
    // messages.appendChild(message);
  }

});
