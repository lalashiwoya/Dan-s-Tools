// FileUpload.js

import React, { useState } from 'react';
import axios from 'axios';

function FileUpload() {
    const [file, setFile] = useState(null);
    const [uploadStatus, setUploadStatus] = useState('');

    const onFileChange = event => {
        setFile(event.target.files[0]);
    };

    const onFileUpload = () => {
        if (!file) {
            alert("Please select a file to upload.");
            return;
        }
        const formData = new FormData();
        formData.append("file", file);
        
        axios.post("http://localhost:5000/upload", formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
        .then(response => {
            const blob = new Blob([response.data], { type: 'image/gif' });
            const downloadUrl = window.URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = downloadUrl;
            link.setAttribute('download', 'converted.gif'); // Set the download name
            document.body.appendChild(link);
            link.click();
            link.parentNode.removeChild(link);
            setUploadStatus('File successfully converted and downloaded!');
        })
        .catch(error => {
            console.error('Error uploading file: ', error);
            setUploadStatus('Error uploading file');
        });
    };

    return (
        <div>
            <h1>Upload a MP4 File</h1>
            <input type="file" onChange={onFileChange} accept="video/mp4" />
            <button onClick={onFileUpload}>
                Upload!
            </button>
            {uploadStatus && <p>{uploadStatus}</p>}
        </div>
    );
}

export default FileUpload;
