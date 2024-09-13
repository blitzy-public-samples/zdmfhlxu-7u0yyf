import { AxiosInstance, create } from 'axios';
import { Repository } from '../schema/repository';

const apiClient: AxiosInstance = create({ baseURL: process.env.REACT_APP_API_URL });

export const fetchRepositories = async (): Promise<Repository[]> => {
  try {
    const response = await apiClient.get('/repositories');
    return response.data;
  } catch (error) {
    console.error('Error fetching repositories:', error);
    throw error;
  }
};

export const generateReport = async (): Promise<string> => {
  try {
    const response = await apiClient.post('/reports');
    return response.data.url;
  } catch (error) {
    console.error('Error generating report:', error);
    throw error;
  }
};

export const sendEmailNotification = async (reportId: string): Promise<string> => {
  try {
    const response = await apiClient.post('/notifications', { reportId });
    return response.data.status;
  } catch (error) {
    console.error('Error sending email notification:', error);
    throw error;
  }
};

// HUMAN ASSISTANCE NEEDED
// The confidence level for the sendEmailNotification function is below 0.8.
// Please review and adjust the implementation if necessary.
// Consider adding error handling, input validation, or additional parameters if required.