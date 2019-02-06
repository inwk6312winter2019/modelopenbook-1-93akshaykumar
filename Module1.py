def list_ifname_ip(fout):
    ip_dic={}  
    for line in fout:
        if 'no' not in line:
            if 'nameif' in line:
                line=line.strip()
                key=line.split(" ")
                #print('nameif::',temp)
            if 'ip address' in line:
                line=line.strip()
                iptemp=line.split(" ")
                tup=(iptemp[2],)
                #print('ip address::',iptemp[2])
                ip_dic.setdefault(key[1],(iptemp[2],iptemp[3]))
           
    return ip_dic

def new_config_file():
    pass
fout=open('running-config.cfg','r')
print("The dictionary of ip addresses::",list_ifname_ip(fout))
