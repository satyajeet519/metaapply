import './App.css';
import University from './Pages/University';
import { Route, Routes } from "react-router";
import Header from './Components/Header';
import Home from './Pages/Home';
import About from './Pages/About';
import Login from './Pages/Login';
import Profile from './Pages/Profile';
import Register from './Pages/Register';

function App() {
  return (
    <div className="App">
      <Header/>
      <Routes>
        <Route path="/" element={<Home/>}>Home</Route>
        <Route path="/about" element={<About/>}>About</Route>
        <Route path="/profile" element={<Profile/>}>Profile</Route>
        <Route path="/university" element={<University/>}>University</Route>
        <Route path="/login" element={<Login/>}>Login</Route>
        <Route path="/register" element={<Register/>}>Register</Route>
      </Routes>
    </div>
  
  );
}

export default App;
