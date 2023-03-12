
import urllib.parse


url = "https://10.255.1.101/api/tokenservices/"
# token = "67FC67@8192@7782@0ADF07E0179ACBBE88F2BD48134BF12A8878C1AB"

params = {'objectId': '16B5F4@4096@E6EB@5A23FA1AE2409580864B1CFF07A2E2D2AA614B28'}

print(url + urllib.parse.urlencode(params))

