import React from 'react';

import logo from './assets/images/falp_logo.jpg';
import uploadFile from './components/uploadFile';

import './App.css';

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
