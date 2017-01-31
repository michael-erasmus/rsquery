# rsquery

A simple command line sql client for Redshift, powered by Docker, Python and Pandas

## Setup

You should have [Docker installed](https://docs.docker.com/engine/installation/)

To run the rsquery container you'll need to have a `.env` file in your $HOME directory with the following env variables

```
  REDSHIFT_ENDPOINT=xxx.us-east-1.redshift.amazonaws.com
  REDSHIFT_DB_NAME=foo_db
  REDSHIFT_DB_PORT=5439
  REDSHIFT_USER=foo_user
  REDSHIFT_PASSWORD=foo_password
```

To build the container, run

```bash
make build
```

## Run a query

```
echo "select count(*) from users" | bin/query
```

Or pass in a file

```
cat my_query.sql | bin/query
```
