import socket
from IPy import IP


def scan(target, port_num, timeout):
    converted_ip = check_ip(target)
    print(f'\n "[ - 0  Scanning Target] {target}')
    for port in range(1, port_num):
        scan_port(converted_ip, port, timeout)


def check_ip(ip):
    try:
        IP(ip)
        return (ip)
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(s):
    return s.recv(1024)


def scan_port(ip_address, port, timeout):
    try:
        sock = socket.socket()
        sock.settimeout(timeout)
        sock.connect((ip_address, port))
        try:
            banner = get_banner(sock)
            print(f"[+] Open Port {port} : {banner.decode()}")
        except:
            print(f"[+] Open Port {port}")
    except:
        pass


if __name__ == "__main__":
    targets = input(
        "[+] Enter Target's To Scan: (Split multiple targets with ,): ")
    port_num = int(
        input("[+] Enter the Number of Ports That You Want to Scan: "))
    timeout = float(input('[+] Give the Time Out... 0.5: '))
    # converted_ip = check_ip(ip_address)
    # port = 80
    if ',' in targets:
        for ip_address in targets.split(","):
            scan(ip_address.strip(' '))
    else:
        scan(targets.strip(" "), port_num, timeout)


print("FINISH")
