# Munin Api Layer

An API layer for Munin-Node, dynamically returns the requested images generated by the RRD database tool. Designed to serve images and data to an iOS application for Server monitoring.

## Getting Started

Clone this repo and start a virtual Environment

### Prerequisites

A instllation of Munin that can be installed via the command line on any linux m,achine by running the following:
```
apt-get install Munin
apt-get install Munin-Node
```
Python3 --Version 3.3 or greater
Venv or virtualenv (VirtualEnv is deprecated in later editions of python)

### Installing

This project can be cloned via the link [LINK] https://github.com/jadotis/Munin-Api.git

```
git clone https://github.com/jadotis/Munin-Api.git
```
The virtualEnvironment can then be instantiated via the command:
```
source venv/bin/activate
```
You can then run the project via the command:
```
python3 or python<version> manage.py runserver <PortNumber>
```
On some machines there can be issues with the version of Django,
Which can be fixed by installing Django with the virtualenv active:
```
python<version> -m pip install django
```

I have included a shell script to update the project at your convenience:
```
chmod 777 run.sh
./run.sh
```
The project is configured to run on 127.0.0.1

## Authors

* **James Otis** - 
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

--
