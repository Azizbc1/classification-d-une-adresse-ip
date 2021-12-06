classA = IPv4Network(("0.0.0.0", "126.255.255.255"))  #
classB = IPv4Network(("128.0.0.0", "191.255.255.255"))  
classC = IPv4Network(("192.0.0.0", "223.255.255.255"))  
classD = IPv4Network(("224.0.0.0", "239.255.255.255"))  
classF = IPv4Network(("240.0.0.0 ", "255.255.255.255"))  





print(" saisir votre addresse IP =  ")
ipIn = input()
Type1 = IpType(ip)
ip =IPv4Address(ipIn)
result =" votre addresse Ip : " + ipIn +" est une addresse "+ str(Type1)
if(ip in classA):
   if (ip = " 0.0.0.0" ) 
   result = result + "  est de la classe A et non-routable"
   elif (ip = 127.0.0.1)                  
   result = result + "  est l adresse localhost et elle est de la classe A et "
elif (ip in classB):
     result = result +" est de la classe B"  
elif (ip in classC):
     result = result +"est de la classe C"
elif (ip in classC):
     result = result +"est de la classe D"
elif (ip in classC):
     result = result +"est de la classe E"
elif
     result = " vous n avez pas saisir une adresse ip " 

print(result)    
