import subprocess
from datetime import datetime

FOLDER_NAME = "wifi_diag_logs"

IFCONFIG = ("ifconfig en0", "ifconfig")
SYSTEM_PROFILER = ("system_profiler SPAirPortDataType", "system_profiler")


def get_diagnostics(command, subfolder_name='.'):
    now = datetime.now().strftime("%y%m%d_%H%M%S")

    process = subprocess.run(
        command[0].split(),
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    with open(f'{subfolder_name}/{command[1]}_{now}.txt', 'w') as f:
        for line in process.stdout:
            f.write(line)

    return process.stdout


def main():
    now = datetime.now().strftime("%y%m%d_%H%M%S")
    subfolder_name = (f"{FOLDER_NAME}/wifi_diag_{now}")

    subprocess.run(f'mkdir {FOLDER_NAME}'.split())
    subprocess.run(f'mkdir {subfolder_name}'.split())

    # Basic information about network interfaces
    print(get_diagnostics(IFCONFIG, subfolder_name))

    # Basic information from Wi-Fi adapter including
    # fw version, CC, PHY, supported channels, visible networks, etc.
    print(get_diagnostics(SYSTEM_PROFILER, subfolder_name))


if __name__ == '__main__':
    main()
