/**
 * creates  a connection with redis server
 */
import { createClient } from 'redis';

const client = createClient();

client.on('error', (eror) =>{
	console.log(`Redis client not connected to the serve: ${eror}`)
});
client.connect();

client.on('connect', () =>{
	console.log("Redis client connected to the server");
});
