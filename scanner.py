import socket
import concurrent.futures
from tqdm import tqdm

OPEN_PORTS = []


def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host, port))
        s.close()
        OPEN_PORTS.append(port)
        print(f"Порт {port} открыт")
    except:
        pass


def scan_ports(host, ports):
    global OPEN_PORTS
    OPEN_PORTS = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = [executor.submit(scan_port, host, port) for port in tqdm(ports)]


def main():
    host = '127.0.0.1'
    ports = range(1, 1025)

    scan_ports(host, ports)

    print("Открытые порты:")
    for port in OPEN_PORTS:
        print(port)


if __name__ == "__main__":
    main()