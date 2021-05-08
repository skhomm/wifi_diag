import subprocess
import re
from datetime import datetime

FOLDER_NAME = 'wifi_diag_logs'

TASKS = {
    'log_show': {
        'command': 'log show --info --debug --last 1m',
        'filename': 'log_show',
        'expressions': []
    },
    'ifconfig': {
        'command': 'ifconfig en0',
        'filename': 'ifconfig',
        'expressions': [
            r'ether \S+',
            r'inet6 .+',
            r'inet .+'
        ]
    },
    'system_profiler': {
        'command': 'system_profiler SPAirPortDataType',
        'filename': 'system_profiler',
        'expressions': [
            r'Card Type: .+',
            r'Firmware Version: .+',
            r'Supported Channels: .+',
        ]
    },
    'airport': {
        'command': 'airport -Is',
        'filename': 'airport',
        'expressions': [
            r'\S+ \S+ -\d+ .+'
        ]
    },
    'wdutil': {
        'command': 'wdutil info',
        'filename': 'wdutil',
        'expressions': []
    },
}


def get_diagnostics(task, subfolder_name='.'):
    now = datetime.now().strftime('%y%m%d_%H%M%S')
    filename = f"{task['filename']}_{now}.txt"

    print(f"\nExecuting: <{task['command']}>")
    process = subprocess.run(
        task['command'].split(),
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    output = process.stdout

    with open(f'{subfolder_name}/{filename}', 'w') as f:
        for line in output:
            f.write(line)

        search_results = []
        for expression in task['expressions']:
            search_results.extend(re.findall(expression, output))
        for search_result in search_results:
            print(search_result)

    return search_results


def main():
    # Create folder <wifi_diag_logs> if it doesn't exist
    # Create subfolder <wifi_diag_date_time> each time program runs
    now = datetime.now().strftime('%y%m%d_%H%M%S')
    subfolder_name = (f'{FOLDER_NAME}/wifi_diag_{now}')
    subprocess.run(f'mkdir {FOLDER_NAME}'.split())
    subprocess.run(f'mkdir {subfolder_name}'.split())

    # Save diagnostics inside the created subfolder
    for task in TASKS:
        get_diagnostics(TASKS[task], subfolder_name)


if __name__ == '__main__':
    main()
