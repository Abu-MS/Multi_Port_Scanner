# multi_port_scan.py

import socket


def dns_check(domain):
    """
    DNS resolution check is done i.e. the domain name given by the user is converted into ipv4 address.
    If successfully resolved returns the ipv4 address.
    If resolution failed, it raises a socket.gaierror i.e, invalid domain or no DNS record which is caught and returns None value.
    """

    try:

        IP = socket.gethostbyname(domain)  # Successful DNS Resolution returns the IPv4 address.
        print(f'Domain IP is: {IP}')
        return IP

    except socket.gaierror:  # When domain name cannot be resolved an error is thrown and None value is returned.
        return None


def port_check(p):
    """
    This function checks whether the port given by the user falls in between valid TCP/UDP port range (0-65535).
    If true returns the port number.
    If false, then prints an error message indicating the port is out of range.
    """

    if p <0 or p > 65535:  # Port range check if out of range, notifies user.
        print(f'Port {p} is out of range.')
    else:
        return p  # If port check is valid returns the port.


def single_port_scanner(ip, port):
    """
    This function attempts to connect to the IP and port using TCP connection.
    If the port is Open, success message is print.
    If not it catches the error and notifies the user.
    The socket has a timeout of 2 seconds (set by settimeout(TIMEOUT)).
    This means the socket will wait up to 5 seconds for a response before raising a timeout error.
    """

    # Establishing a connection, (#IPv4 add, TCP connection)
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.settimeout(TIMEOUT)  # Timeout value is passed.

    try:
        c.connect((ip, port))   # (Successful Connect), port is open and returns None.
        print(f'Port {port} is open')
    except socket.timeout:   # (No Response) when the connection takes too long and exceeds the specified timeout.
        print(f'Port {port} is filtered.')
    except (socket.error, OSError) as a:    # (Connection Refused), to catch both the errors, tuples is used here.
        print(f'Port {port} is closed. Error: {a}')
    finally:
        c.close()  # closes the socket connection after the scan.


def multi_port_scanner(ip, ports):

    for port in ports:
        valid_port = port_check(port)
        if valid_port:
            single_port_scanner(ip, valid_port)


def range_scan(start, end, ip):
    for single_port in range(start, end + 1):
        if port_check(single_port):
            single_port_scanner(ip, single_port)


if __name__ == '__main__':

    TIMEOUT = 2
    domain_to_IP = dns_check(input('Enter domain: '))

    if domain_to_IP:
        user_ports = input('Enter ports (Eg: 21, 22, ...n or 21-n or 21): ')

        if ',' in user_ports:
            clean_ports = sorted(set([int(port.strip()) for port in user_ports.split(',')]))
            multi_port_scanner(domain_to_IP, clean_ports)

        elif '-' in user_ports:
            range_ports = user_ports.split('-')
            s, e = int(range_ports[0]), int(range_ports[1])
            range_scan(s, e, domain_to_IP)

        else:
            if port_check(int(user_ports)):
                single_port_scanner(domain_to_IP, int(user_ports))
    else:
        print('Domain failed to resolve.')
