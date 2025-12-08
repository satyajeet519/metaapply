import { useState } from "react";
import { useNavigate } from "react-router";

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [responseMessage, setResponseMessage] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async(e) => {
        e.preventDefault(); 
        try {
            const response = await fetch ("http://127.0.0.1:8000/api/auth/login/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    username: username,
                    password: password,
                }),
            });
            const data = await response.json();
            console.log("Raw backend response:", data);

            if(response.ok){
                localStorage.setItem("access", data.access);
                localStorage.setItem("refresh", data.refresh);
                setResponseMessage("Login Successful!");
                navigate('/profile');
            }
            else{
                setResponseMessage(data.detail || "Login Not Successful!");
            }
        } catch (error) {
             setResponseMessage("Something went wrong");
        }
        

        
    }
    
    return(
        <>
            <div className="LoginPage">
                <h1>Login Page</h1>
                <form onSubmit={handleSubmit}>
                    <input type="text" onChange={(e)=>setUsername(e.target.value)} placeholder="Enter Username"/><br/><br/>
                    <input type="password" onChange={(e)=>setPassword(e.target.value)} placeholder="Enter Password"/><br/><br/>
                    <button type="submit">Login</button>
                </form>
                {responseMessage}
            </div>
        </>
    )
}

export default Login;