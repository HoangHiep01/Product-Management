window.addEventListener("DOMContentLoaded", () => {

  const websocket = new WebSocket("ws://192.168.1.18:5678/");
  websocket.onmessage = ({ data }) => {
    document.getElementById("idInput").value = data;
    document.getElementById('scanForm').submit();
  };
});