/**
 * writing the job creation functon
 */

function createPushNotificationsJobs(jobs, queue){
	if (!Array.isarray(queue)){
		throw new Error("Jobs is not an array");
	}
	for (const job of jobs){
		const job = queue.create('push_notification_code_3', contact);
		job.save((err) =>{
			if (err){
				console.error(`Notification job ${job.id} failed: ${err}`);
			}else{
				console.log(`Notification job created: ${job.id}`);
			}
		});
		job.on('progress', (progress) =>{
			console.log(`Notification job #${job.id} ${progress}% complete`)
		});
		job.on('complete', () =>{
			console.log(`Notification job ${job.id} completed`);
		});

		job.on('failed', (err) =>{
			console.log(`Notification job failed: ${err}`);
		});
	}
}
