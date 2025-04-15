import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Settings } from 'lucide-react';

const Navbar: React.FC = () => {
  const location = useLocation();

  const isActive = (path: string) => {
    return location.pathname === path ? 'text-blue-600' : 'text-gray-600 hover:text-blue-600';
  };

  return (
    <nav className="bg-white shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <Link to="/" className="flex items-center space-x-3">
              <Settings className="h-8 w-8 text-blue-600" />
              <span className="text-xl font-bold text-gray-900">PredictiveCare</span>
            </Link>
          </div>
          <div className="flex items-center space-x-8">
            <Link to="/" className={`${isActive('/')} font-medium`}>Home</Link>
            <Link to="/features" className={`${isActive('/features')} font-medium`}>Features</Link>
            <Link to="/about" className={`${isActive('/about')} font-medium`}>About</Link>
            <Link to="/dashboard" className={`${isActive('/dashboard')} font-medium`}>Dashboard</Link>
            <Link to="/contact" className={`${isActive('/contact')} font-medium`}>Contact</Link>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;