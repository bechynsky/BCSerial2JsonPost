# BCSerial2JsonPost

This script is mainly for school project. Idea is to reduce need of computer setup. Script reads data directly from [BigClown USB Dongle](https://www.bigclown.com/doc/interfaces/serial-port-json/). Data from USB Dongle are transformed to JSON object and send to URL using POST method. It is usable for differend integration platforms like [Microsoft Flow](https://flow.microsoft.com/).

## Configuration file

URL and Serial port number or name you can put to _config.ini_ file.

```
[DEFAULT]
URL = https://...
COM = /dev/ttyUSB0
```