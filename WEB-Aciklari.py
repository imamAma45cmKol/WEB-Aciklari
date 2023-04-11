import os


os.system("clear")
banner="""

██████╗ ██╗   ██╗ ██████╗ ███╗   ███╗███████╗██████╗ 
██╔══██╗╚██╗ ██╔╝██╔═══██╗████╗ ████║██╔════╝██╔══██╗
██████╔╝ ╚████╔╝ ██║   ██║██╔████╔██║█████╗  ██████╔╝
██╔══██╗  ╚██╔╝  ██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗
██████╔╝   ██║   ╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║
╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝

@1_omer.bck 
omerbocek1606@gmail.com
                                                     
"""

print(banner)

print("1 : WEB BİLGİ \n2 : NİKTO \n3 : SKİPFİSH \n4 : WAPİTİ \n5 : NMAP \n6 : UNİCORNSCAN \n7 : EXPLOİT \n8 : MSF")

lang = input("Yapmak İstediğiniz İşlemi Seçin : ")

match lang:
    case "2":
        ip_adres=input("Hedef İP : ")
        print("Yükleniyor...")
        os.system("nikto -host {}".format(ip_adres))
    case "1":
        print("http/https Olmadan!")
        url=input("Hedef URL : ")
        print("Yükleniyor...")
        os.system("whatweb {}".format(url))
    case "3":
        print("http/https Olmadan!")
        url=input("Hedef URL : ")
        kayıt=input("Dosya Adı : ")
        print("Yükleniyor...")
        os.system("skipfish -o {0} {1}".format(kayıt , url))
    case "4":
        ip_adres=input("Hedef İP : ")
        print("Yükleniyor...")
        os.system("wapiti -u {}".format(ip_adres))
    case "5":
        ip_adres=input("Hedef İP : ")
        kayıt=input("Dosya Adı : ")
        dizin=input("Kayıt Edilecek Dizini Girin : ")
        os.system("Nmap -sS -sV -oA {3}{1} --script vuln {0}".format(ip_adres,kayıt,dizin))
    case "6":
        os.system("unicornscan")
        ip_adres=input("Hedef İP : ")
        print("Yükleniyor...")
        os.system("unicornscan {}/24".format(ip_adres))
    case "7":
        sploit=input("Exploit : ")
        os.system("searchsploit {}".format(sploit))
    case "8":
        os.system("msfconsole")
        

    case _:
        
        print("Boş Bırakamazsınız !")


        

