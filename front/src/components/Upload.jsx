import React, { useState } from "react";
import { useDropzone } from "react-dropzone";
import { FileServer } from "../components/fileServer";

export function Upload({ children }) {
  const [files, setFiles] = useState([]);
  const [progress, setProgress] = useState(0);
  const { getRootProps, getInputProps } = useDropzone({
    onDrop: (acceptedFiles) => onDrop(acceptedFiles, setFiles, setProgress),
    multiple: false,
    accept: ".pdf"
  });

  return (
    <>
      <h1>Uploader Example</h1>
      <div {...getRootProps()}>
        {children}
        <input {...getInputProps()} />
      </div>
      <h3>See them here</h3>
      <ul>
        <li>{progress.toFixed(0)}%</li>
        {files.map((file) => (
          <li key={file.name}>
            {file.name}, {file.type}
          </li>
        ))}
      </ul>
    </>
  );
}

function onDrop(acceptedFiles, setFiles, setProgress) {
  const file = acceptedFiles[0];
  FileServer.sendFile(file, setProgress)
    .then(() => {
      setFiles((prev) => [...prev, file]);
    })
    .catch((err) => console.error(err));
}
