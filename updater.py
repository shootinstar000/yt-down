import os
import sys
print("WELCOME TO TERMUX DOWNLOAD MANAGER")
if os.path.isfile("/data/data/com.termux/files/home/YTD_Android.py"):
    with open("/data/data/com.termux/files/home/YTD_Android.py") as u:
        update = u.readline().rstrip()
    with open("/data/data/com.termux/files/home/main.py") as m:
        main = m.readline().rstrip()
    if update==main:
        os.remove("/data/data/com.termux/files/home/YTD_Android.py")
        print("\nNo New Update...\n")
        code = "python '/data/data/com.termux/files/home/main.py' '" +sys.argv[1] +"'"
        os.system(code)
    else:
        print("\nUpdating......\n")
        os.remove("/data/data/com.termux/files/home/main.py")
        os.system("mv YTD_Android.py main.py")
        os.system("sleep 5")
        print("\nUpdated..!\n")
        code = "python '/data/data/com.termux/files/home/main.py' '" +sys.argv[1] +"'"
        os.system(code)
    m.close()
    u.close()
else:
    print("New Mode")
    url = "https://github.com/DrDelin/Youtube-Downloader-Android/blob/master/YTD_Android.py"
    import requests
    from bs4 import BeautifulSoup
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    ver = soup.find(id="LC1")
    update = ver.text.strip()
    with open("/data/data/com.termux/files/home/main.py") as m:
        main = m.readline().rstrip()
    if update==main:
        print("\nNo New Update...\n")
        code = "python '/data/data/com.termux/files/home/main.py' '" +sys.argv[1] +"'"
        os.system(code)
    else:
        print("\nUpdating......\n")
        open('/data/data/com.termux/files/home/noobjection.temp', 'a').close()
        os.system("sh refresh.sh")
        code = "python '/data/data/com.termux/files/home/main.py' '" +sys.argv[1] +"'"
        os.system(code)
    m.close()
    
quit()
