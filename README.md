# joulia-webserver
Nginx configuration files for the joulia proxy server.

## Full Nginx Quickstart
This applies if you are running Nginx within a full Nginx server, which you will
SSH into.

Build the configuration file into a single conf file by running:
```
$ python build_nginx_config.py joulia-frontend.conf joulia-frontend.conf
```

Copy `out/joulia-frontend.conf` to
`/etc/nginx/sites-available/joulia-frontend.conf` and add a symbolic link to it
in `/etc/nginx/sites-enabled/`.

Add the contents of `crontab` to the root user crontab with `sudo crontab -e`,
which will auto-renew the SSL certificates daily.

## Licensing
Copyright 2017 William Schmitt. All Rights Reserved.
