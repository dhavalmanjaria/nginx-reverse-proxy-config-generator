#!/usr/bin/python3
import csv
import sys


def get_nginx_template():
	"""Generate the nginx template for one config
	"""
	domain, addr = "",""

	# Note, the string has to be this way without indentation
	nginx_config = """
server {{
        listen 80;
        listen [::]:80;

        server_name {domain};

        location / {{
                proxy_pass http://{addr};
                include /etc/nginx/conf.d/nginx-proxy-settings.conf;
        }}
}}
	"""

	return nginx_config


def get_domain_map(filepath):
	"""Read domain and ip (with port) from csv
	"""
	domain_ip_mappings = []

	with open(filepath) as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			domain_ip_mappings.append(row)

	return domain_ip_mappings

def main(filepath):

	for mapping in get_domain_map(filepath):
		domain = mapping[0]
		addr = mapping[1]

		nginx_config = get_nginx_template()

		print(nginx_config.format(domain=domain, addr=addr))


if __name__ == '__main__':

	if len(sys.argv) < 2: 
		print("Usage: python app.py <path-to-csv>")
		sys.exit(1)
	else:
		filepath = sys.argv[1]

		main(filepath)
