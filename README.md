# wifi_diag
Collects useful Wi-Fi diagnostics from MacBooks.
Essentially script executes the commands from the list and saves the output to files.
It will also parse the most important information and print highlights.

## Commands
Basic information about network interfaces:
>ifconfig

Basic information from Wi-Fi adapter including fw version, CC, PHY, supported channels, visible networks, etc:
>system_profiler SPAirPortDataType

Get latest logs:
>log show --info --debug --last 1m
