export function showNotification(
  message,
  type = 'error',
  duration = 3000
) {
  let notification = document.getElementById('notification');

  if (!notification) {
    notification = document.createElement('div');
    notification.id = 'notification';
    notification.className = 'notification';
    document.body.prepend(notification);
  }

  // remove previous types
  notification.classList.remove(
    'notification--error',
    'notification--success'
  );

  notification.textContent = message;
  notification.classList.add(
    'notification--visible',
    `notification--${type}`
  );

  setTimeout(() => {
    notification.classList.remove('notification--visible');
  }, duration);
}