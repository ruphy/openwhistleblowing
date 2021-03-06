from twisted.internet.defer import inlineCallbacks

from globaleaks.tests import helpers

from globaleaks.jobs.delivery_sched import DeliverySchedule

from globaleaks.jobs.notification_sched import NotificationSchedule


class TestNotificationSchedule(helpers.TestGLWithPopulatedDB):
    @inlineCallbacks
    def setUp(self):
        yield helpers.TestGLWithPopulatedDB.setUp(self)
        yield self.perform_full_submission_actions()

    @inlineCallbacks
    def test_notification_schedule(self):
        yield DeliverySchedule().operation()

        notification_schedule = NotificationSchedule()
        notification_schedule.skip_sleep = True
        yield notification_schedule.operation()

        # TODO to be completed with real tests.
        #      now we simply perform operations to raise code coverage
