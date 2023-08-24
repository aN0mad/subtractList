# subtractLists
A script to take a base file and subtract all lines in a second file from the base.

## Installation
### Pipx (Easiest)
If `pipx` is installed this is the easiest method to use as it should install the package in an automated virtualenv and add the binary to your path.
```bash
pipx install .
```

```bash
subtractLists -h
```

### Python virtualenv
If manual python virtual environment management is your thing, here you go.
```bash
python -m venv env
```
```bash
source ./env/bin/activate
```
```bash
pip install .
```

```bash
python main -hzs
```

### System wide
Not recommended unless you want dependency hell
```bash
pip install .
```

```bash
python main -hzs
```

## Usage
```
usage: subtractLists [-h] [-b BASE] [-s SUBTRACT] [--debug]

A script to modify the severity of vulnerabilities within a nessus file

options:
  -h, --help            show this help message and exit
  -b BASE, --base BASE  File to use as the base
  -s SUBTRACT, --subtract SUBTRACT
                        File subtract from the base file
  --debug               Enable debug
```

## Examples
### Using subtractLists on files of IP addresses
```bash
# subtractLists -b base.txt -s sub.txt 
2023-08-24T18:52:16.800116+0000 | INFO | Reading lines from base base.txt
2023-08-24T18:52:16.803874+0000 | INFO | Opening subtraction file sub.txt
2023-08-24T18:52:16.806452+0000 | MODIFICATION | Removing line 132.206.17.10
2023-08-24T18:52:16.806553+0000 | MODIFICATION | Removing line 104.39.130.23
2023-08-24T18:52:16.806621+0000 | MODIFICATION | Removing line 184.101.226.160
2023-08-24T18:52:16.806650+0000 | MODIFICATION | Removing line 167.250.229.68
2023-08-24T18:52:16.806998+0000 | INFO | Writing output file: base-cleaned.txt
2023-08-24T18:52:16.809633+0000 | FILEWRITE | Writing output file: base-cleaned.txt
```