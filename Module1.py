def list_ifname_ip(fout):
    ip_dic={}  
    for line in fout:
        if 'no' not in line:
            if 'nameif' in line:
                line=line.strip()
                key=line.split(" ")
                #print('nameif::',temp)
            if 'ip address' in line and '.' in line:
                line=line.strip()
                iptemp=line.split(" ")
                tup=(iptemp[2],)
                #print('ip address::',iptemp[2])
                ip_dic.setdefault(key[1],(iptemp[2],iptemp[3]))
           
    return ip_dic

def new_config_file(fout):
    fin=open('new-running-config.cfg','a+')
    for line in fout:
        if 'ip address' in line and '.' in line:
            line=line.strip()
            line=line.split()
            iptemp=line[2]
            masktemp=line[3]
            iptemp=iptemp.split('.')
            masktemp=masktemp.split('.')
            if iptemp[0] =='192' or iptemp[0] =='172':
                iptemp[0]='10'

            if (masktemp[0]=='255' and masktemp[1]=='255') or masktemp[2]=='255':
                masktemp[1]=masktemp[2]='0'

            iptemp=' ip address '+'.'.join(iptemp)+' '+'.'.join(masktemp)+'\n'
            
            fin.write(iptemp)

        else:
            fin.write(line)



    
fout=open('running-config.cfg','r')
#print("The dictionary of ip addresses::",list_ifname_ip(fout))
new_config_file(fout,)
