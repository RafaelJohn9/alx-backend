/**
 * creates  a connection with redis server
 */
import { createClient } from 'redis';
import * as redis from 'redis';

const client = createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});
client.connect()
client.on('connect', async () => {
  console.log('Redis client connected to the server');

  const data = {
    Portland: '50',
    Seatle: '80',
    'New York': '20',
    Bogota: '20',
    Cali: '40',
    Paris: '2'
  };

  const hashName = 'HolbertonSchools';
  for (const key in data) {
    const value = data[key];
    client.hSet(hashName, key, value, (error, response) => {
      if (error) {
        console.log(error);
      } else {
        console.log('Reply: 1');
      }
    });
  }
});
