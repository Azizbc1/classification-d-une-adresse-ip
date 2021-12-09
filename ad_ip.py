from ipaddress import IPv4Address, IPv4Network
from ipaddress import IPv6Address, IPv6Network
from ipaddress import ip_address 

def IpType(IP: str) -> str: 
    if (ip_address(IP).is_private) 
       return "Private"
   elif (ip_address(IP).is_public)
   return "Public"
else 
return "multicast"



classA = IPv4Network(("0.0.0.0", "127.255.255.255"))  #
classB = IPv4Network(("128.0.0.0", "191.255.255.255"))  
classC = IPv4Network(("192.0.0.0", "223.255.255.255"))
classD = IPv6Network(("224.0.0.0", "239.255.255.255"))  
classF = IPv6Network(("240.0.0.0 ", "255.255.255.255"))


print(" saisir votre addresse IP =  ")
ipIn = input()
Type1=IpType(ipIn)
ip =IPv4Address(ipIn)
result =" votre addresse Ip : " + ipIn +" est une addresse "+ Type1
if(ip in classA):
   result = result + "  est de la classe A"
elif (ip in classB):
     result = result +" est de la classe B"  
elif (ip in classC):
     result = result +"est de la classe C" 
elif ipIn == "0.0.0.0":
     result = result + " ,de la classe A et non-routable"
elif ipIn == "127.0.0.1":  
   result = result + " ,localhost et  de la classe A  "
else:
     result = " vous n avez pas saisir une adresse ip "  

print(result)
