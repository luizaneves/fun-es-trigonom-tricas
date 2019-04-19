m = float(input('Digite uma distância em metros: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print('''Em {:.0f}m tem {:.0f}km 
{:.0f}hm, {:.0f} dam, {:.0f} dm, {:.0f} cm e {:.0f}mm'''.format(m,km,hm,dam,dm,cm,mm))

