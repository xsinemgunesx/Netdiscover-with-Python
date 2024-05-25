import argparse
import scapy.all as scapy

class ARPing():

    def __init__(self):
        print("ARPing başlatıldı...")

    def get_user_input(self):
        parser = argparse.ArgumentParser() #argumentParse sınıfından parser objesi
        parser.add_argument('-i','--ipaddress', type = str, help="IP adresinizi girmelisiniz.")
        #kullanıcının bize verdiği args almak içins
        args = parser.parse_args()
        #print(args.ipaddress)
        if args.ipaddress != None:
            return args
        else:
            print("ip adresini, -i argümanıyla giriniz")

    def arp_istegi(self,ip):
        arp_request_packet = scapy.ARP(pdst=ip) #kullanıcıdan aldığımız ARP paketi
        broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")#yayın yaptığımız adres
        combined_packet = broadcast_packet/arp_request_packet

        #tuple'dır ve kısa yazımın açılımı
        (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout = 1)
        answered_list.summary() #özetini gösterir

        #arp ping yapma kısa yazım aşağıda
       # ans, unans = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst="192.168.1.0/24"), timeout=2)

if __name__ == "__main__": # python kodları import edilmediyse main olarak kaydedilir
    arp_ping = ARPing() ##obje oluşturma
    kullanici_girdisi = arp_ping.get_user_input()
    arp_ping.arp_istegi(kullanici_girdisi.ipaddress) # bu sayede kullanıcı arp tablosunu görebilir
