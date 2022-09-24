# Installing Postgres on ubuntu

    $ sudo apt update

    $ sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib


# Accessing Postgres Terminal

    $ sudo -u postgres psql


# Creating The Table

    $ CREATE DATABASE gp_website;


# Creating the Password

    $ CREATE USER gpadmin WITH PASSWORD 'GP$$2022';


# Altering The Roles For Django Piviledges

    $ ALTER ROLE gpadmin SET client_encoding TO 'utf8';
    $ ALTER ROLE gpadmin SET default_transaction_isolation TO 'read committed';
    $ ALTER ROLE gpadmin SET timezone TO 'UTC';


# Granting Privileges
    $ GRANT ALL PRIVILEGES ON DATABASE gp_website TO gpadmin;


# Exiting Postgres Terminal

    $ \q

# Setting Up The Environment Variables In The Root Project

    $ export DATABASE_URL=postgres://gpadmin:'GP$$2022'@127.0.0.1:5432/gp_website


