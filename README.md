# PASSWORD GENERATOR

Python modules to generate secure random passwords with letters (lowercase and uppercase), digits and symbols.

## Usage

Clone repo
```
$ git clone https://github.com/naijopkr/password-generator.git

$ cd password-generator
```

Run the script
```
$ python . <password-length> [OPTIONS]
```

The options can be `--no-symbols`, `--no-digits`, `--no-lower`, and `--no-upper`. They can be used combined to omit the character type in the generated password. An example:

```
$ python . 32 --no-symbols
OUTPUT: 3OFNRrL08uZVNqQimxEjlwZ0HuDnYIFL
```

```
$ python . 16 --no-symbols --no-upper
OUTPUT: 3cuwn7mjel7ir8ut
```
