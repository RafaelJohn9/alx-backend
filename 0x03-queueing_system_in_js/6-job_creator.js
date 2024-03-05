/**
 * creating a queue with Kue
 */
const kue = require('kue');
let contact = {
	phoneNumber: '4153518780',
	message: 'This the code to verify your account'
};
const push_notification_code = kue.createQueue();

const job = push_notification_code.create('contact', contact);
job.save((err) =>{
	if (err){
	console.log(`Notification job failed`);
	}else{
	console.log(`Notification job created: ${job.id}`);
	}
});

job.on('complete', () =>{
	console.log("Notification job completed");
});
