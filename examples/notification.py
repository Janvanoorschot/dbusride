from dasbus.connection import SessionMessageBus
bus = SessionMessageBus()

proxy = bus.get_proxy(
    "org.freedesktop.Notifications",
    "/org/freedesktop/Notifications"
)

id = proxy.Notify(
    "", 0, "face-smile", "Hello World!",
    "This notification can be ignored.",
    [], {}, 0
)

print("The notification {} was sent.".format(id))