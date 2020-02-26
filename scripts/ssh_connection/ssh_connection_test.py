import paramiko

ps = ["1","2"]

def start_connection():
    for ip in range(1,255):
        for pswd in ps:
            u_name = 'root'
            port = 22
            r_ip = '10.10.10.%d' % (ip)
            print (r_ip)
            try:
                myconn = paramiko.SSHClient()
                myconn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                session = myconn.connect(r_ip, username =u_name, password=pswd, port=port,timeout=5)
                print (r_ip, 'deneniyor')
            except:
                continue
            if session is None:
                remote_cmd = 'hostname'
                (stdin, stdout, stderr) = myconn.exec_command(remote_cmd)
                print((stdout.read()).replace("\n",""),  r_ip, pswd)
                myconn.close()
                break


if __name__ == '__main__':
    start_connection()
