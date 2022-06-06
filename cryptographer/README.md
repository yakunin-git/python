# Small cryptographer

## History

One day i needed to transfer my private ssh key to another computer. 
Even if i pass it in my environment, i can compromise it. Of course, one could use openssl or perhaps ansible vault. But i wanted something of my own. 
That's why i wrote this little program.

- Added use of argparse library instead of system arguments.
- Added the ability to specify keys without prompting when starting the program.

## Getting started

Before using it, you need to install the crypto library. I found it small and comfortable. More details can be found here: https://pypi.org/project/pyAesCrypt/

To install use:

```
pip install pyAesCrypt
```

The operation of the program is simple: we run the program with the first argument as the input file. 
At the output, you will get an encrypted file, to which the .aes extension will be added.
For example, if we want to encrypt a file:

```
# Encrypt the file, while deleting the original file, leaving only the encrypted one.
python cryptographer.py --clear --encrypt file_name
```

```
# Decrypt the file, while deleting the encrypted file after decryption.
python cryptographer.py --clear --decrypt file_name
```

Try it, it's easy)



