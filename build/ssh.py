import paramiko

def return_gpu_info(GPU_Name:str, Username:str, Password:str):
    Port = int("2223"+GPU_Name[-1])
    Results = [False, False, False, False,
               False, False, False, False,
               False, False,
               False, False, False, False,
               False, False, False, False]

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    ssh_client.connect(hostname="202.120.45.56", port=Port, username=Username, password=Password)
    stdin, stdout, stderr = ssh_client.exec_command('nvidia-smi | grep \"0MiB\" -B 1 | grep \"Off\"')
    stdout_info = stdout.read().decode("utf8")
    available_info_list = stdout_info.split("\n")[:-1]
    for available_info in available_info_list:
        Results[int(GPU_Name[-1])*2-2+int(available_info[4])] = True
    ssh_client.close
    
    return Results

if __name__ == "__main__":
    r = return_gpu_info(GPU_Name="GPU02", Username="taowentao", Password="uhbuhbuhb")
    for i in r:
        print(i)