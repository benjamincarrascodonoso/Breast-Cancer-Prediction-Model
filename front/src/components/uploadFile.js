import React, { useRef, useState } from "react";

const MAX_FILE_SIZE = 500000;

const uploadFile = ({
  label,
  updateFilesCb,
  maxFileSizeInBytes = MAX_FILE_SIZE,
  ...otherProps
}) => {

  const fileInputField = useRef(null);
  const [files, setFiles] = useState({});

  return (
      <section>
        <label>{label}</label>
        <p>Drag and drop your files</p>
        <button type="button">
          <i className="fas fa-file-upload" />
          <span> Upload {otherProps.multiple ? "files" : "a file"}</span>
        </button>
        <input
          type="file"
          ref={fileInputField}
          title=""
          value=""
          {...otherProps}
        />
      </section>      
  );
}

export default uploadFile;