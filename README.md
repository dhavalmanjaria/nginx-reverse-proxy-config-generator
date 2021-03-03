### nginx reverse proxy generator

Generate an nginx reverse proxy for subdomains and address mappings

CSV example:

a.xyz.com,172.16.0.1:8000
b.xyz.com,172.16.0.1:8001
b.xyz.com,172.16.0.2:8001

*Note*: This does not use pandas or anything so do not put in headers.

Usage:

python app.py path-to-file.csv