a = [1,2,3,4,5,"f",6,7,8]

for item in a:
    if type(item) == type('str'):
        break   #[eitar mane hocche je loop ta ke thamiye dewa]
    else:
        print(item)

print("--------------------------------------------------------------")

for item in a:
    if type(item) == type('str'):
        continue   #[eitar mane hocche je, codition mille take ignore kre shamne jawa]
    else:
        print(item)