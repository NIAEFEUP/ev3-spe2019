# Ev3 2019 - Rubick's Cube Solver

## Configuration instructions

### Windows
**1.** Install a [Linux operating system distribution](https://www.ubuntu.com/download/desktop)

**2.** Proceed to the Linux chapter

### Linux

#### Server (your computer)
**1.** Clone project and go to the project's folder:
```
git clone https://github.com/NIAEFEUP/ev3-spe2019.git
cd ev3-spe2019
```

**2.** Setup a virtual environment (Option, Recommended)

It is recommended that you use a virtual environment:
```
sudo apt install virtualenv
virtualenv -p /usr/bin/python3 venv
source ./venv/bin/activate
```
To exit the virtual environment, simply run `deactivate`.

**3.** Install python dependencies
```
pip install -r requirements.txt
```

**4.** Find your configured IP address for the bluetooth acces point, by accesing Blueman > Local Services > Network.

**5.** Edit the **serverInfo.py** file, updating the **hostName** variable with your IP address. Example, supposing that your address is *10.236.232.1*:
```python3
serverInfo = {
  'hostname': '10.236.232.1',   # IP address
  'port': '5000'
}
```

**6.** Run the server
```
python3 server.py
```

#### Client (Ev3 Bot)
**1.** If the project is not already cloned, clone it:
```
git clone https://github.com/NIAEFEUP/ev3-spe2019.git
cd ev3-spe2019
```
Otherwise, make sure your are using the latest version:
```
git pull
```

**2.** Configure the **serverInfo.py** file with the same data as the file in the server (same IP Address and same Port)

**3.** Run the program:
```
python3 solver.py
```
