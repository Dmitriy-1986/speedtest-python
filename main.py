import subprocess

def get_internet_speed():
    speedtest_cmd = "speedtest-cli --simple"
    process = subprocess.Popen(speedtest_cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        return "Ошибка измерения скорости: {}".format(error.decode())
    return output.decode()

speed_info = get_internet_speed()
print(speed_info)
