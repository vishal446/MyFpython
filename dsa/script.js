function loadHTML(filename, targetId) {
    fetch(filename)
        .then(response => response.text())
        .then(data => {
            document.getElementById(targetId).innerHTML = data;
        })
        .catch(error => console.error('Error:', error));
}