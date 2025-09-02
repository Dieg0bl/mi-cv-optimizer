import { render, screen } from '@testing-library/react';
import App from './App';

test('renders CV optimizer title', () => {
  render(<App />);
  const titleElement = screen.getByText(/Optimiza tu CV/i);
  expect(titleElement).toBeInTheDocument();
});
