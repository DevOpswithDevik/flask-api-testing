import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  vus: 10,       // 10 Virtual Users
  duration: '30s', // Test duration
};

export default function () {
  const res = http.get('http://127.0.0.1:5000/items');
  
  // Validation logic
  check(res, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
  });
  
  sleep(1); // Wait 1 second between requests
}