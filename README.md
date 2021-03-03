### nginx reverse proxy generator

Generate an nginx reverse proxy for subdomains and address mappings

CSV example:

```
a.xyz.com,172.16.0.1:8000
b.xyz.com,172.16.0.1:8001
b.xyz.com,172.16.0.2:8001
```

*Note*: This does not use pandas or anything so do not put in headers.

Usage:

python app.py path-to-file.csv

### How to use:

1. Make sure you have an nginx conf file at `/etc/nginx/conf.d/nginx-proxy-settings.conf`. This path is hardcoded, but you can change it in the nginx config template

2. Run the command as directed:

`python app.py path-to-file.csv`

This will generate an nginx config file and output to stdout. Copy that output to a file in /etc/nginx/sites-enabled/your-file.conf. Overriding default.conf will do. 

3. Finally do `sudo nginx -s reload` to reload configuration.

