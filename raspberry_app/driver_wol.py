from wakeonlan import send_magic_packet


def send_wol_packet(mac_address):
    send_magic_packet(mac_address)
    print(f'{mac_address}: send packet')