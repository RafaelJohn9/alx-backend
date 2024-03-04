/**
 * creates  a connection with redis server
 */
import { createClient } from 'redis';
import * as redis from 'redis'
import { promisify } from 'util'

const client = createClient();

client.on('error', (eror) =>{
	console.log(`Redis client not connected to the serve: ${eror}`)
});
client.connect();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

client.on('connect', () =>{
	console.log("Redis client connected to the server");
});

async function setNewSchool(schoolName, value) {
	await setAsync(schoolName);
	console.log('Value set:', value);
};

async function  displaySchoolValue(schoolName){
	const reply = await getAsync(schoolName);
	console.log(`Value for ${schoolName} ${reply}`);
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
