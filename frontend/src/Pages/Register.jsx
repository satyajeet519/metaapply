import { useState } from "react";
import { useNavigate } from "react-router";

const Register = () => {
    const [username, setUsername] = useState(''); 
    const [email, setEmail] = useState(''); 
    const [password, setPassword] = useState(''); 
    const [phone, setPhone] = useState(''); 
    const [city, setCity] = useState(''); 
    const [message, setMessage] = useState('');
    const nav = useNavigate();

    const HandleRegister = async(e) =>{
        e.preventDefault();
        try {
            const response = await fetch("http://127.0.0.1:8000/api/auth/register/",{
                method: "POST",
                headers: {
                    "Content-Type" : "application/json",
                },
                body: JSON.stringify({
                    username, email, password, phone, city
                })
            });

            const data = await response.json();
            console.log("Register data", data);

            if(response.ok){
                setMessage("Registration Successful!");
                nav('/login');
            }
            else{
                setMessage(data.detail || "Registration failed");
            }
        } catch (err) {
            setMessage("Something went wrong!")
        }
    }

    return(
        <>
            <form onSubmit={HandleRegister}>
                <input type="text" placeholder="Enter Username" onChange={(e)=>setUsername(e.target.value)}/><br/><br/>
                <input type="email" placeholder="Enter Email" onChange={(e)=>setEmail(e.target.value)}/><br/><br/>
                <input type="text" placeholder="Enter Password" onChange={(e)=>setPassword(e.target.value)}/><br/><br/>
                <input type="text" placeholder="Enter Phone" onChange={(e)=>setPhone(e.target.value)}/><br/><br/>
                <input type="text" placeholder="Enter City" onChange={(e)=>setCity(e.target.value)}/><br/><br/>
                <button type="submit">Register</button>
            </form>
            {message}
        </>
    )
}

export default Register;