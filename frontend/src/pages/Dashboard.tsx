import React, { useState } from 'react';
import { LineChart, AlertCircle, Settings, Activity, Thermometer, RotateCw, PenTool as Tool, Wind } from 'lucide-react';
import MachineStatus from '../components/MachineStatus';
import LiveChart from '../components/LiveChart';
import AlertPanel from '../components/AlertPanel';
import MachineSelector from '../components/MachineSelector';

const Dashboard: React.FC = () => {
  const [selectedMachine, setSelectedMachine] = useState('Machine-H1');

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <div className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8 flex justify-between items-center">
          <div className="flex items-center space-x-3">
            <Settings className="h-8 w-8 text-blue-600" />
            <h1 className="text-2xl font-bold text-gray-900">Machine Dashboard</h1>
          </div>
          <MachineSelector 
            selectedMachine={selectedMachine} 
            onMachineChange={setSelectedMachine} 
          />
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8">
        {/* Status Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
          <MachineStatus
            title="Machine Status"
            value="Operational"
            icon={Activity}
            status="success"
          />
          <MachineStatus
            title="Temperature"
            value="45.2°C"
            icon={Thermometer}
            status="warning"
          />
          <MachineStatus
            title="Rotation Speed"
            value="1750 RPM"
            icon={RotateCw}
            status="success"
          />
          <MachineStatus
            title="Tool Wear"
            value="65%"
            icon={Tool}
            status="warning"
          />
        </div>

        {/* Main Content */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Charts Section */}
          <div className="lg:col-span-2 space-y-6">
            <div className="bg-white rounded-lg shadow p-6">
              <div className="flex items-center justify-between mb-4">
                <h2 className="text-lg font-semibold text-gray-900">Sensor Readings</h2>
                <div className="flex items-center space-x-2">
                  <span className="text-sm text-gray-500">Live Updates</span>
                  <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
                </div>
              </div>
              <LiveChart />
            </div>

            <div className="bg-white rounded-lg shadow p-6">
              <h2 className="text-lg font-semibold text-gray-900 mb-4">Performance Metrics</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="p-4 bg-gray-50 rounded-lg">
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-gray-500">Air Temperature</span>
                    <Thermometer className="h-4 w-4 text-blue-500" />
                  </div>
                  <p className="text-2xl font-semibold mt-2">24.5°C</p>
                </div>
                <div className="p-4 bg-gray-50 rounded-lg">
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-gray-500">Process Temperature</span>
                    <Thermometer className="h-4 w-4 text-orange-500" />
                  </div>
                  <p className="text-2xl font-semibold mt-2">45.2°C</p>
                </div>
                <div className="p-4 bg-gray-50 rounded-lg">
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-gray-500">Torque</span>
                    <Wind className="h-4 w-4 text-purple-500" />
                  </div>
                  <p className="text-2xl font-semibold mt-2">35.8 Nm</p>
                </div>
                <div className="p-4 bg-gray-50 rounded-lg">
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-gray-500">Tool Wear</span>
                    <Tool className="h-4 w-4 text-red-500" />
                  </div>
                  <p className="text-2xl font-semibold mt-2">65%</p>
                </div>
              </div>
            </div>
          </div>

          {/* Alerts Panel */}
          <div className="lg:col-span-1">
            <AlertPanel />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;