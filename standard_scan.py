import socket

from multiprocessing import Pool
from tqdm.auto import tqdm


def scan(arg):
    target_ip, port = arg

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    # Checks ports through sockets
    try:
        sock.connect((target_ip, port))
        sock.close()

        return port, True
    except (socket.timeout, socket.error):
        return port, False


# Standard Port Scanner
# Checks for open ports within a preset range for the Target IP
# Prints list of all detected open ports
if __name__ == '__main__':
    open_ports = []
    target_ip = input('\nTarget IP: ')
    num_process = int(input('Number of processes (max at 60): '))

    ports = range(1, 1025)
    pool = Pool(processes=num_process)

    for port, status in tqdm(pool.imap_unordered(scan, [(target_ip, port) for port in ports])):
        if status:
            open_ports.append(port)

    clean_open_ports = str(open_ports)[1:-1]
    print("Open Ports: ", clean_open_ports)
