async function main() {
  const login_button = document
    .querySelector("#login_button")
    .addEventListener("click", login);
}

async function login() {
  const upperbound = 50;
  const lowerbound = 5;
  const username = document.querySelector("#username").value;
  const password = document.querySelector("#password").value;

  if (
    username.length > lowerbound &&
    username.length < upperbound &&
    password.length > lowerbound &&
    password.length < upperbound
  ) {
    console.log("ok");
    const url = "http://127.0.0.1:8000/login";

    fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username: username, password: password }),
    })
      .then((res) => res.json())
      .then((data) => console.log(data))
      .catch((err) => console.error(err));
  } else {
    console.log(
      `Username and password must be between ${lowerbound} and ${upperbound} characters.`
    );
  }
}

main();
