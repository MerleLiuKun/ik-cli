Ik-cli

[![Build Status](https://travis-ci.org/MerleLiuKun/ik-cli.svg?branch=master)](https://travis-ci.org/MerleLiuKun/ik-cli)

## Introduction

This application provides some common command line tools for me.

## Install

You can use pip to install this tool.

```shell script
pip install ik-cli
```

## Usage

You can use main command to show all subcommands.

```shell script
ik_cli -h
# the echo are:
Usage: ik_cli [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --verbose  Enable verbose mode.
  -h, --help     Show this message and exit.

Commands:
  ip  get ip info
  time  timestamp convert
```

#### ip info 

Now you can use `ip` subcommand to get point ip info from `ip.sb`.

```shell script
ik_cli ip 8.8.8.8

# the echo is:
IP:              8.8.8.8
ASN:             15169
CONTINENT_CODE:  NA
COUNTRY:         United States
COUNTRY_CODE:    US
LATITUDE:        37.751
LONGITUDE:       -97.822
ORGANIZATION:    Google LLC
TIMEZONE:        America/Chicago
```

If you want get your host ip, you can do as follows:

```shell script
ik_cli ip -m host

# echo
Your IP:  192.168.0.2
Method:   UDP
```

#### time convert

Now you can change string time (like: `2019-8-1` or `2019-8-2 12.09.11`) to timestamp.
Or change timestamp (like `1565007913`) to string time. 

Notice: the timezone depend on your machine's timezone.

```shell script
ik_cli time '2019-08-05 13:14:11' 
# echo 
Timestamp:  1564982051
Time:       2019-08-05 13:14:11

ik_cli time 1564982100 
# echo
Timestamp:  1564982100
Time:       2019-08-05 13:15:00
```
