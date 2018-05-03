var getJSON = function(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
      var status = xhr.status;
      if (status == 200) {
        callback(null, xhr.response);
      } else {
        callback(status);
      }
    };
    xhr.send();
};

var postJSON = function(url, params, callback) {
    var xhr = new XMLHttpRequest();
    var params; // as json style string;
    xhr.open("POST", url, true);

    //Send the proper header information along with the request
    xhr.setRequestHeader("Content-type", "application/json");

    xhr.onreadystatechange = function() {//Call a function when the state changes.
        if(xhr.status == 200) {
            callback(null, JSON.parse(xhr.responseText));
        } else {
            callback(xhr.status, null)
        }
    }
    xhr.send(params);
}
