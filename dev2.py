import wmi
c = wmi.WMI()
wql = "Select * From Win32_USBControllerDevice"
for item in c.query(wql):
    print item.Dependent.Caption