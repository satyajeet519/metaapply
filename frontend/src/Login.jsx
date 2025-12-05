import { useState } from "react";

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [responseMessage, setResponseMessage] = useState('');

    const handleSubmit = async(e) => {
        e.preventDefault(); 
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

        if(response.ok){
            setResponseMessage("Login Successful!");
        }
        else{
            setResponseMessage(data.detail | "Login Not Successful!")
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