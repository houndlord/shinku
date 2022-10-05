## Simple cross-platform tool for directory replication
Recursively and periodically copies all files from source directory to given directory preserving permissions. Operations are logged to stdout and to specified log file. Works on Linux, Win and MacOS.

## Usage 

```
python main.py /path/to/source /path/to/replica /path/to/log 5
```
Log is log file where shinku will append messages about files creation/deletion and errors. If log file does not exist it will be created. Note that on any error such permission error program will abort.

## Run tests


```
python -m pytest ./tests  
```
