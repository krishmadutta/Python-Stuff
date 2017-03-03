from urllib2 import urlopen

kittens = urlopen('https://twitter.com/i/moments/833744647805493248?lang=en')

f = open('C4z8tKoVcAEmbX-.jpg', 'wb')
f.write(kittens.read())
f.close()