import subprocess
from datetime import datetime

FOLDER_NAME = "wifi_diag_logs"

TASKS = {
    "ifconfig": {
        "command": "ifconfig en0",
        "filename": "ifconfig"
    },
    "system_profiler": {
        "command": "system_profiler SPAirPortDataType",
        "filename": "system_profiler"
    },
    "log_show": {
        "command": "log show --info --debug --last 1m",
        "filename": "log_show"
    },
}


def get_diagnostics(task, subfolder_name='.'):
    now = datetime.now().strftime("%y%m%d_%H%M%S")
    filename = f'{task["filename"]}_{now}.txt'

    print(task["command"])
    process = subprocess.run(
        task["command"].split(),
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    with open(f'{subfolder_name}/{filename}', 'w') as f:
        for line in process.stdout:
            f.write(line)

    return process.stdout


def main():
    # Create folder <wifi_diag_logs> if it doesn't exist
    # Create subfolder <wifi_diag_date_time> each time program runs
    now = datetime.now().strftime("%y%m%d_%H%M%S")
    subfolder_name = (f"{FOLDER_NAME}/wifi_diag_{now}")
    subprocess.run(f'mkdir {FOLDER_NAME}'.split())
    subprocess.run(f'mkdir {subfolder_name}'.split())

    # Save diagnostics inside the created subfolder
    for task in TASKS:
        get_diagnostics(TASKS[task], subfolder_name)


if __name__ == '__main__':
    main()
