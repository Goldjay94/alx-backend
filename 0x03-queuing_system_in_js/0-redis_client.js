import { createClient } from 'redis';
const client = createClient();

function redisConnect () {
  client.on('connect', function () {
    console.log('Redis client connected to the server');
  }).on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });
}

redisConnect();
