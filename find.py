import sys
import socket
from dns import resolver
from dns import reversename

listfile = 'list.txt' if len(sys.argv) <= 1 else sys.argv[1]

ips = []
with open(listfile, 'r') as f:
    for l in f:
        if l.startswith('#'):
            continue
        domain = l.strip().replace(
            'http://',
            '').replace(
            'https://',
            '').replace(
            '/',
            '')
        ip = socket.gethostbyname_ex(domain)
        ips.extend(ip[2])

ips = set(ips)

for ip in ips:
    addr = reversename.from_address(ip)
    hosts = resolver.query(addr, "PTR")
    if len(hosts) == 1:
        print('%s: %s' % (addr, hosts[0]))
    else:
        print(hosts)
#     print socket.gethostbyaddr(ip)
