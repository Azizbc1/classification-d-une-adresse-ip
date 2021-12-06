from ipaddress import IPv4Address, IPv4Network
from ipaddress import ip_address

def IpType(IP: str) -> str:
    return "Private" if (ip_address(IP).is_private) else "Public"



classA = IPv4Network(("10.0.0.0", "255.0.0.0"))  #
classB = IPv4Network(("172.16.0.0", "255.240.0.0"))
classC = IPv4Network(("192.168.0.0", "255.255.0.0"))



print(" saisir votre addresse IP =  ")
ipIn = input()
Type1 = IpType(ip)
ip =IPv4Address(ipIn)
result =" votre addresse Ip : " + ipIn +" est une addresse "+ str(Type1)
if(ip in classA):
   result = result + "  est de la classe A"
elif (ip in classB):
     result = result +" est de la classe B"
elif (ip in classC):
     result = result +"est de la classe C"

print(result)    