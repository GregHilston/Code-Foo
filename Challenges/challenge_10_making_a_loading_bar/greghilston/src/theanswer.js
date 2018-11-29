var totalTime;
var curTime;

var setButton = document.getElementById("setload");
var loadingBar = document.getElementById("progress");

setButton.onclick = function() {
  resetLoad();
}

function resetLoad() {
  totalTime = document.getElementById("secondsinput").value * 100;
  curTime = 0;
  setLoadingBar();
  loadBar();
}

function setLoadingBar() {
  loadingBar.style.width = ((curTime / totalTime) * 100) + "%";
  loadingBar.innerHTML = ((curTime / totalTime) * 100).toFixed(0) + "%";
}

function loadBar() {
  var loading = setInterval(loadTheBar,0);
  function loadTheBar() {
    if (curTime < totalTime) {
      curTime++;
      setLoadingBar();
    } else {
      clearInterval(loading);
    }
  }
}
