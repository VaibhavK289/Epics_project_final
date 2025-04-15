import React from 'react';
import { AlertCircle, Bell } from 'lucide-react';

const AlertPanel: React.FC = () => {
  const alerts = [
    {
      id: 1,
      title: 'High Temperature Warning',
      message: 'Machine H1 temperature exceeds normal range',
      severity: 'warning',
      time: '5 minutes ago',
    },
    {
      id: 2,
      title: 'Maintenance Required',
      message: 'Tool wear at 65% - schedule maintenance',
      severity: 'error',
      time: '15 minutes ago',
    },
    {
      id: 3,
      title: 'Performance Degradation',
      message: 'Rotation speed fluctuation detected',
      severity: 'warning',
      time: '1 hour ago',
    },
  ];

  return (
    <div className="bg-white rounded-lg shadow">
      <div className="p-6">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-lg font-semibold text-gray-900">Active Alerts</h2>
          <Bell className="h-5 w-5 text-gray-500" />
        </div>
        <div className="space-y-4">
          {alerts.map((alert) => (
            <div
              key={alert.id}
              className={`p-4 rounded-lg ${
                alert.severity === 'error' ? 'bg-red-50' : 'bg-yellow-50'
              }`}
            >
              <div className="flex items-start">
                <AlertCircle
                  className={`h-5 w-5 ${
                    alert.severity === 'error' ? 'text-red-500' : 'text-yellow-500'
                  }`}
                />
                <div className="ml-3">
                  <h3 className="text-sm font-medium text-gray-900">
                    {alert.title}
                  </h3>
                  <p className="mt-1 text-sm text-gray-500">{alert.message}</p>
                  <p className="mt-1 text-xs text-gray-400">{alert.time}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default AlertPanel;