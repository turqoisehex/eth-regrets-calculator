n = 0
eth = 0
ceth = 0
r = 0
dif = float(11141.259137989429 * 1e11) #in terahash    11135.753 * 1e9
bt = float(13.6) #block time in seconds. 15-13.6s historically
mhr = 25
hr = mhr * 1e6 #converted to h/s
db = 86400 / bt #daily blocks
#print("ETH daily: " + str((hr * r * db) / dif))
#print("Daily block rewards: " + str(db * r))

dif_list = [1506, 1509, 1935, 2666, 3103, 3239, 3164, 3194, 3361, 3554, 3385, 3240, 3061, 2512, 2398, 2408, 2036, 1809, 1928, 2112, 2195, 2186, 2227, 2449, 2465, 2530, 2455, 2041, 2046, 2276, 2188, 2318, 2299, 2358, 2438, 3263, 3396, 3692, 3730, 4615, 5362, 6288, 7262, 7689, 6334, 7405, 8523, 9226] #noqa
bt_list = [14, 15, 13.6]

while n < 48:
    ceth = 0
    if n < 28:
        r = 3 * 1.36
        bt = 14.5
    elif n >= 28:
        r = 2 * 1.36
        bt = 13.4
    db = 86400 / 13.6 # bt_list[n]
    #r = r_list[n] * 1.39
    #print(r_list[n])
    #print(bt_list[n])
    #print(dif_list[n])
    ceth = ((hr * r * db) / (dif_list[n] * 1e11)) * 30
    eth = eth + ((hr * r * db) / (dif_list[n] * 1e11)) * 30
    n += 1
    print("After " + str(n) + " Month(s): " + str(eth) + " ETH.")
    print("ETH mined this month: " + str(ceth))
print( )
print("USD value on Nov 1 2021 (ETH @ $4300): " + '${:,.2f}'.format(eth * 4300))
print("ETH Monthly @ 11.14P difficulty (~Nov 2021): " + str(((hr * 2 * 1.36 * db) / dif) * 30))