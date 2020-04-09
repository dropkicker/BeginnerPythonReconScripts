
import nmap
import sys


target = str(sys.argv[1])
ports = [21, 22, 23, 80, 443]

scan_v = nmap.PortScanner()

print("\nScanning target for ports 21, 22, 23, 80, 443....\n")

for port in ports:
    portscan = scan_v.scan(target, str(port))
    print("Port", port, " is ", portscan['scan'][target]['tcp'][port]['state'])


print("\nHost", target, " is ", portscan['scan'][target]['status']['state'])
