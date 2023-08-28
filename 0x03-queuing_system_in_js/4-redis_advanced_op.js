import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', function () {
  console.log('Redis client connected to the server');
});

client.on('error', function (error) {
  console.log(`Redis client not connected to the server: ${error}`);
});

const holbertonSchoolsData = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2
};

for (const [key, value] of Object.entries(holbertonSchoolsData)) {
  client.hset('HolbertonSchools', key, value, print);
}
// client.hmset("HolbertonSchools", holbertonSchoolsData, print);

client.hgetall('HolbertonSchools', (err, value) => {
  if (err) {
    console.log(err);
    throw err;
  }
  console.log(value);
});
