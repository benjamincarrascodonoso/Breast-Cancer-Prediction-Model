import React, { useState } from "react";

import logo from './assets/images/falp_logo.jpg';
import uploadFile from './components/uploadFile';
import displayInfo from "./components/displayInfo";

import './App.css';

/** 
 * Include const functions to handle the files and analysis button  
 * Investigate how to developt a conditional button => related to useState of uploadFile 
 * Modify css file to set behaviour and appearance of the app view 
 * 
 * 
 * 
 * */  

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" />

        <uploadFile className="App-File"></uploadFile>
      </header>
    </div>
  );
}

export default App;