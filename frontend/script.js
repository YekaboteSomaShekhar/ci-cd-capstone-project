function load() {
  fetch("http://localhost:5000/users")
    .then(res => res.json())
    .then(data => {
      document.getElementById("output").innerText = JSON.stringify(data, null, 2);
    })
    .catch(err => console.error(err));
}
