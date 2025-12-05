import { NavLink, Route, Router } from "react-router";
import './Header.css'
import Container from '@mui/material/Container'
import Logo from '../Assets/website-logo.png'

const Header = () => {
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
                        </ul>
                    </div>
                </Container>
                
            </nav>
        </>
    )
}

export default Header;