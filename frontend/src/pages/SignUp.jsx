import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { toast, ToastContainer } from "react-toastify";
// import "react-toastify/dist/ReactToastify.css";

import "./SignUp.css";
import { SignUp } from "../../src/services/authentication"

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

      <div className="box-auth">
        <h2>Signup</h2>
        <form onSubmit={handleSubmit} className="signup">
          <div className="signup-form">

            <br></br>
            <label id="usernameLabel" htmlFor="username">
              Username:
            </label>
            <input
              id="username"
              type="text"
              placeholder="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />

            <br></br>
            <label id="emailLabel" htmlFor="email">
              Email:
            </label>
            <input
              id="email"
              type="text"
              placeholder="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />

            <br></br>
            <label id="passwordLabel" htmlFor="password">
              Password:
            </label>
            <input
              id="password"
              type="password"
              placeholder="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />

            <br></br>
            <label id="confirmPasswordLabel" htmlFor="password">
              Confirm Password:
            </label>
            <input
              id="confirmPassword"
              type="password"
              placeholder="confirm password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
            />

            <br></br>
            <label id="profileImageLabel" htmlFor="profileImage">
              Profile Image:
            </label>
            <input
              id="profileImage"
              role="profile-image"
              type="file"
              onChange={(e) => setFile(e.target.files[0])}
            />
          </div>
          <div className="signup-buttons">
          <br></br>
            <input 
              role="submit-button"
              id="submit"
              type="submit"
              value="Sign Up"
              className="button-class"
            />
          </div>
        </form>            
      </div>
      <br></br>
      <Link id="login" to="/">Return to home page</Link>
    </div>
  );
}