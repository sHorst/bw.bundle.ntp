@metadata_processor
def add_apt_packages(metadata):
    if node.has_bundle("apt"):
        metadata.setdefault('apt', {})
        metadata['apt'].setdefault('packages', {})

        metadata['apt']['packages']['ntp'] = {
            'installed': True,
        }

    return metadata, DONE


@metadata_processor
def add_iptables_rules(metadata):
    if node.has_bundle("iptables"):
        # we are available on all interfaces
        metadata += repo.libs.iptables.accept(). \
            state_new(). \
            udp(). \
            dest_port(123)

    return metadata, DONE
