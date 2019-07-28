Ik-cli

[![Build Status](https://travis-ci.org/MerleLiuKun/ik-cli.svg?branch=master)](https://travis-ci.org/MerleLiuKun/ik-cli)

## Introduction

This application provides some common command line tools for me.

## Usage

You can use main command to show all subcommands.

```shell script
ik_cli --help
# the echo are:
Usage: ik_cli [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --verbose  Enable verbose mode.
  --help         Show this message and exit.

Commands:
  network  get ip info

```

Now you can use `network` subcommand to get point ip info from `ip.sb`.

```shell script
ik_cli network 8.8.8.8

# the echo is:
IP: 8.8.8.8
ASN: 15169
CONTINENT_CODE: NA
COUNTRY: United States
COUNTRY_CODE: US
LATITUDE: 37.751
LONGITUDE: -97.822
ORGANIZATION: Google LLC
TIMEZONE: America/Chicago
```