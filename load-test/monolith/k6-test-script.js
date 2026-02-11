import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  stages: [
    { duration: '10s', target: 200 },
    { duration: '20s', target: 500 },
    { duration: '5s', target: 0 },
  ],
};

const requests = [
    ['GET', 'http://monolith-order-product:8084/orders'],
    ['GET', 'http://monolith-order-product:8084/products'],
];

export default function() {
  const responses = http.batch(requests);
  check(responses[0], { "status is 200": (res) => res.status === 200 });
  check(responses[1], { "status is 200": (res) => res.status === 200 });
  sleep(1);
}