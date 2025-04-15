import React from 'react';
import { Link } from 'react-router-dom';
import { Activity, BarChart, Shield, Clock } from 'lucide-react';

const Home: React.FC = () => {
  return (
    <div>
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-blue-600 to-blue-800 text-white">
        <div className="max-w-7xl mx-auto px-4 py-20 sm:px-6 lg:px-8">
          <div className="text-center">
            <h1 className="text-4xl md:text-6xl font-bold mb-6">
              Smart Industrial Maintenance
            </h1>
            <p className="text-xl md:text-2xl mb-8 text-blue-100">
              Predict and prevent equipment failures before they happen
            </p>
            <Link
              to="/dashboard"
              className="inline-block bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-blue-50 transition-colors"
            >
              View Dashboard
            </Link>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl font-bold text-gray-900">Why Choose PredictiveCare?</h2>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div className="text-center p-6">
              <div className="inline-block p-4 bg-blue-100 rounded-full mb-4">
                <Activity className="h-8 w-8 text-blue-600" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Real-time Monitoring</h3>
              <p className="text-gray-600">
                Track machine performance and health metrics in real-time
              </p>
            </div>
            <div className="text-center p-6">
              <div className="inline-block p-4 bg-green-100 rounded-full mb-4">
                <BarChart className="h-8 w-8 text-green-600" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Predictive Analytics</h3>
              <p className="text-gray-600">
                ML-powered predictions for maintenance scheduling
              </p>
            </div>
            <div className="text-center p-6">
              <div className="inline-block p-4 bg-purple-100 rounded-full mb-4">
                <Shield className="h-8 w-8 text-purple-600" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Failure Prevention</h3>
              <p className="text-gray-600">
                Prevent costly breakdowns and extend equipment life
              </p>
            </div>
            <div className="text-center p-6">
              <div className="inline-block p-4 bg-orange-100 rounded-full mb-4">
                <Clock className="h-8 w-8 text-orange-600" />
              </div>
              <h3 className="text-xl font-semibold mb-2">24/7 Alerts</h3>
              <p className="text-gray-600">
                Instant notifications for critical maintenance needs
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="bg-gray-50 py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl font-bold text-gray-900 mb-8">
            Ready to optimize your maintenance operations?
          </h2>
          <Link
            to="/contact"
            className="inline-block bg-blue-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-blue-700 transition-colors"
          >
            Get Started Today
          </Link>
        </div>
      </section>
    </div>
  );
};

export default Home;