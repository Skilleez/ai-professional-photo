import React from "react";

const Showcase: React.FC = () => {
  const image1: string = '/test.jpeg';
  const image2: string = 'https://static-cb2.phot.ai/bg_replacer/2025-02-24/9ed07190-f532-42ef-a57f-78e325a039f5_878835_1.webp';

  return (
    <div className="flex items-center justify-center mt-12 space-x-8">
      <img src={image1} alt="Original" className="scale-80 object-cover rounded-lg hover:scale-110 ease-in duration-200" />
      <span className="text-4xl">→</span>
      <img src={image2} alt="Generated" className="scale-80 object-cover rounded-lg hover:scale-110 ease-in duration-200" />
    </div>
  );
};

export default Showcase;
