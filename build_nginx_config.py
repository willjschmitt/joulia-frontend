"""Builds a single nginx configuration file from joulia-frontend.conf.

Replaces all includes by directly including their contents inline in the conf.
Will recursively include any files as necessary.

`/etc/nginx` will be treated as the working directory.

Takes two arguments: infile outfile

Example usage:
    joulia-frontend.conf:
        server {
            include /etc/nginx/joulia-frontend/extra.conf;
        }

    joulia-frontend/extra.conf:
        resolver_timeout 10s;

    $ python build_config.py joulia-frontend.conf nginx.conf

    out/nginx.conf:
        server {
            resolver_timeout 10s;
        }
"""

import argparse
import os
import re


def build_nginx_config(input_filename, output_file):
    with open(input_filename) as input_file:
        for line in input_file:
            include_pattern = re.compile(
                r'include\s+/etc/nginx/(?P<filename>\S+);')
            include_match = include_pattern.search(line)
            if include_match is not None:
                include_filename = include_match.group('filename')
                build_nginx_config(include_filename, output_file)
            else:
                output_file.write(line)


def argparser():
    parser = argparse.ArgumentParser(
        description='Compiles an nginx config into a single config from'
                    ' includes.')
    parser.add_argument('input_filename', type=str,
                        help='Input file name to build config from.')
    parser.add_argument('output_filename', type=str,
                        help='Output file name to build config from.')
    args = parser.parse_args()
    return args.input_filename, args.output_filename


if __name__ == '__main__':
    input_filename, output_filename = argparser()

    output_directory = 'out'

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_path = os.path.join(output_directory, output_filename)

    with open(output_path, 'w') as output_file:
        build_nginx_config(input_filename, output_file)
