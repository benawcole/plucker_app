import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { toast, ToastContainer } from "react-toastify";
import { SignUp } from "../services/authentication";
import "react-toastify/dist/ReactToastify.css";

// import "./SignupPage.css";

export function SignUpPage() {
//   const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [file, setFile] = useState(null);

  const navigate = useNavigate();

  const validatePassword = (password) => {
    const chars = /[!#$%&'()*+,\-:;<=>?@£÷]/;

    if (password == "") {
      toast.error("Please enter a password");
    } else if (password !== confirmPassword) {
      toast.error("Passwords must match");
    } else if (password.length < 8) {
      toast.error("Password must be 8 or more characters long");
    } else if (!chars.test(password)) {
      toast.error("Password must contain at least 1 special character");
    } else {
      return true;
    }
  };

  const validateUsername = (username) => {
    if (!username) {
      toast.error("Please enter a username");
      return false;
    }

    return true;
  };

  const validateEmail = (email) => {
    if (!email || !email.includes("@") || !email.includes(".")) {
      toast.error("Please enter a valid email address with an '@' and '.'");
      return false;
    }

    return true;
  };

  async function handleSubmit(event) {
    event.preventDefault();

    if (
      validatePassword(password) &&
      validateUsername(username) &&
      validateEmail(email)
    ) {
      const formData = new FormData();
      formData.append("email", email);
      formData.append("username", username);
      formData.append("password", password);

      if (file) {
        formData.append("file", file); // Append the profile image if it exists
      }
      try {
        await SignUp(formData);
        navigate("/");
      } catch (err) {
        console.error(err);
        const errorMessage = err.message;

        if (errorMessage === "username") {
          toast.error("That username is taken, please try something else");
        } else if (errorMessage === "email") {
          toast.error(
            "An account with that email already exists, please login."
          );
        } else {
          toast.error("An unexpected error occurred. Please try again.");
        }

        setPassword("");
        setConfirmPassword("");
      }
    }
  }

  const date18YearsAgo = new Date();
  date18YearsAgo.setFullYear(date18YearsAgo.getFullYear() - 18);

  const formattedDate = `${date18YearsAgo.getFullYear()}-${(
    date18YearsAgo.getMonth() + 1
  )
    .toString()
    .padStart(2, "0")}-${date18YearsAgo.getDate().toString().padStart(2, "0")}`;

  return (
    <div className="wrapper-auth">
      <ToastContainer
        toastStyle={{ backgroundColor: "#E4E0E1", color: "#493628" }}
      />

      <div className="logo-auth">
        <h1>Birds App</h1>
        <p>Catch your bird!</p>
      </div>

      <div className="box-auth">
        <h2>Signup</h2>

        <form onSubmit={handleSubmit} className="signup">
          <div className="signup-form">
            <label id="usernameLabel" htmlFor="username">
              Username:
            </label>
            <input
              id="username"
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />

            <label id="emailLabel" htmlFor="email">
              Email:
            </label>
            <input
              id="email"
              type="text"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />

            <label id="passwordLabel" htmlFor="password">
              Password:
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />

            <label id="confirmPasswordLabel" htmlFor="password">
              Confirm Password:
            </label>
            <input
              id="confirmPassword"
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
            />

            <label id="profileImageLabel" htmlFor="profileImage">
              Profile Image:
            </label>
            <input
              id="profileImage"
              type="file"
              onChange={(e) => setFile(e.target.files[0])}
            />
          </div>
          <div className="signup-buttons">

            <Link id="login" to="/">
              Login
            </Link>
            <input
              role="submit-button"
              id="submit"
              type="submit"
              value="Sign Up"
            />
          </div>
        </form>
      </div>
    </div>
  );
}