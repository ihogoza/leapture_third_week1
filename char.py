import urllib.request
import chardet
from chardet.universaldetector import UniversalDetector

usock = urllib.request.urlopen('http://yahoo.co.jp/')
detector = UniversalDetector()
for line in usock.readlines():
    detector.feed(line)
    if detector.done: break
detector.close()
usock.close()
print(detector.result)

rawdata = urllib.request.urlopen('http://yahoo.co.jp/').read()
# print(rawdata)

print(chardet.detect(rawdata))
# {'encoding': 'EUC-JP', 'confidence': 0.99}
# UTF-8 is an encoding system for Unicode.