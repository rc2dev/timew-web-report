# timew-web-report

Get Timewarrior's total time per tag per week through a web API/page.

## Running with pipenv

Clone this repository and install the dependencies:

```sh
git clone https://github.com/rc2dev/timew-web-report
cd timew-web-report
pipenv install
```

Run it with `pipenv run flask run`. You may replace this command with your preferred Python HTTP server.

## Usage

To use the web interface, browse to the address given by the previous command. The API is under `/api/totals`.

## Extra columns

Besides the tags, there are two extra columns at the beginning of the table: `_all` and `_prod`:

- `_all` is the total time tracked for each week.
- `_prod` is the same but excludes the tags you configure. This is done through a custom Timewarrior config: `custom.unproductive_tags`. For example, to exclude foo and bar:

  ```sh
  timew config custom.unproductive_tags foo,bar
  ```

## License

Licensed under [GPLv3](LICENSE)

Copyright (C) 2021 [Rafael Cavalcanti](https://rafaelc.org/)
