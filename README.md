<p align="center">
  <img src="/logo.png" alt="Logo" width="200"/>
</p>

<div align="center">

# Polytoria.py

[Installation](#Installation)
[Usage](#Usage)
[license](#License)
[Credits](#Credits)

<p align="center">
  <img src="https://img.shields.io/badge/python-3.7+-blue.svg"/>
  <img src="https://img.shields.io/badge/license-MIT-green.svg"/>
  <img src="https://img.shields.io/github/contributors/Redlavaa/polytoria.py">
</p>

<div align="left">

# Introduction
Polytoria.py is a wrapper that lets you easily use the polytoria api inside of python.

# Installation

```bash
pip install polytoria.py
```

# Example
```python

import Polytoria
import asyncio

async def main():

  polytoria = Polytoria() # initalize the client

  user = await polytoria.user(1) # gets the user with the id 1

  print(user.username) # prints the users name

if __name__ == "__main__":
  asyncio.run(main())

```


# Usage

Everything starts with the main polytoria module, followed by the specific resource you want to access. Below are references for resources you can access.

### Polytoria.User(id)

| Attribute | Type |
| :--- | :--- |
| `id` | `int` |
| `username` | `str` |
| `description` | `str` |
| `thumbnail` | `dict` |
| `avatar` | `str` |
| `icon` | `str` |
| `playing` | `int` / `None` |
| `networth` | `int` |
| `placevisits` | `int` |
| `forumposts` | `int` |
| `assetSales` | `int` |
| `membershipType` | `str` |
| `istaff` | `bool` |
| `userroleclass` | `str` |
| `joindate` | `str` |
| `lastseen` | `str` |

### Polytoria.Item(id)

### Polytoria.Place(id)

### Polytoria.Guild(id)
