from time import strftime

strftime("%Y-%m-%d %H:%M:%S")


def log(log_path, log_entry, src=None):
    f = open(log_path, 'a', encoding='utf-8')

    if log_entry == 'init':
        print(strftime("%Y-%m-%d %H:%M:%S"), 'initiating replication')
        f.write(strftime("%Y-%m-%d %H:%M:%S") + ' initiating replication \n')

    if log_entry == 'mkdir':
        print(strftime("%Y-%m-%d %H:%M:%S"), 'created directory', src)
        f.write(
            strftime("%Y-%m-%d %H:%M:%S") + 'created directory ' + src + '\n')

    if log_entry == 'cp':
        print(strftime("%Y-%m-%d %H:%M:%S"), 'copyied file', src)
        f.write(strftime("%Y-%m-%d %H:%M:%S") + ' copyied file ' + src + '\n')

    if log_entry == 'rm':
        print(strftime("%Y-%m-%d %H:%M:%S"), 'removed file', src)
        f.write(strftime("%Y-%m-%d %H:%M:%S") + ' removed file ' + src + '\n')
