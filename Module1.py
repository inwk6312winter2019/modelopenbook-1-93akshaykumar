def list_ifname_ip(fout):
    '''
    INPUT
    fout - File of the object read in method

    OUTPUT

    RETURN
    ip_dic - Dictionary of names as key and ip address, ip mask as value 
    '''
    ip_dic={}  
    for line in fout:
        if 'no' not in line:
            line=line.strip()
            if 'nameif' in line:   
                key=line.split(" ")
            if 'ip address' in line and '.' in line:
                iptemp=line.split(" ")
                tup=(iptemp[2],)
                ip_dic.setdefault(key[1],(iptemp[2],iptemp[3]))
           
    return ip_dic

def new_config_file(fout,fin):
    '''
    INPUT
    fout - File of the object read in method
    fin - File of the object to write

    OUTPUT

    RETURN
    True - If All operations went Fine 
    '''
    fout.seek(0)
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
    return True

def get_access_list(fout):
    '''
    INPUT
    fout - File of the object read in method
    
    OUTPUT
    transit_access_in - access list of type transit_access_in
    global_access - access list of type global_access
    fw_management_access_in -  access list of type fw_management_access_in

    RETURN
    
    '''
    fout.seek(0)
    transit_access_in=[]
    global_access=[]
    fw_management_access_in=[]
    
    for line in fout:
        line=line.strip()
        if 'access-list' in line:
            if 'transit_access_in' in line:
                transit_access_in.append(line)
            elif 'global_access' in line:
                global_access.append(line)
            elif 'fw-management_access_in' in line:
                fw_management_access_in.append(line)
    print('access list for transit_access_in::\n',transit_access_in)
    print('access list for global_access::\n',global_access)
    print('access list for fw_management_access_in::\n',fw_management_access_in)
    



try:
    fout=open('running-config.cfg','r')
    fin=open('new-running-config.cfg','a+')
    print("The dictionary of ip addresses::",list_ifname_ip(fout))
    if new_config_file(fout,fin):
        print('New File Created Successfully')
    else:
        print('Not Able to Create New File File')
    get_access_list(fout)
except:
    print('Something Went wrong While working with Files.Please check files have proper permissions')
 

    
