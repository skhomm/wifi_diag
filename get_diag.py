import subprocess


IFCONFIG = ("ifconfig en0", "ifconfig")
SYSTEM_PROFILER = ("system_profiler SPAirPortDataType", "system_profiler")


def get_diagnostics(command):
    process = subprocess.run(
        command[0].split(),
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    with open(f'{command[1]}.txt', 'w') as f:
        for line in process.stdout:
            f.write(line)

    return process.stdout


# Basic information about network interfaces
print(get_diagnostics(IFCONFIG))

# Basic information from Wi-Fi adapter including
# fw version, CC, supported PHY, channels, visible networks, etc.
print(get_diagnostics(SYSTEM_PROFILER))
