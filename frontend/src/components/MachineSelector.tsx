import React from 'react';

interface MachineSelectorProps {
  selectedMachine: string;
  onMachineChange: (machine: string) => void;
}

const MachineSelector: React.FC<MachineSelectorProps> = ({
  selectedMachine,
  onMachineChange,
}) => {
  const machines = [
    'Machine-H1',
    'Machine-H2',
    'Machine-M1',
    'Machine-L1',
  ];

  return (
    <select
      value={selectedMachine}
      onChange={(e) => onMachineChange(e.target.value)}
      className="block w-48 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm"
    >
      {machines.map((machine) => (
        <option key={machine} value={machine}>
          {machine}
        </option>
      ))}
    </select>
  );
};

export default MachineSelector;