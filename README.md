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

## Kubernetes Quickstart
Build the configuration file into a single conf file by running:
```
$ python build_nginx_config.py joulia-frontend.conf default.conf
```

Create a configmap to store the Nginx config:
```
kubectl create configmap joulia-frontend-configmap --from-file=out/default.conf
```

Create the kubernetes deployment and service to serve from:
```
kubectl create -f kubernetes/joulia-frontend-deployment.yaml
kubectl create -f kubernetes/joulia-frontend-service.yaml
```

## Licensing
Copyright 2017 William Schmitt. All Rights Reserved.
