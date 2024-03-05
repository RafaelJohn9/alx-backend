/**
 * publishes to a redis server
 */
import * as redis from 'redis'

const client = redis.createClient();

client.on('error', () =>{
	console.log(`Redis client not connected to the server: ${error}`)
})

client.on('connect', () =>{
	console.log('Redis client connected to the server');
});
client.connect();

function publishMessage(message, time){
	setTimeout(() =>{
		console.log(`About to send ${message}`);
	}, time);
	const channelName = 'holberton school channel';
	client.publish(channelName, message, (error, numSubscribed) =>{
		if(error){
			console.log(`Error publishing message: ${error}`);
		}else{
			console.log(message);
		}
	});
};
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);

