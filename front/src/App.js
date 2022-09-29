import logo from './logo.svg';

import { Upload } from '../src/components/Upload';
import './App.css';

function App() {
  return (
    <div className="App">
      <Upload>
        <button>Upload Files</button>
      </Upload>
    </div>
  );
}

export default App;
