import { createQueue } from 'kue';

const queue = createQueue();
const job = queue.create('push_notification_code', {
  phoneNumber: '2555',
  message: 'Hello B',
});

job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
}).on('complete', () => {
  console.log('Notification job completed');
}).on('ailed attempt', () => {
  console.log('Notification job failed');
}).save();
