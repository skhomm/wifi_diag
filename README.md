# wifi_diag
Collects useful Wi-Fi diagnostics from MacBooks.
Essentially script executes the commands from the list and saves the output to files.
It will also parse the most important information and print highlights.

## Commands available on every MacBook out of the box:
Basic information about network interfaces:
>ifconfig

Basic information from Wi-Fi adapter including fw version, CC, PHY, supported channels, visible networks, etc:
>system_profiler SPAirPortDataType SPHardwareDataType SPSoftwareDataType

Get latest logs:
>log show --info --debug --last 1m

Routing tables:
>netstat -rn

Wi-Fi network scan with information about current connection:
>/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -Is

List of known networks:
>networksetup -listpreferredwirelessnetworks en0

Another way to gather wireless information (requires sudo):
>sudo wdutil info
