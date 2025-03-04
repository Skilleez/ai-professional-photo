import { motion } from 'framer-motion';
import Navbar from '@/Navbar';
import ImageUpload from '@/ImageUpload';
import Showcase from '@/Showcase';
import { useEffect } from 'react';
import { v4 as uuidv4 } from 'uuid';

// Home Page Component
const HomePage: React.FC = () => {
  useEffect(() => {
    let storedUserId = localStorage.getItem('user_id');
    if (!storedUserId) {
      storedUserId = uuidv4();
      localStorage.setItem('user_id', storedUserId);
    }
  }, []);
  
  return (
    <div className="min-h-screen bg-black-100">
      <Navbar />
      <motion.main
        className="flex flex-col items-center justify-center mt-20"
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <p className="text-lg mb-8 text-center ">Welcome to ProfAI, the one stop shop for making Professional AI photos. Start by entering a selfie below!</p>
        <ImageUpload />
        <Showcase />
      </motion.main>
    </div>
  );
};

export default HomePage;
