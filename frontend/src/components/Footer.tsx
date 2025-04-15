import React from 'react';
import { Link } from 'react-router-dom';
import { Settings, Mail, Phone, MapPin } from 'lucide-react';

const Footer: React.FC = () => {
  return (
    <footer className="bg-gray-900 text-white">
      <div className="max-w-7xl mx-auto px-4 py-12 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div>
            <div className="flex items-center space-x-3">
              <Settings className="h-8 w-8 text-blue-400" />
              <span className="text-xl font-bold">PredictiveCare</span>
            </div>
            <p className="mt-4 text-gray-400">
              Advanced industrial maintenance solutions powered by machine learning.
            </p>
          </div>
          <div>
            <h3 className="text-lg font-semibold mb-4">Quick Links</h3>
            <div className="space-y-2">
              <Link to="/" className="block text-gray-400 hover:text-white">Home</Link>
              <Link to="/features" className="block text-gray-400 hover:text-white">Features</Link>
              <Link to="/about" className="block text-gray-400 hover:text-white">About</Link>
              <Link to="/dashboard" className="block text-gray-400 hover:text-white">Dashboard</Link>
            </div>
          </div>
          <div>
            <h3 className="text-lg font-semibold mb-4">Contact</h3>
            <div className="space-y-2">
              <div className="flex items-center space-x-2 text-gray-400">
                <Mail className="h-5 w-5" />
                <span>contact@predictivecare.com</span>
              </div>
              <div className="flex items-center space-x-2 text-gray-400">
                <Phone className="h-5 w-5" />
                <span>+1 (555) 123-4567</span>
              </div>
              <div className="flex items-center space-x-2 text-gray-400">
                <MapPin className="h-5 w-5" />
                <span>123 Tech Street, Innovation City</span>
              </div>
            </div>
          </div>
          <div>
            <h3 className="text-lg font-semibold mb-4">Newsletter</h3>
            <p className="text-gray-400 mb-4">Stay updated with our latest features and news.</p>
            <div className="flex">
              <input
                type="email"
                placeholder="Enter your email"
                className="px-4 py-2 rounded-l-md w-full focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-900"
              />
              <button className="bg-blue-600 px-4 py-2 rounded-r-md hover:bg-blue-700 transition-colors">
                Subscribe
              </button>
            </div>
          </div>
        </div>
        <div className="mt-12 pt-8 border-t border-gray-800 text-center text-gray-400">
          <p>&copy; {new Date().getFullYear()} PredictiveCare. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;