import ipaddress


def get_ip_details(ip_str, mask_str):
  try:
    network = ipaddress.IPv4Network(f"{ip_str}/{mask_str}", strict=False)
  except ValueError:
    return None, None
  return network, ipaddress.IPv4Address(ip_str)


def get_ip_class(ip):
  first_octet = int(ip.split('.')[0])
  if 1 <= first_octet <= 126:
    return "A"
  elif 128 <= first_octet <= 191:
    return "B"
  elif 192 <= first_octet <= 223:
    return "C"
  elif 224 <= first_octet <= 239:
    return "D"
  elif 240 <= first_octet <= 255:
    return "E"
  else:
    return None


def is_private(ip):
  return ip.is_private




# Main program
ip_input = input("Enter an IP address: ")
mask_input = input("Enter subnet mask: ")
network, ip_addr = get_ip_details(ip_input, mask_input)

if not network:
  print("Invalid IP address or subnet mask.")
  exit(1)

print(f"IP Address: {ip_addr}")
print(f"IP Class: {get_ip_class(ip_input)}")
print(f"Subnet Mask: {mask_input}")
print(f"Network Address: {network.network_address}")
print(f"Broadcast Address: {network.broadcast_address}")
hosts = list(network.hosts())
if hosts:
  print(f"First Usable Host: {hosts[0]}")
  print(f"Last Usable Host: {hosts[-1]}")
print(f"Is Private: {is_private(ip_addr)}")
