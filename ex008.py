num = float(input('Digite um valor em metros para a conversão: '))

km = num /1000
hm = num /100
dam = num /10
dm = num * 10
cm = num * 100
mm = num * 1000

print('{}km = {}hm = {}dam = {}m = {}dm = {}cm = {}mm'.format(km, hm, dam, num, dm, cm, mm))