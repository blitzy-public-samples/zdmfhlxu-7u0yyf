import { format } from 'date-fns';

/**
 * Formats a given date into a human-readable string using the 'MM/dd/yyyy' format.
 * @param date The date to be formatted
 * @returns The formatted date string
 */
export function formatDate(date: Date): string {
  return format(date, 'MM/dd/yyyy');
}