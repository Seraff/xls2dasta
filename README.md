## Installation

Run `pip3 install -r requirements.txt` in your shell.

## Usage

```
usage: convert.py [-h] -i INPUT -o OUTPUT
```

## Example

```
test
├── input.xlsx
└── results/
```

```
./convert.py -i test/input.xlsx -o test/results/
```

The xml files will be saved to `-o` folder. 

The names of the files are taken from the corresponding "Číslo žádanky" field.

```
test
├── input.xlsx
└── results/
    ├── 1288750004.xml
    ├── 3346000249.xml
    ├── 3400060648.xml
    ├── 4100937568.xml
    ├── 6849646004.xml
    ├── 7700425327.xml
    └── 8297630058.xml


```
