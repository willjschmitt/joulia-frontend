# joulia-webserver
Nginx configuration files for the joulia proxy server.

## Quickstart
Copy the `joulia-frontend` directory as `/etc/nginx/joulia-frontend`. Copy
`joulia-frontend.conf` to `/etc/nginx/sites-available/joulia-frontend.conf` and
add a symbolic link to it in `/etc/nginx/sites-enabled/`.

Add the contents of `crontab` to the root user crontab with `sudo crontab -e`,
which will auto-renew the SSL certificates daily.

## Licensing
Copyright 2017 William Schmitt. All Rights Reserved.
