import React from 'react';
import { DivideIcon as LucideIcon } from 'lucide-react';

interface MachineStatusProps {
  title: string;
  value: string;
  icon: LucideIcon;
  status: 'success' | 'warning' | 'error';
}

const statusColors = {
  success: 'bg-green-100 text-green-800',
  warning: 'bg-yellow-100 text-yellow-800',
  error: 'bg-red-100 text-red-800',
};

const MachineStatus: React.FC<MachineStatusProps> = ({ title, value, icon: Icon, status }) => {
  return (
    <div className="bg-white rounded-lg shadow p-6">
      <div className="flex items-center">
        <div className={`p-3 rounded-full ${statusColors[status]}`}>
          <Icon className="h-6 w-6" />
        </div>
        <div className="ml-4">
          <h3 className="text-sm font-medium text-gray-500">{title}</h3>
          <p className="text-lg font-semibold text-gray-900 mt-1">{value}</p>
        </div>
      </div>
    </div>
  );
}

export default MachineStatus;