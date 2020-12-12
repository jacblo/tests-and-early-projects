import urllib

url = "https://us04web.zoom.us/j/3333333333"
while True:
    file = urllib.request.urlopen(url)
    
    w = False
    for line in file:
        decoded_line = line.decode("utf-8")
        x = decoded_line.lower().find("<input type=\"hidden\" id=\"data_is_iframe_verified\" value=\"true\">")
        if x != -1:
            print("online")
            w = True
            break
    if w:
        break
    else:
        print("nope")

input("press enter to exit")