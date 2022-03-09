import idna
import idna.codec

# For typical usage, the encode and decode functions will take a domain name argument and perform a conversion to A-labels or U-labels respectively.

idna.encode('ドメイン.テスト')
# b'xn--eckwd4c7c.xn--zckzah'
print(idna.decode('xn--eckwd4c7c.xn--zckzah'))
# ドメイン.テスト

# You may use the codec encoding and decoding methods using the idna.codec module:



print('домен.испытание'.encode('idna'))
# b'xn--d1acufc.xn--80akhbyknj4f'
print(b'xn--d1acufc.xn--80akhbyknj4f'.decode('idna'))
# домен.испытание

# print('domain.test'.encode('idna'))