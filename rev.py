from multiprocessing.dummy import Pool
import requests
import json
import socket
import pyfiglet
from ansi.colour import fg, bg

class Reverse_IP():
    def banner(self):
        b = "Treverse IP"
        gr = "Coded By : 4dsec \nThanks To Lolic0de For Cut Function \nTeam:0x33 Troya Crew | Ghost Coder | Clan_X12\nMasukkan List Berformat IP\nRepo ini Open Source,Silahkan Jika Ingin Mengembangkan\n[Note:Jangan Cuma Recode Nama Doang Y Pler]"
        pyfiglet.print_figlet(b,'rounded')
        print("\n" + gr)

    def revip(self,ip):
        r = requests.get(f"https://tr0yacrew.herokuapp.com/1/{ip}")
        j = json.loads(r.text)
        if "error" in r.text:
            print(bg.red("[BAD]") + fg.white(" [") + fg.blue(">>>") + fg.white("] ") + fg.yellow(ip))
        else:
            result = json.loads(r.text)
            print(bg.green("[GOOD]") + fg.white(" [") + fg.blue(">>>") + fg.white("] ") + fg.green("{} {} [>>>] Domains".format(self.cut(str(ip) ,15), len(result))))
            for domain in j:
                open('Resultz.txt', 'a').write('http://' + domain + "\n")
    
    def cut(self, ip='',leng=False):
            if leng == False:
                ret = ip
            else:
                length_string = len(ip)
                if length_string > leng:
                    ret = ip[0:leng]
                else:
                  nephi = leng-length_string
                  ret = ip+' '*nephi
            return str(ret)
                    
try:
    rev = Reverse_IP()
    rev.banner()
    ip = [i.strip() for i in open(str(input("List : "))).readlines()]
    thr = Pool(int(input("Thread: ")))
    thr.map(rev.revip,ip)
except IOError:
    print(fg.red("File Not Found"))
except FileNotFoundError:
    print(fg.red("File Not Found"))
except KeyboardInterrupt:
    print(fg.red("Keyboard Interrupt Detected"))
