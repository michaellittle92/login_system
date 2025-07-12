async function main() {
  const login_button = document
    .querySelector("#login_button")
    .addEventListener("click", login);
}

async function login() {
  upperbound = 50;
  lowerbound = 5;
  username = document.querySelector("#username").value;
  password = document.querySelector("#password").value;

  if (
    username.length > lowerbound &&
    username.length < upperbound &&
    password.length > lowerbound &&
    password.length < upperbound
  ) {
    console.log("ok");
  } else {
    console.log(
      `Username and password must be between ${lowerbound} and ${upperbound} characters.`
    );
  }
}

main();
