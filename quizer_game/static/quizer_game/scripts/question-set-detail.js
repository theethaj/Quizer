function easy() {
  var e = document.getElementById("table_easy");
  if (e.className.indexOf("w3-show") == -1) {
    e.className += " w3-show";
  } else {
    e.className = e.className.replace(" w3-show", "");
  }
}

function medium() {
   var m = document.getElementById("table_medium");
  if (m.className.indexOf("w3-show") == -1) {
    m.className += " w3-show";
  } else {
    m.className = m.className.replace(" w3-show", "");
  }
}

function hard() {
  var h = document.getElementById("table_hard");
  if (h.className.indexOf("w3-show") == -1) {
    h.className += " w3-show";
  } else {
    h.className = h.className.replace(" w3-show", "");
  }
}

