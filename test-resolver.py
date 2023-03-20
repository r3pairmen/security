import socket

# Open the input file containing domain names
with open('domain_names.txt', 'r') as f:
    domain_names = [line.strip() for line in f]

# Loop through the list of domain names and resolve each one to an IP address
for domain_name in domain_names:
    try:
        ip_address = socket.gethostbyname(domain_name)
        print(f'{domain_name} resolves to {ip_address}')
    except socket.gaierror:
        print(f'Could not resolve {domain_name}')
