import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter} from 'react-router-dom';
import Routes from "./components/Routes";
import MainNavbar from "./components/MainNavbar";


function App() {
    
    return (
        <BrowserRouter>
            <MainNavbar/>
            <Routes/>
        </BrowserRouter> 
    );
}

export default App;
