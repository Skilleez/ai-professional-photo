import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import Navbar from '@/Navbar';


const Dashboard: React.FC = () => {
  const [images, setImages] = useState<string[]>([]);
  const router = useRouter();

  useEffect(() => {
    const fetchImages = async () => {
      try {
        const userId = localStorage.getItem('user_id');
        if (!userId) {
          alert('User ID missing. Please upload an image first.');
          router.push('/');
          return;
        }

        const response = await fetch('http://localhost:8000/images', {
          headers: { 'x-user-id': userId },
        });

        if (!response.ok) throw new Error('Failed to fetch images');

        const data = await response.json();
        const d = data.split(",")
        const list: string[] = []
        for (const entry of d) {
          const m = entry.match(/(http.*?\.webp)/g)
          list.push(m[0])
        }
        

        console.log(list)
        console.log(typeof list)
        setImages(list);
      } catch (error) {
        console.error('Error fetching images:', error);
      }
    };

    fetchImages();
  }, [router]);

  const downloadImage = async (url: string) => {
    try {
      const response = await fetch(url);
      const blob = await response.blob();
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = 'downloaded_image.jpg';
      link.click();
    } catch (error) {
      console.error('Error downloading image:', error);
    }
  };

  return (
    <div className="min-h-screen bg-black-100 p-8">
      <Navbar />
      <h1 className="text-5xl font-bold mb-8 text-center p-8 ">Image History</h1>
      {images.length === 0 ? (
        <p>No images found. Upload some images to get started!</p>
      ) : (
        <div className="grid grid-cols-3 gap-8">
          {images.map((url, index) => (
            <div key={index} className="shadow-lg rounded-lg overflow-hidden">
              <img src={url} alt="Generated" className="w-full h-64 object-cover" />
              <button
                className="w-full py-2 bg-blue-500 text-white mt-2"
                onClick={() => downloadImage(url)}
              >
                Download
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Dashboard;
