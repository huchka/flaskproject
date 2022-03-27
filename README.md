# Start flask project

## Prerequesties
Installed python and created virtual environment.


## Initialize steps

Create database.

```shell
flask db stamp head
flask db migrate
flask db upgrade
```