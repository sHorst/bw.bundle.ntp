files = {}

if node.metadata.get('ntp', {}).get('enable_server', False):
    files['/etc/ntp.conf'] = {
        'source': 'etc/ntp.conf.j2',
        'content_type': 'jinja2',
        'context': {
            'cfg': node.metadata.get('ntp', {}),
        },
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
        'triggers': [
            'svc_systemd:ntpd.service:restart',
        ],
        'needs': {
            'pkg_apt:ntp'
        }
    }

    svc_systemd = {
        'ntpd.service': {
            'enabled': True,
            'running': True,
            'needs': [
                'file:/etc/ntp.conf',
            ]
        }
    }
