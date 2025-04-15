import React from 'react';
import { 
  Activity, 
  BarChart, 
  Bell, 
  Clock, 
  Database, 
  Shield, 
  Smartphone, 
  Zap 
} from 'lucide-react';

const Features: React.FC = () => {
  const features = [
    {
      icon: Activity,
      title: "Real-time Monitoring",
      description: "Monitor machine health metrics in real-time with our advanced sensor network.",
      color: "blue"
    },
    {
      icon: BarChart,
      title: "ML-Powered Analytics",
      description: "Leverage machine learning algorithms to predict maintenance needs accurately.",
      color: "green"
    },
    {
      icon: Bell,
      title: "Smart Alerts",
      description: "Receive instant notifications when maintenance attention is required.",
      color: "red"
    },
    {
      icon: Clock,
      title: "Predictive Scheduling",
      description: "Optimize maintenance schedules based on actual equipment condition.",
      color: "purple"
    },
    {
      icon: Database,
      title: "Data Management",
      description: "Centralized storage and analysis of all maintenance-related data.",
      color: "indigo"
    },
    {
      icon: Shield,
      title: "Risk Prevention",
      description: "Identify and prevent potential equipment failures before they occur.",
      color: "yellow"
    },
    {
      icon: Smartphone,
      title: "Mobile Access",
      description: "Access your dashboard and alerts from any device, anywhere.",
      color: "pink"
    },
    {
      icon: Zap,
      title: "Performance Optimization",
      description: "Maximize equipment efficiency and reduce downtime.",
      color: "orange"
    }
  ];

  return (
    <div className="py-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-16">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            Comprehensive Maintenance Features
          </h1>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Our platform combines advanced technology with practical solutions to deliver
            a complete predictive maintenance system.
          </p>
        </div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {features.map((feature, index) => {
            const Icon = feature.icon;
            return (
              <div
                key={index}
                className="bg-white rounded-lg shadow-lg p-6 hover:shadow-xl transition-shadow"
              >
                <div className={`inline-block p-3 bg-${feature.color}-100 rounded-lg mb-4`}>
                  <Icon className={`h-6 w-6 text-${feature.color}-600`} />
                </div>
                <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
                <p className="text-gray-600">{feature.description}</p>
              </div>
            );
          })}
        </div>

        {/* Technical Specifications */}
        <div className="mt-20">
          <h2 className="text-3xl font-bold text-gray-900 mb-8 text-center">
            Technical Specifications
          </h2>
          <div className="bg-white rounded-lg shadow-lg overflow-hidden">
            <div className="grid grid-cols-1 md:grid-cols-2 divide-y md:divide-y-0 md:divide-x divide-gray-200">
              <div className="p-6">
                <h3 className="text-xl font-semibold mb-4">Sensor Capabilities</h3>
                <ul className="space-y-3 text-gray-600">
                  <li>• Temperature monitoring (±0.1°C accuracy)</li>
                  <li>• Vibration analysis (up to 20kHz)</li>
                  <li>• Rotation speed measurement</li>
                  <li>• Torque monitoring</li>
                  <li>• Power consumption tracking</li>
                </ul>
              </div>
              <div className="p-6">
                <h3 className="text-xl font-semibold mb-4">System Requirements</h3>
                <ul className="space-y-3 text-gray-600">
                  <li>• Modern web browser</li>
                  <li>• Internet connection (minimum 1Mbps)</li>
                  <li>• Compatible with all major operating systems</li>
                  <li>• Mobile-responsive design</li>
                  <li>• 24/7 system availability</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Features;