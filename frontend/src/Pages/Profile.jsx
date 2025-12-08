import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const Profile = () => {
    const [profile, setProfile] = useState(null);
    const [error, setError] = useState("");
    const nav = useNavigate();

    const handleLogout = async()=>{
            const refresh = localStorage.getItem("refresh");
            if(refresh){
                try {
                    await fetch('http://127.0.0.1:8000/api/auth/logout/',{
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({ refresh }),
                    });
                } catch (err) {
                    setError('Something went wrong!')
                }
            }
            

            localStorage.removeItem("access");
            localStorage.removeItem("refresh");
            nav('/login');
        }

    useEffect(()=>{
        const refreshAccessToken = async()=>{
            try {
                const refresh = localStorage.getItem("refresh");
                if(!refresh) return null;

                let resp = await fetch("http://127.0.0.1:8000/api/auth/refresh/",{
                    method: "POST",
                    headers: {
                        "Content-Type" : "application/json"
                    },
                    body: JSON.stringify({
                        refresh: refresh
                    })
                });
                const data = await resp.json();
                console.log(data);

                if(resp.ok){
                    localStorage.setItem("access", data.access)
                    return data.access;
                }
                else{
                    return null;
                }
            } catch (err) {
                return null
            }
            
        }

        const fetchProfile = async() => {
            const token = localStorage.getItem("access");
             if(!token){
                setError("Token Not Found");
                return; 
             }

             try {
                let resp = await fetch("http://127.0.0.1:8000/api/student/profile/", {
                    method: "GET",
                    headers: {
                        "Authorization": `Bearer ${token}`,
                        "Content-Type" : "application/json",
                    }
                });
                const data = await resp.json();

                if (resp.status === 401) {
                    const newToken = await refreshAccessToken();
                    if (!newToken) {
                        setError("Session expired. Please log in again.");
                        return;
                    }
                    resp = await fetch("http://127.0.0.1:8000/api/student/profile/", {
                        method: "GET",
                        headers: {
                            "Authorization": `Bearer ${newToken}`,
                            "Content-Type": "application/json",
                        }
                    });
                }

                if(resp.ok){
                    setProfile(data);
                    console.log("PROFILE API RESPONSE:", data);
                }else{
                    setError(data.detail || "Failed to load profile")
                }
             } catch (err) {
                setError("Something went wrong");
             }
        }


        fetchProfile();
    },[])

    return(
        <>
            {error}
            <h1>Student Profile</h1>
            {
                profile && (
                    <div>
                         <p><strong>Username:</strong> {profile.user.username}</p>
                         <p><strong>Email:</strong> {profile.user.email}</p>
                         <p><strong>Phone:</strong> {profile.phone}</p>
                         <p><strong>City:</strong> {profile.city}</p>
                    </div>
                )
            }
            <button onClick={handleLogout}>Logout</button>
        </>
    )
}

export default Profile;