# netsh wlan show profiles Ghishulal key=clear
import subprocess
metaData=subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

metaData=metaData.decode('utf-8', errors ="backslashreplace")

string="All User Profile"
ans=[]

for i in range(len(metaData.split("\n"))):
    lst=metaData.split("\n")[i]
    lst=lst.strip()
    if string in lst:
        ans.append(lst.split(':')[1].strip())

for name in ans:
    result=subprocess.check_output(['netsh', 'wlan', 'show', 'profiles',f"{name}","key=clear"])
    result=result.decode('utf-8', errors ="backslashreplace")
    string="Key Content"
    for i in range(len(result.split('\n'))):
        lst=result.split("\n")[i]
        lst=lst.strip()
        if string in lst:
            print(f"the password of {name} is {lst.split(':')[1]}")