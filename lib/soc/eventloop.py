class EventSubscription(object)::

    def __init__(self, uid):
        self.uid = uid

    def __hash__(self):
        return hash(self.uid)

    def notify_of_event(self, event):
        raise NotImplementedError


class EventEmitter(object):

    def __init__(self):
        self._subscriptions = set()

    def subscribe(self, subscriber, selector=None):
        subscription = EventSubscription(self.generate_uid(),
                                         subscriber,
                                         selector)
        self._subscriptions.add(subscription)
        return subscription

    def unsubscribe(self, subscription):
        self._subscriptions.remove(subscription)

    def emit(self, event):
        for subscription in subscriptions:
            if subscription.is_interested(event):
                subscription.notify_of_event(event)


