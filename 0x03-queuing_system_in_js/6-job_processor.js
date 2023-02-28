import { createQueue } from 'kue';

const queue = createQueue();
const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

queue.process('push_notification_code', sendNotification('2352', 'Hello Low Balce'));
