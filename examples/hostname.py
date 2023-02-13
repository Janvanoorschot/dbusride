from dasbus.connection import SystemMessageBus
bus = SystemMessageBus()

proxy = bus.get_proxy(
    "org.freedesktop.hostname1",
    "/org/freedesktop/hostname1"
)

print(proxy.Hostname)
