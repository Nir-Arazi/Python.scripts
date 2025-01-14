import nmap

IP = input ("what ip wuld you like to scan ")
PORT = input ("what port wuld you like to scan ")
scan = nmap.PortScanner()
scan.scan(IP,PORT)
print ("scan info", scan.scaninfo())

for i in scan.all_hosts():
    print(f"\nhosts: {i}") 
    print (f"\nstutes: {scan[i].state()}")
for protocul in scan[i].all_protocols():
    print(f"\nprotocol: {protocul}")
port = scan[i][protocul].keys()
for ports in port :
    print(f"port: {ports} | state: {scan[i][protocul][ports]['state']}")
