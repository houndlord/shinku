from time import strftime

strftime("%Y-%m-%d %H:%M:%S")

def log(log_path, log_entry, src = None):
    f = open(log_path, 'w')

    if log_entry == 'init':
        print(strftime("%Y-%m-%d %H:%M:%S"), 'initiating replication')
        f.write(strftime("%Y-%m-%d %H:%M:%S") + 'initiating replication \n')

    if log_entry == 'mkdir':
        print(strftime("%Y-%m-%d %H:%M:%S"), 'creating directory', src)
        f.write(strftime("%Y-%m-%d %H:%M:%S") + 'creating directory ', src + '\n')

    if log_entry == 'cp':
        print(strftime("%Y-%m-%d %H:%M:%S"), 'copying file', src)
        f.write(strftime("%Y-%m-%d %H:%M:%S") + ' copying file ' + src +'\n')
 
    if log_entry == 'rm':
        print(strftime("%Y-%m-%d %H:%M:%S"), 'removing file',  src)
        f.write(strftime("%Y-%m-%d %H:%M:%S") + ' removing file ' + src + '\n')

    