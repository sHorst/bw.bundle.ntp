defaults = {
    'ntp': {
        'enable_server': False,
        'servers': {
            '0.pool.ntp.org': ['iburst'],
            '1.pool.ntp.org': ['iburst'],
            '2.pool.ntp.org': ['iburst'],
            '3.pool.ntp.org': ['iburst'],
        },
        'restrictions': [
            ['default', 'kod', 'limited', 'nomodify', 'notrap', 'nopeer', 'noquery'],
            ['127.0.0.1'],
            ['-6', '::1'],
        ]
    }
}

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
