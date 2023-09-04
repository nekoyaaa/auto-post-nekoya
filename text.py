from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from time import sleep 
 
header_data = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "NjMzNjI4MTk2OTQ4MTQ4MjI0.GoN_dk.TLpD6TArfyyZm6N61jOfoouwjFItbiGuwu2F-4", 
	"host": "discordapp.com", 
	"referer1": "INVITE LINK HERE",
	"referer2": "INVITE LINK HERE",
	"referer3": "INVITE LINK HERE",
	"referer4": "INVITE LINK HERE",
	"referer5": "INVITE LINK HERE",
	"referer6": "INVITE LINK HERE",
	"referer7": "INVITE LINK HERE",
	"referer8": "INVITE LINK HERE",
	"referer9": "INVITE LINK HERE",
	"referer10": "ADDITIONAL INVITES IF YOU WANT",
	"referer11": "ADDITIONAL INVITES IF YOU WANT",
	"referer12": "ADDITIONAL INVITES IF YOU WANT",
	"referer13": "ADDITIONAL INVITES IF YOU WANT",
	"referer14": "ADDITIONAL INVITES IF YOU WANT",
	"referer15": "ADDITIONAL INVITES IF YOU WANT",
	"referer16": "ADDITIONAL INVITES IF YOU WANT",
	"referer17": "ADDITIONAL INVITES IF YOU WANT",
	"referer18": "ADDITIONAL INVITES IF YOU WANT",
	"referer19": "ADDITIONAL INVITES IF YOU WANT",
	"referer20": "ADDITIONAL INVITES IF YOU WANT",
	"referer21": "ADDITIONAL INVITES IF YOU WANT",
} 
 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def send_message(conn, channel_id, message_data): 
    try: 
        conn.request("POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data) 
        resp = conn.getresponse() 
         
        if 199 < resp.status < 300: 
            print("Submitted successfully") 
            pass 
 
        else: 
            stderr.write(f"HTTP received {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("There was an error trying to send the message\n") 
 
def main(): 
	message_data = { 
		"content": '''```prolog
NEKOYA SHOP   i have vouch and alot role trusted & mm
u can check my role in mutual server
      [SELLING FRUITS] 

| Ope ......9$        | Venom ...14$
| Tori .....7$        | Mochi ....8$
| Pika .....5$        | Gura .....2$
| Magu .....4$        | Hie ......3$
| Mera .....4$        | Zushi ....3$ 
| Suna .....3$        | Yuki......5$ 
| Ito ......3$        | Kage .....3$ 
| Paw ......3$        | Yami .....3$ 

    --COMBO FRUIT--
[1] | Venom+Ope : 22$
[2] | Venom+Ope+Mochi+Tori : 30$
[3] | Mochi+Tori : 13$
[4] | Mochi + All leg : 12$
[5] | Tori + All leg : 11$
[6] | Pika+Magu+Mera+Yami : 5$
[7] | Yuki+Hie+Suna+Zushi+Ito : 5$
[8] | Pika+Magu+Yuki : 5$

	ALL LEGEND FRUIT 7$
```
```prolog
     [ITEM] 
[HOT]Legendary chest: 0.4$/1  (minimum 5)
[COMBO] 45 Legendary chest : 15$
	15 Legendary chest : 5$
ASE : 25$
EloHammer : 10$
world ender : 25$
Qfit : 8$
Drum : 6$
Hover : 6$
Kraken Core : 3$ 
Iceborn rapier : 8$
Lucy outfit : 6$
Fruit Bag : 3$
Kraken set :
    Normal 5$
    Azure 10$

     GPO ACC lvl 575: [5$]
        ACCEPT ORDER ITEM
```
```prolog
< PAYMENT METHOD >
PAYPAL F&F | BTC | Cashapp | Zelle | STEAM GC (x1.5) | SKIN CSGO (Overpay) | YGF OR USE MM```
''',
		"tts": "false", 

	} 
 
	send_message(get_connection(), "1074569768151035904", dumps(message_data))
	sleep(4)            
	send_message(get_connection(), "1054206225178431538", dumps(message_data))
	sleep(4)     
	send_message(get_connection(), "1058672145485545512", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "911941876234473512", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "826122235160559646", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1016085678783742090", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "982640609653297174", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "988440039371452476", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "895872167181418506", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "895868689386184805", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1042546952002347039", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1042546950731481088", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "920971942369062912", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "920972407261523988", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "910423322586669088", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "910423096564019211", dumps(message_data))
	sleep(4)             
	send_message(get_connection(), "963284909747748904", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "969693378516238336", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "930580856190431252", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "930580933617270864", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "989744038880108557", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1029090773049815161", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "983733177656938586", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1036697610846744596", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1024354800931966996", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1024354872440659988", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1023723550080765982", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1023339105020547143", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1016139465539989529", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1016139465539989528", dumps(message_data))
	sleep(4)             
	send_message(get_connection(), "858811171552100372", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "858017406541496380", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "949672138711924746", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1024168737647104011", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1024168716998557776", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "997794639283241021", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "997794756828602479", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "964316368411443270", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1062230599420608572", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "980357276298792960", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "825679011694247936", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "941477299809841219", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "941477299809841220", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "941477300241842179", dumps(message_data))
	sleep(4)             
	send_message(get_connection(), "991541506609520650", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1018753143317733386", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1008035066720571596", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "877436315258474546", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1035971823541694535", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1003399082695475270", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1005092471132393472", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1005092447619137566", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "987624687246929970", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "987624686282227752", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1006471200530235513", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1023564180646789201", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1023564037386154084", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "895962842937831435", dumps(message_data))
	sleep(4)             
	send_message(get_connection(), "857236753151819816", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "930420323503964180", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "930420929178251335", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1096173481760141465", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1096494603466707096", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1008183931994124438", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1022597272560746556", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "973269012416954408", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "918557473298874378", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "918557474313883748", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "999246244788576346", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "999246787418263574", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "923046818059800616", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "923046561917837312", dumps(message_data))
	sleep(4)             
	send_message(get_connection(), "1033307744633114634", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "882085327659991185", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "963057993669283891", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "947606403579793418", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "906583408245866548", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "946139196228255804", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1102719048246099988", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1102719110879654028", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1102719173961977976", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1081554843598065824", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1003053731413233671", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1035699733865439312", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1035699992758865991", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "873734272844972102", dumps(message_data))
	sleep(4)             
	send_message(get_connection(), "818345791289819136", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "854837090697216020", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1041541750562508811", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "843523571670450176", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "804923371455250492", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "928429839185223700", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "810018198614179852", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "821471923266387998", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "878001400578195487", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "941038563779285033", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "820186415589621762", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "805210079753535518", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "940028026178109461", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "951629452956299314", dumps(message_data))
	sleep(4)             
	send_message(get_connection(), "893873762179620924", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "891374946822000700", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "842224729443794974", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "902212870056599563", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "920293563248566343", dumps(message_data))
	sleep(4)     
	send_message(get_connection(), "964921717128585327", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "846983031834411018", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "901221336335143012", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "997966986803941417", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "938914533890732072", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "870377475400679445", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "831943470532919336", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "942267349271203901", dumps(message_data))
	sleep(4)               
	send_message(get_connection(), "946410592263094292", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "932485698320228372", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1059014193132605550", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1059014440281964604", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1059014586713522196", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "967159849345515530", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "994132391545282570", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "994131542521692210", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "826938031742124046", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "954986876408827904", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1028825401641930844", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "929635362026946610", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1141481301036253254", dumps(message_data))
	sleep(4)   
	send_message(get_connection(), "1102385448241868810", dumps(message_data))
	
           
	
if __name__ == '__main__': 
	while True:    
		main()      
		sleep(15) #every 15 mins = 400
