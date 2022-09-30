import axios from 'axios';
import React,{Component} from 'react';
import logo from '../src/assets/falp_logo.jpg';

class App extends Component {
    // Initially, no file is selected
    state = { selectedFile: null
    };
    
    // On file select (from the pop up) update the state
    onFileChange = event => {
      this.setState({ selectedFile: event.target.files[0] });
      console.log("Update");
    };
    
    // On file upload (click the upload button)
    onFileUpload = () => {
      const formData = new FormData();

      formData.append(
        "myFile",
        this.state.selectedFile,
        this.state.selectedFile.name
      );
    
      console.log(this.state.selectedFile);
    
      // Request made to the backend api. Send formData object
      axios.post("api/uploadfile", formData);
    };
    
    // File content to be displayed after
    fileData = () => {
      if (this.state.selectedFile) {
        return (
          <div>
            <h2>File Details:</h2>
              <p>File Name: {this.state.selectedFile.name}</p> 
              <p>File Type: {this.state.selectedFile.type}</p>
              <p>
                Last Modified:{" "}
                {this.state.selectedFile.lastModifiedDate.toDateString()}
              </p>
          </div>
        );
      } else {
        return (
          <div>
            <br />
            <h4>Choose before Pressing the Upload button</h4>
          </div>
        );
      }
    };
    
    render() {
      return (
        <div>
            <img src={logo} alt="Logo" />

            <h1>
              Fundación Arturo López Pérez
            </h1>
            <h3>
              File Upload using React!
            </h3>
            <div>
                <input type="file" onChange={this.onFileChange}  />
                <button onClick={this.onFileUpload} disabled={!this.state.selectedFile}>
                  Upload!
                </button>
            </div>
          {this.fileData()}
        </div>
      );
    }
  }
 
  export default App;