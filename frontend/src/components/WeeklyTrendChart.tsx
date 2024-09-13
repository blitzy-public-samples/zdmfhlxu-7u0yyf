import React from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';

interface WeeklyTrendChartProps {
  data: Array<{
    date: string;
    starsGained: number;
  }>;
}

const WeeklyTrendChart: React.FC<WeeklyTrendChartProps> = ({ data }) => {
  return (
    <LineChart width={600} height={300} data={data} margin={{ top: 5, right: 20, bottom: 5, left: 0 }}>
      <Line type="monotone" dataKey="starsGained" stroke="#8884d8" />
      <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
      <XAxis dataKey="date" />
      <YAxis />
      <Tooltip />
    </LineChart>
  );
};

export default WeeklyTrendChart;

// HUMAN ASSISTANCE NEEDED
// The current implementation assumes a specific data structure for the 'data' prop.
// If the actual data structure differs, adjustments may be needed in the component.
// Additionally, consider adding error handling and empty state rendering if no data is provided.