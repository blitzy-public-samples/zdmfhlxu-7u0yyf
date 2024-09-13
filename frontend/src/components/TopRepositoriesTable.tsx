import React, { useEffect, useState } from 'react';
import { fetchRepositories } from 'frontend/src/services/api';

const TopRepositoriesTable: React.FC = () => {
  const [repositories, setRepositories] = useState<any[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    const loadRepositories = async () => {
      try {
        const data = await fetchRepositories();
        setRepositories(data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching repositories:', error);
        setLoading(false);
      }
    };

    loadRepositories();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <table>
      <thead>
        <tr>
          <th>Repository Name</th>
          <th>Owner</th>
          <th>URL</th>
          <th>Stars Gained</th>
          <th>Total Stars</th>
        </tr>
      </thead>
      <tbody>
        {repositories.map((repo) => (
          <tr key={repo.url}>
            <td>{repo.name}</td>
            <td>{repo.owner}</td>
            <td><a href={repo.url} target="_blank" rel="noopener noreferrer">{repo.url}</a></td>
            <td>{repo.stars_gained}</td>
            <td>{repo.total_stars}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default TopRepositoriesTable;