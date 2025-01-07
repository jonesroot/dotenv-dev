# dotenv_dev
dotenv-dev package for python

# How to install from pypi
```pip3 install dotenv-dev```

# How to install from github
```pip3 install git+https://github.com/jonesroot/dotenv.git```

# How to use

```
import os
from dotenv_dev import dotenv

if __name__ == "__main__":
    dotenv.load(".env")  # Load .env file
    dotenv.load("sample.env")  # Load specifically filename or directory.env

    # Access Variable
    print(dotenv.get("DATABASE_URL", "None"))

    # Add or update variables
    dotenv.set("NEW_VAR", "Hello World")

    # Save changes to the .env file
    dotenv.save()

    # Delete variables
    dotenv.delete("NEW_VAR")

    # List all environment variables
    print(dotenv.list_all())
```

# Source code
You can find Original source code at
https://github.com/hikarine3/firstclass_dotenv
<!--
# How to test this module (This procedure is for developer of this module)

## Preparation
sudo pip install wheel;

sudo pip install twine;

## Update version
vi setup.py

## Create distribution
rm -f dist/*;
python3 setup.py sdist bdist_wheel

## Register if you haven't
https://test.pypi.org/

## Upload to Test
python3 -m twine upload --repository testpypi dist/*

## Confirm
https://test.pypi.org/project/dotenv_dev/

## Confirm by intallation
pip3 install -i https://test.pypi.org/simple/ dotenv_dev

## Deploy to production
python3 -m twine upload --repository pypi dist/*

## Confirm on Page
https://pypi.org/project/dotenv_dev/
-->