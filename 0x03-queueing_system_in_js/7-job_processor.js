/**
 * processes incoming jobs
 */
const kue = require('kue');
const blacklist = ['4153518780', '4153518781'];
const queue = kue.createQueue();

function sendNotification(phoneNumber, message, job, done){
	job.progress(0);

	if (blacklist.includes(phoneNumber)){
		done(new Error(`Phone number ${phoneNumber} is blacklisted`));
		return;
	}
	job.progress(50).save();
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
;
	job.save();
};

queue.process('push_notification_code_2', 2, (job, done) =>{
	const phoneNumber = job.data.phoneNumber;
	const message = job.data.message;
	sendNotification(phoneNumber, message, job, done);
	done();
});
