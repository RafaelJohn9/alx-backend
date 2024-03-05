/**
 * creating a job processor
 */
const kue = require('kue');
const queue = kue.createQueue();

function sendNotification(phoneNumber, message){
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
};


queue.process('contact', (job, done) => {
	const phoneNumber = job.data.phoneNumber;
	const message = job.data.message;
	sendNotification(phoneNumber, message);
});
