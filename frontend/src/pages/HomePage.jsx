import { toast, ToastContainer } from "react-toastify";
import "./HomePage.css";

export function HomePage() {
    return (
        <div className="wrapper-auth">
            <ToastContainer toastStyle={{ backgroundColor: "#E4E0E1", color: "#493628" }} />
    
            <div className="logo-auth">
                <h1>Birds App</h1>
                <h3>Catch your bird!</h3>
            </div>
            <div className="box-auth">
                <a href="/login" className="button-class">Login</a> 
                <a href="/SignUp" className="button-class">Sign up</a>
            </div>
        </div>
    );
}
