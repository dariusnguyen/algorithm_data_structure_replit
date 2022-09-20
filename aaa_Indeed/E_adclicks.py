'''
The people who buy ads on our network don't have enough data about how ads are working for their business. They've asked us to find out which ads produce the most purchases on their website.

Our client provided us with a list of user IDs of customers who bought something on a landing page after clicking one of their ads:

Each user completed 1 purchase.
completed_purchase_user_ids = [
"3123122444","234111110", "8321125440", "99911063"]

And our ops team provided us with some raw log data from our ad server showing every time a user clicked on one of our ads:

ad_clicks = [
#"IP_Address,Time,Ad_Text",
"122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
"96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
"122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
"82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
"92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
"122.121.0.155,2017-01-01 03:18:55,Buy wool coats for your pets",
"92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]

The client also sent over the IP addresses of all their users.

all_user_ips = [
#"User_ID,IP_Address",
"2339985511,122.121.0.155",
"234111110,122.121.0.1",
"3123122444,92.130.6.145",
"39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
"8321125440,82.1.106.8",
"99911063,92.130.6.144"
]

Write a function to parse this data, determine how many times each ad was clicked, then return the ad text, that ad's number of clicks, and how many of those ad clicks were from users who made a purchase.

Expected output:

1 of 2 2017 Pet Mittens
0 of 1 The Best Hollywood Coats
3 of 4 Buy wool coats for your pets

purchases: number of purchase IDs
clicks: number of ad clicks
ips: number of IP addresses
*/
'''
'''
parse ad clicks
split by ',' --> dict key: ad_text, value: list of ipaddress
loop through dict
for each key, total users  = count of ips
if ip is in completed purchase user ids, 


{
    '2017 Pet Mittens': [96.3.199.11, 92.130.6.145]
    
}
'''

def parseAdClicks(adClicks, completed_purchase_user_ids, all_user_ips):
    adClicksDict = {}
    for i in range(len(adClicks)):
        ip, time, adText = adClicks[i].split(',')
        if adClicksDict.get(adText) is None:
            adClicksDict[adText] = [ip]
        else:
            adClicksDict[adText].append(ip)
            
    ipToUser = {}
    for i in range(len(all_user_ips)):
        user, ip = all_user_ips[i].split(',')
        ipToUser[ip] = user
    
    for k, v in adClicksDict.items():
        totalclicks = 0
        numpurchases = 0
        for ip in v:
            totalclicks += 1
            user = ipToUser.get(ip, None)
            if user and user in completed_purchase_user_ids:
                numpurchases += 1
        print(f'{numpurchases} of {totalclicks} {k}')
        

ad_clicks = [
#"IP_Address,Time,Ad_Text",
"122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
"96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
"122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
"82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
"92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
"122.121.0.155,2017-01-01 03:18:55,Buy wool coats for your pets",
"92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]

all_user_ips = [
#"User_ID,IP_Address",
"2339985511,122.121.0.155",
"234111110,122.121.0.1",
"3123122444,92.130.6.145",
"39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
"8321125440,82.1.106.8",
"99911063,92.130.6.144"
]

completed_purchase_user_ids = [
"3123122444","234111110", "8321125440", "99911063"]

parseAdClicks(ad_clicks, completed_purchase_user_ids, all_user_ips)