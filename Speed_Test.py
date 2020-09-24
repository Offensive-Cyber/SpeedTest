from speedtest import Speedtest
stt = Speedtest()

download = round(stt.download())
f_d = "{:,}".format(download)
print("Your Download Is: "+f_d+" mbps")
print("================================")
upload = round(stt.upload())
f_u = "{:,}".format(upload)
print("Your Upload Is: "+f_u+" mbps")
print("================================")
stt.get_closest_servers()
PPing = (round(stt.results.ping))
print("Ping:"+str(PPing))
print("================================")
if (download<=10000000):
    print("Your Internet Is Slow")
if (download in range(10000000,50000000)):
    print("Your Internet Is Normal")
if (download in range(50000000,100000000)):
    print("Your Internet Is Fast")
if (download in range(100000000,300000000)):
    print("Your Internet Is Very Fast")
print("================================")
if (PPing == 0):
    print("Your Ping Is Insane Low. Are You Live In Datacenter Or Its Microsoft VPS?!")
if (PPing in range(1,5)):
    print("Your Ping Is Very Very Good. I Sure Your Internet Is FTTH & Its a Best FTTH Service")
if (PPing in range(5,15)):
    print("Your Ping Is Very Good. I Sure Your Internet Is FTTH Or Maybe 5G")
if (PPing in range(15,20)):
    print("Your Ping Is Nice.")
if (PPing in range(20,26)):
    print("Your Ping Is Good.")
if (PPing in range(26,30)):
    print("Your Ping Is Normal.")
if (PPing in range(30,40)):
    print("Your Ping Is Not Bad. I Sure Your Internet Is ADSL+")
if (PPing in range(30,40)):
    print("Your Ping Is High.")
if (PPing > 40):
    print("Your Ping Is Very High.")
print("")
input("Press Any Key to Close...")