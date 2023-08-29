function createPushNotificationsJobs (jobs, queue) {
  if (!Array.isArray(jobs)) throw Error('Jobs is not an array');
  for (const job of jobs) {
    const jobNotification = queue.create('push_notification_code_3', job);

    jobNotification.on('complete', () => {
      console.log(`Notification job ${jobNotification.id} completed`);
    }).on('failed', (err) => {
      console.log(`Notification job ${jobNotification.id} failed: ${err}`);
    }).on('progress', (progress) => {
      console.log(`Notification job ${jobNotification.id} ${progress}% complete`);
    });

    jobNotification.save((err) => {
      if (!err) console.log(`Notification job created: ${jobNotification.id}`);
    });
  }
}

module.exports = createPushNotificationsJobs;
