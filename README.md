# MKVAVI

Is a simple MKV to AVI converter.

## Requirements

- ffmpeg

```bash
sudo apt update
sudo apt install ffmpeg
```


- python3

```bash
sudo apt install python3
```

## Usage

```bash
python3 conv.py -i input.mkv -o output.avi
```

## PATH
To use the script in any directory you can add it to your /usr/local/bin or ~/.local/bin/ directory without the .py extension.
Make sure to give the execution permission by doing:

```bash
sudo chmod +x conv
```
Your .bashrc or .zshrc file in your home directory needs to contain this line:

```bash
PATH=$PATH:/home/kyriefs/.local/bin
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
