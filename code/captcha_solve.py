import requests 
import base64
import subprocess

host = 'http://challenge01.root-me.org/programmation/ch8/'

s = requests.Session()
res = s.get( host )

buf = res.text
start_index = buf.index('<img src="data:image/png;base64,') + len('<img src="data:image/png;base64,')
end_index   = buf.index('" /><br><br><form action')

b64Image = buf[start_index:end_index]

binaryImage = base64.b64decode(b64Image)

fd = open("image.png", 'wb')
fd.write( binaryImage )
fd.close()


result = subprocess.Popen(['gocr -i image.png'], shell=True, stdout=subprocess.PIPE).communicate()[0]

result = result.replace('\n', '')
result = result.replace(' ', '')
result = result.replace(',', '')
result = result.replace('\'', '')

res = s.post( host, data={'cametu':result})

print res.text
