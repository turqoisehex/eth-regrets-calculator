n = 0 #months
eth = 0 #total eth
ceth = 0 #current eth
r = 0 #block rewards
bt = 13.6 #block time in seconds. 15-13.6s historically
dif = float(11141.259137989429 * 1e11) #Nov 2021 difficulty in terahash
mhr = float(input("Hashrate in MH/s? ")) #Hashrate in MH/s
hr = mhr * 1e6 #converted to h/s
db = 86400 / bt #daily blocks
dif_list = [1506, 1509, 1935, 2666, 3103, 3239, 3164, 3194, 3361, 3554, 3385, 3240, 3061, 2512, 2398, 2408, 2036, 1809, 1928, 2112, 2195, 2186, 2227, 2449, 2465, 2530, 2455, 2041, 2046, 2276, 2188, 2318, 2299, 2358, 2438, 3263, 3396, 3692, 3730, 4615, 5362, 6288, 7262, 7689, 6334, 7405, 8523, 9226] #noqa

while n < 48:
    ceth = 0
    if n < 28: #Pre Constantinople hardfork
        r = 3 * 1.36
        bt = 14.5
    elif n >= 28: #Post
        r = 2 * 1.36
        bt = 13.4
    db = 86400 / bt
    ceth = ((hr * r * db) / (dif_list[n] * 1e11)) * 30
    eth = eth + ((hr * r * db) / (dif_list[n] * 1e11)) * 30
    n += 1
    print("After " + str(n) + " Month(s): " + str(eth) + " ETH.")
    print("ETH mined this month: " + str(ceth))
print( )
print("USD value on Nov 1 2021 (ETH @ $4300): " + '${:,.2f}'.format(eth * 4300))
print("ETH Monthly @ 11.14P difficulty (~Nov 2021): " + str(((hr * 2 * 1.36 * db) / dif) * 30))