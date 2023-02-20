url = "http://naver.com"
# print(url)
url_1 = url.replace("http://","") # 규칙1
# print(url_1)
url_1 = url_1[:url_1.index(".")]
# print(url_1)
password = url_1[:3] + str(len(url_1)) + str(url_1.count("e")) + "!"
print(password)