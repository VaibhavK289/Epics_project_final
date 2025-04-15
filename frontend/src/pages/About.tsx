import React from 'react';
import { Users, Target, Award, Lightbulb } from 'lucide-react';

const About: React.FC = () => {
  return (
    <div className="py-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Hero Section */}
        <div className="text-center mb-16">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            About PredictiveCare
          </h1>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            We're revolutionizing industrial maintenance through advanced machine learning
            and IoT technology.
          </p>
        </div>

        {/* Mission & Vision */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-20">
          <div className="bg-blue-50 rounded-lg p-8">
            <div className="flex items-center mb-4">
              <Target className="h-8 w-8 text-blue-600 mr-3" />
              <h2 className="text-2xl font-bold text-gray-900">Our Mission</h2>
            </div>
            <p className="text-gray-600">
              To empower industries with predictive maintenance solutions that prevent
              equipment failures, reduce downtime, and optimize operational efficiency.
            </p>
          </div>
          <div className="bg-green-50 rounded-lg p-8">
            <div className="flex items-center mb-4">
              <Lightbulb className="h-8 w-8 text-green-600 mr-3" />
              <h2 className="text-2xl font-bold text-gray-900">Our Vision</h2>
            </div>
            <p className="text-gray-600">
              To become the global leader in industrial predictive maintenance,
              driving the future of smart manufacturing and Industry 4.0.
            </p>
          </div>
        </div>

        {/* Team Section */}
        <div className="mb-20">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Our Team</h2>
            <p className="text-gray-600 max-w-2xl mx-auto">
              We're a team of passionate engineers, data scientists, and industry
              experts committed to transforming industrial maintenance.
            </p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center">
              <img
                src="https://images.unsplash.com/photo-1568602471122-7832951cc4c5?ixlib=rb-1.2.1&auto=format&fit=crop&w=300&q=80"
                alt="Team Member"
                className="w-48 h-48 rounded-full mx-auto mb-4 object-cover"
              />
              <h3 className="text-xl font-semibold">Dr. John Smith</h3>
              <p className="text-gray-600">Chief Technology Officer</p>
            </div>
            <div className="text-center">
              <img
                src="https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?ixlib=rb-1.2.1&auto=format&fit=crop&w=300&q=80"
                alt="Team Member"
                className="w-48 h-48 rounded-full mx-auto mb-4 object-cover"
              />
              <h3 className="text-xl font-semibold">Sarah Johnson</h3>
              <p className="text-gray-600">Lead Data Scientist</p>
            </div>
            <div className="text-center">
              <img
                src="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?ixlib=rb-1.2.1&auto=format&fit=crop&w=300&q=80"
                alt="Team Member"
                className="w-48 h-48 rounded-full mx-auto mb-4 object-cover"
              />
              <h3 className="text-xl font-semibold">Michael Chen</h3>
              <p className="text-gray-600">IoT Solutions Architect</p>
            </div>
          </div>
        </div>

        {/* Stats Section */}
        <div className="bg-gray-50 rounded-lg p-8">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8 text-center">
            <div>
              <div className="text-4xl font-bold text-blue-600 mb-2">500+</div>
              <div className="text-gray-600">Machines Monitored</div>
            </div>
            <div>
              <div className="text-4xl font-bold text-blue-600 mb-2">98%</div>
              <div className="text-gray-600">Prediction Accuracy</div>
            </div>
            <div>
              <div className="text-4xl font-bold text-blue-600 mb-2">50+</div>
              <div className="text-gray-600">Enterprise Clients</div>
            </div>
            <div>
              <div className="text-4xl font-bold text-blue-600 mb-2">24/7</div>
              <div className="text-gray-600">Support Available</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default About;