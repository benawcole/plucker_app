/* eslint-disable react/no-unescaped-entities */
import { useState } from "react"

// This is just HTML - there is no functionality to this form
import { useNavigate } from "react-router-dom";
import "./Login.css"
// import { NavBar } from "../../src/components/NavBar";
import { Login } from "../../src/services/authentication";

export function LoginPage() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const navigate = useNavigate();
    
    async function handleSubmit(event) {
        event.preventDefault();
        try {
            const token = await Login(email, password);
            localStorage.setItem("token", token);
            navigate("/myProfile");
        } catch (err) {
            console.error(err);
            navigate("/login");
        }
    }
    
    function handleEmailChange(event) {
        setEmail(event.target.value);
    }
    
    function handlePasswordChange(event) {
        setPassword(event.target.value);
    }


    return (
        <>
        {/* <NavBar /> */}
        
        <div className="login-container">
            <h2>Login</h2>
            <form className="login-form" action="/login" method="POST" onSubmit={handleSubmit}>
                <label className="username">Username</label>

                <br></br>
                <input 
                    type="text" 
                    id="email" 
                    name="email" 
                    placeholder="email"
                    value={ email }
                    onChange={handleEmailChange} />
                <br></br>
                <label className="password">Password</label>
                <br></br>
                <input 
                    type="text" 
                    id="password" 
                    name="password" 
                    placeholder="password"
                    value={ password }
                    onChange={handlePasswordChange} />
                <br></br>
                <input 
                    type="submit" 
                    value="Login"
                    className="button-class"
                    role="submit-button"
                    id="submit" />

            </form>
            <a href="/signup" className="button-class">New Account</a>
            <a href="/" className="button-class">Return to homepage</a>
        </div>
        
        </>
    )
}