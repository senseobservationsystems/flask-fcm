from flask import current_app
from pyfcm import FCMNotification

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class FCM(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("FCM_API_KEY", "")

    @property
    def service(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'fcm_service'):
                ctx.fcm_service = FCMNotification(api_key=current_app.config['FCM_API_KEY'])
            return ctx.fcm_service

    def notify_single_device(self, *args, **kwargs):
        response = self.service.notify_single_device(*args, **kwargs)
        if int(response['failure']) > 0:
            self.handle_failure()
        return True

    def notify_multiple_devices(self, *args, **kwargs):
        response = self.service.notify_multiple_devices(*args, **kwargs)
        if int(response['failure']) > 0:
            self.handle_failure()
        return True

    def handle_failure(self):
        raise Exception("Failed to send notification")
