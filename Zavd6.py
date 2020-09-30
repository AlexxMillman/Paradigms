h= int(input('hour='))
m= int(input('minute='))
s= int(input('second='))

a=360/43200
s= s + (m*60) + (h*3600)
corner = a * s
print('%5.2f' % corner  + ' Градусів')