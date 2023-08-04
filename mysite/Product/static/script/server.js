
const websocket = new WebSocket("ws://192.168.1.18:5678/");

websocket.onopen = function() {
  alert('Connected!')
};

connection.addEventListener('message', function(event) {

websocket.onmessage = function(data) {
  document.getElementById("idInput").value = data;
  document.getElementById('scanForm').submit();
};

});
// eventName : open, close, send, message...


