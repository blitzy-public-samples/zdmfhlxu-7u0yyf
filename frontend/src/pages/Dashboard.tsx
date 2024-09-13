import React, { useEffect, useState } from 'react';
import { fetchRepositories } from 'frontend/src/services/api';
import WeeklyTrendChart from 'frontend/src/components/WeeklyTrendChart';
import TopRepositoriesTable from 'frontend/src/components/TopRepositoriesTable';

const Dashboard: React.FC = () => {
  const [repositories, setRepositories] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const loadRepositories = async () => {
      try {
        setIsLoading(true);
        const data = await fetchRepositories();
        setRepositories(data);
      } catch (error) {
        console.error('Error fetching repositories:', error);
        // TODO: Handle error state
      } finally {
        setIsLoading(false);
      }
    };

    loadRepositories();
  }, []);

  return (
    <div className="dashboard">
      <h1>GitHub Repository Scanner Dashboard</h1>
      {isLoading ? (
        <p>Loading...</p>
      ) : (
        <>
          <WeeklyTrendChart data={repositories} />
          <TopRepositoriesTable data={repositories} />
        </>
      )}
    </div>
  );
};

export default Dashboard;

// HUMAN ASSISTANCE NEEDED
// The current implementation assumes that the WeeklyTrendChart and TopRepositoriesTable
// components are ready to accept the repositories data as a prop named 'data'.
// Please verify if these components are implemented correctly and adjust the prop names if necessary.