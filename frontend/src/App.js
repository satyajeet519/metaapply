import './App.css';
import University from './Pages/University';
import { Route, Routes } from "react-router-dom";
import Header from './Components/Header';
import Home from './Pages/Home';
import About from './Pages/About';
import Login from './Pages/Login';
import Profile from './Pages/Profile';
import Register from './Pages/Register';
import PrivateRoute from './Pages/PrivateRoute';

function App() {
  return (
    <div className="App">
      <Header/>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/about" element={<About/>}/>
        <Route path="/profile" element={<PrivateRoute><Profile/></PrivateRoute>} />
        <Route path="/university" element={<University/>}/>
        <Route path="/login" element={<Login/>}/>
        <Route path="/register" element={<Register/>}/>
      </Routes>
    </div>
  
  );
}

export default App;
