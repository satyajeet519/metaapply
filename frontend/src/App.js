import './App.css';
import University from './University';
import { Route, Routes } from "react-router";
import Header from './Components/Header';
import Home from './Home';
import About from './About';

function App() {
  return (
    <div className="App">
      <Header/>
      <Routes>
        <Route path="/" element={<Home/>}>Home</Route>
        <Route path="/about" element={<About/>}>About</Route>
        <Route path="/university" element={<University/>}>University</Route>
      </Routes>
    </div>
  
  );
}

export default App;
