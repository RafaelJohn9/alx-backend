/**
 * Writing the test for job creation
 */
const assert = require('assert');
const createPushNotificationJobs = require('./8-job');
const kue = require('kue');
const mocha = require('mocha');
const queue = kue.createQueue();


describe("createPushNotificationJobs", () => {
	before(function (done){
		queue.testMode.enter();
		done();
	});

	it('display an error message if jobs is not an array', (done) =>{
		const invalidJobs = 'not an array';

		// Call the function with invalid jobs
		try{
			createPushNotificationJobs(invalidJobs, queue)
		} catch (error) {
			// Assertion to test the error message
			assert.strictEqual(error.message, 'Jobs is not an array');
		}
		done();
	});

	it ('creates two test jobs to the queue', (done) =>{
		const validJobs = [
			{title: 'Job 1', message: 'Notification job created: 1'},
			{title: 'Job 2', message: 'Notification job created: 2'},
		];
		createPushNotificationJobs(validJobs, queue, (error) =>{
			assert.strictEqual(error, null);

			// validate which jobs are inside the queue using testMode
			const jobsInQueue = queue.testMode.jobs;
			assert.strictEqual(jobsInQueue.length, 2);
			assert.strictEqual(jobsInQueue[0].data.title, 'Job 1');
			assert.strictEqual(jobsInQueue[1].data.title, 'Job 1');
		});
		done();
	});
	after((done) =>{
		queue.testMode.exit();
		done();
	});
});
