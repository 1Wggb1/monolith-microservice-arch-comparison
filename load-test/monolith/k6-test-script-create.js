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
    {
        method: 'POST',
        url: 'http://monolith-order-product:8084/products',
        body: JSON.stringify({ name: "PC", description: "Computer", createAt: Date.now(), price: 99.98 }),
        params: { headers: { 'Content-Type': 'application/json' } }
    },
    {
        method: 'POST',
        url: 'http://monolith-order-product:8084/orders',
        body: JSON.stringify({ productIds: [100, 200, 200], userId: 1, createAt: Date.now(), total: 200.99 }),
        params: { headers: { 'Content-Type': 'application/json' } }
    },
];

export default function() {
  const responses = http.batch(requests);
  check(responses[0], { "status is 200": (res) => res.status === 201 });
  check(responses[1], { "status is 200": (res) => res.status === 201 });
  sleep(1);
}