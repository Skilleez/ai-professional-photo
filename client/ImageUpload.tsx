import React, { useState} from 'react';
import { useDropzone } from 'react-dropzone';
import { useRouter } from 'next/router';

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

  const uploadImage = async () => {
    if (!file) return alert('No image selected!');
    setIsUploading(true);
    const userId = localStorage.getItem('user_id')
    console.log(userId)
    console.log(file)
    try {
      const response = await fetch('http://localhost:8000/data', {
        method: 'POST',
        headers: {
          'Content-Type': file.type,
          'X-User-Id': userId || '',
        },
        body: file,
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
        onClick={uploadImage}
        disabled={isUploading}>
          Upload
        </button>
      )}
    </div>
  );
};

export default ImageUpload