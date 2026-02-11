import http from 'k6/http';
import { sleep, check } from 'k6';

const requests = [
    ['GET', 'http://microservice-order:8082/orders'],
    ['GET', 'http://microservice-product:8083/products'],
];

export const options = {
  stages: [
    { duration: '10s', target: 200 },
    { duration: '5s', target: 500 },
    { duration: '10s', target: 500 },
    { duration: '5s', target: 0 },
  ],
  thresholds: Object.fromEntries(
  ['http_req_duration', 'http_reqs', 'http_req_failed']
    .flatMap(metric => requests.map(request => [ `${metric}{url:${request[1]}}`, []]))),
};

export default function() {
  const responses = http.batch(requests);
  check(responses[0], { "status is 200": (res) => res.status === 200 });
  check(responses[1], { "status is 200": (res) => res.status === 200 });
  sleep(1);
}