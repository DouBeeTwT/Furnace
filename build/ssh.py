import paramiko
import time

class SSH_Client(object):
    def __init__(self, ip, port, username, password, timeout=30, flag_ftp=False) -> None:
        self.ip =ip
        self.port = port
        self.username = username
        self.password = password
        self.timeout = timeout
        self.flag_ftp = flag_ftp

        # Create a ssh client
        self.ssh = paramiko.SSHClient()
        if self.flag_ftp:
            # Create a file transport client
            self.transport = paramiko.Transport(sock=(self.ip, self.port))

    def connect(self):
        try:
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname=self.ip, port=self.port, username=self.username, password=self.password)
            self.channel = self.ssh.invoke_shell()
            time.sleep(5)
            stdout = self.channel.recv(1024).decode()
            if self.flag_ftp:
                self.transport.connect(username=self.username, password=self.password)
        except:
            return "Connect Failed"
        return stdout
        
        
    def close(self):
        if self.flag_ftp:
            self.transport.close()
        self.channel.close()
        self.ssh.close()
    
    def cmd(self, command, sleep=0.5):
        self.channel.send(command+"\n")
        time.sleep(sleep)
        stdout = self.channel.recv(1024).decode("utf8")
        return stdout
    
    def cuda_available_test(self):
        Results = [False, False, False, False, False, False, False, False, False,
                   False, False, False, False, False, False, False, False, False]
        cuda_avilable_list = self.cmd(command='nvidia-smi | grep \"0MiB\" -B 1 | grep \"Off\"').split("\n")[:-1]
        for available_info in cuda_avilable_list:
            Results[int(self.port[-1])*2-2+int(available_info[4])] = True
        return Results