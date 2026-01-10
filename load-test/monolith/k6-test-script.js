import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  vus: 100,
  duration: '10s',
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