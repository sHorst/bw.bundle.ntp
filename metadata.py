defaults = {}

if node.has_bundle("apt"):
    defaults['apt'] = {
        'packages': {
            'ntp': {'installed': True}
        }
    }

if node.has_bundle("iptables"):
    defaults += repo.libs.iptables.accept(). \
        udp(). \
        dest_port(123)
