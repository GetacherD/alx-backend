import { createQueue } from 'kue';

const queue = createQueue();

const blackList = ['4153518780', '4153518781'];
const sendNotification = (phoneNumber, message, job, done) => {
  job.log(`Notification job #${job.id} 0% complete`);
  if (blackList.includes(phoneNumber)) {
    console.log(`Notification job #${job.id} failed: Phone number ${phoneNumber} is blacklisted`);
  } else {
    job.log(`Notification job #${job.id} 50% complete`);
  }
  done();
};
let i = 0;
while (i < 11) {
  queue.process('push_notification_code_2', (job, done) => {
    const { data } = job;
    // console.log(data)
    console.log(`Sending notification to ${data.phoneNumber}, with message: ${data.message}`);
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
  });
  i += 1;
}
