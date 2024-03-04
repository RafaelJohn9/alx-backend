/**
 * creates  a connection with redis server
 */
import { createClient } from 'redis';
import * as redis from 'redis'

const client = createClient();

client.on('error', (eror) =>{
	console.log(`Redis client not connected to the serve: ${eror}`)
});
client.connect();

client.on('connect', () =>{
	console.log("Redis client connected to the server");
});

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
};

function  displaySchoolValue(schoolName){
	client.get(schoolName, (err, reply) =>{
		if (err){
			console.error(err);
		}else{
			console.log(`Value for ${schoolName}: ${reply}`);
		}
	});
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
