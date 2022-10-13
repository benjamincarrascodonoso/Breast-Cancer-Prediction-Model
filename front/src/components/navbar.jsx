import React from 'react';
import './style.css';


function Navbar(){
    return(
        <nav className="nav">
            <a className="nav-title" href="/">Fundación Arturo López Pérez</a>
            <ul>
                <li>
                    <a href="https://www.institutoncologicofalp.cl"> Información</a>
                </li>
                <li>
                    <a href="https://www.institutoncologicofalp.cl/contacto/">Contacto</a>
                </li>
            </ul>
        </nav>
    );
}

export default Navbar