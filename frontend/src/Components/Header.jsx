import { NavLink } from "react-router-dom";
import './Header.css'
import Container from '@mui/material/Container'
import Logo from '../Assets/website-logo.png'

const Header = () => {
    const isLoggedIn = !!localStorage.getItem("access");

    const handleLogout = () =>{
        localStorage.removeItem("access");
        localStorage.removeItem("refresh");
        window.location.href = "/login";
    }
    return(
        <>
            <nav>
                <Container maxWidth="xl">
                    <div className="NavContainer">
                        <div className="navbar-brand">
                            <NavLink to="/"><img src={Logo}/></NavLink>
                        </div>
                        <ul>
                            <li><NavLink to="/">Home</NavLink></li>
                            <li><NavLink to="/about">About</NavLink></li>
                            <li><NavLink to="/university">University</NavLink></li>
                            {
                            isLoggedIn ? (
                                <>
                                    <li><NavLink to="/profile">Profile</NavLink></li>
                                    <li><button onClick={handleLogout}>Logout</button></li>
                                </>
                            ) : (
                                <>
                                    <li><NavLink to="/login">Login</NavLink></li>
                                    <li><NavLink to="/register">Register</NavLink></li>
                                </>
                            )}
                            
                            
                        </ul>
                    </div>
                </Container>
                
            </nav>
        </>
    )
}

export default Header;