import json
import re

# Enable logs structure into nginx server configuration.
# log_format full_log '$remote_addr - $remote_user [$time_local] '
#                     '"$request" $status $bytes_sent '
#                     '"$http_referer" "$http_user_agent" "$gzip_ratio" '
#                     '"$request_length" "$request_time" '
#                     '"$connection_requests"';

regex = r'(?P<client_ip>\d+.\d+.\d+.\d+)\s+(?P<auth_name>.+?)\s+' \
        '(?P<proxy_ip>.+?)\s+\[(?P<date>.+?)\]\s+\"(?P<method>GET|POST|HEAD|PUT|DELETE|OPTIONS)\s+' \
        '(?P<request>.+?)\s+(?P<http_version>.+?)\"\s+(?P<response>\d+)\s+(?P<size>\d+)\s+\"' \
        '(?P<referer>.+?)\"\s+\"(?P<user_agent>.+?)\"\s+\"(?P<gzip>.+?)\"\s+\"' \
        '(?P<request_length>\d+)\"\s+\"(?P<request_time>.+?)\"\s+\"(?P<connection_request>\d+)\"'


def parse_logs(r):
    print(json.dumps({'client': r.group('client_ip'),
                      'auth_name': r.group('auth_name'),
                      'proxy_ip': r.group('proxy_ip'),
                      'date': r.group('date'),
                      'method': r.group('method'),
                      'request': r.group('request'),
                      'http_version': r.group('http_version'),
                      'response': r.group('response'),
                      'size': r.group('size'),
                      'referer': r.group('referer'),
                      'user_agent': r.group('user_agent'),
                      'gzip': r.group('gzip'),
                      'request_length': r.group('request_length'),
                      'request_time': r.group('request_time'),
                      'connection_request': r.group('connection_request')
                      }, sort_keys=True, indent=1))


def get_parse_default():
    with open('/Users/yakuninv.vasily/docker/nginx/logs/access.log', 'r') as file:
        for line in file:
            r = re.search(regex, line)
            if r:
                parse_logs(r)


def get_parse_statistic():
    get_file_lines_count = 0
    get_passed_line_count = 0
    get_failed_line_count = 0
    with open('/Users/yakuninv.vasily/docker/nginx/logs/access.log', 'r') as file:
        for line in file:
            get_file_lines_count += 1
            r = re.search(regex, line)
            if r:
                get_passed_line_count += 1
                parse_logs(r)
            else:
                get_failed_line_count += 1
    print('\n')
    print('-' * 50)
    print('Total lines: ' + str(get_file_lines_count))
    print('Parsed lines: ' + str(get_passed_line_count))
    print('Error parsed lines: ' + str(get_failed_line_count) + '\n')


get_parse_default()
