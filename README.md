# ctf-tools
Some simple data manipulation tools for Infosec CTF

## binary.py
Process a file containing strings representing binary with configurable start and stop bits, as well as byte size. Prints the newly rearranged bytes/bits as well as the ASCII, decimal, and hexadecimal values.

At this time the majority of the settings are hard-coded.

Usage:

```
./binary.py file.txt
```

Sample input:

```
1111000011010001110001011100
```

## binasc.py
Processes a file containing strings representing binary bytes separated by white space, and displays the ASCII equivalent. Does not make any attempt to avoid trying to print non-printable characters.

Usage:

```
./binasc.py file.txt
```

Sample input:

```
00110101 10111001 00011100
```

## hexasc.py
Processes a file containing strings representing hexadecimal bytes separated by white space, and displays the ASCII equivalent. Does not make any attempt to avoid trying to print non-printable characters.

Usage:

```
./hexasc.py file.txt
```

Sample input:

```
0A 32 4F 7E
```

## md5.py
Calculates the md5 hash of a string. *Important note:* this is different than placing the string in a file and using `md5sum`!

Usage:

```
./md5.py string
./md5.py "a string with spaces"
./md5.py "a string \"with\" quotes"
```
