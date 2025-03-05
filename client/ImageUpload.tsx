import React, { useState} from 'react';
import { useDropzone } from 'react-dropzone';
import { useRouter } from 'next/router';
import imageCompression from 'browser-image-compression';


const ImageUpload: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [isUploading, setIsUploading] = useState<boolean>(false);
  const router = useRouter();

  const { getRootProps, getInputProps } = useDropzone({
    accept: { 'image/*': ['.png', '.jpg', '.jpeg'] },
    onDrop: (acceptedFiles) => {
      if (acceptedFiles.length > 0) {
        setFile(acceptedFiles[0]);
      }
    },
  });

  const imageUpload = async () => {
    if (!file) return alert('No image selected!');
    setIsUploading(true);
    const userId = localStorage.getItem('user_id')
    console.log(userId)
    console.log(file)
    const options = {
      maxSizeMB: 1, // Compress to 1MB
      maxWidthOrHeight: 1920, // Resize if needed
    };
    
    const compressedFile = await imageCompression(file, options);
    try {
      const response = await fetch('https://ai-professional-photo-backend.vercel.app/data', {
      // const response = await fetch('http://localhost:5000/data', {
        method: 'POST',
        headers: {
          'Content-Type': file.type,
          'X-User-Id': userId || '',
        },
        body: compressedFile,
      });
      
      const url = await response.json();
      console.log(url)
      router.push('/dashboard')

    } catch (error) {
      console.error('Error uploading image:', error);
      alert('Error uploading image!');
    } finally {
      setIsUploading(false);
    }
  };


  return (
    <div className="flex flex-col items-center">
      <div {...getRootProps()} className="p-8 border-2 border-dashed border-gray-300 rounded-lg cursor-pointer">
        <input {...getInputProps()} />
        <p className="text-center">Drag & drop an image here, or click to select one.</p>
        {file && (
          <ul className="mt-4">
            <li>{file.name}</li>
          </ul>
        )}
      </div>
      {file && (
        <button 
        className="mt-4 px-4 py-2 bg-blue-500 text-white text-center rounded" 
        onClick={imageUpload}
        disabled={isUploading}>
          Upload
        </button>
      )}
    </div>
  );
};

export default ImageUpload