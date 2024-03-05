/**
 * client publisher and subscriber
 */
import * as redis from 'redis'

const client = redis.createClient();
client.connect();

client.on('error', (error) =>{
	console.log(`Redis client not connected to the server: ${error}`);
});

client.on('connect', () =>{
	console.log("Redis client connected to the server");
	client.subscribe('holberton school channel', (message, channel) =>{
		console.log(message);

		if (message === 'KILL_SERVER'){
			client.unsubscribe("holberton school channel");
			client.quit();
			return;
		}
	});
});
