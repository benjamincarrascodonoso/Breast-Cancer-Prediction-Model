import axios from 'axios';
import React,{Component} from 'react';
import Navbar from './components/navbar';
import logo from '../src/assets/falp_logo.jpg';
import user from '../src/assets/icons/usuario.png';
import load from '../src/assets/icons/loading.png';


import './App.css';

class App extends Component {
    
  // Initially, no file is selected
    state = { 
      selectedFile: null,
    };
    
    // On file select (from the pop up) update the state
    onFileChange = event => {
      this.setState({ selectedFile: event.target.files[0] });
      console.log("Update");
    };
    
    // On file upload (click the upload button)
    onFileUpload = () => {
      // window.location.href="https://youtu.be/ZpAoeQBzfr8?t=82"

      /** axios async response post & fetch 
       * https://dev.to/tutrinh/basic-using-async-and-await-with-axios-ad5
      */

      /** 
       * Meanwhile read const data from a json. Set up conditional return and div with 
       * display information
      */

      /*
      const formData = new FormData();

      formData.append(
        this.state.selectedFile,
        this.state.selectedFile.name
      );
    
      console.log(this.state.selectedFile);
    
      // Request made to the backend api. Send formData object
      axios.post("api/uploadfile", formData);
      */
    };

    
    // File content to be displayed after
    fileData = () => {
      if (this.state.selectedFile) {
        return (
          <div className='yesInfo'>
            <img src={user} className="imgPatient" alt="paciente"/>
            <h2>File Details:</h2>
              <p>File Name: {this.state.selectedFile.name}</p> 
              <p>File Type: {this.state.selectedFile.type}</p>
              <p>Last Modified:{" "}{this.state.selectedFile.lastModifiedDate.toDateString()}</p>
          </div>
        );
      } else {
        return (
          <div className='nonInfo'>
            <br/>
            <img src={user} className="imgPatient" alt="paciente"/>
            <h1>Sin Datos</h1>
          </div>
        );
      }
    };
    
    render() {
      return (
        <div>
            <Navbar className="nav"/>
            <table>
              <tr>
                <th className='Left'>
                  <img src={logo} alt="Logo"/>

                  <h1> Fundación Arturo López Pérez </h1>
                  <h3> Sistema de detección de cáncer de mama </h3>

                  <form>
                    <label className='inputButton' onChange={this.onFileChange} htmlFor="input">
                    <input name='' type="file" id='input' hidden/>
                    Seleccionar Archivo
                    </label>
                    <br></br>

                    <button className='uploadButton' onClick={this.onFileUpload} disabled={!this.state.selectedFile} startIcon={<load/>}>
                      Iniciar Análisis
                    </button> 
                    <br></br>
                  </form>
                </th>
                <th className='Right'>
                {this.fileData()}
                </th>
              </tr>
            </table>
        </div>
      );
    }
  }
 
  export default App;