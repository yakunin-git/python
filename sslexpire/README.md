# Certificate date tracking

## History

When I used zabbix, I needed to keep track of the certificate expiration date of many domains. That's why this program was written. Specify the domain name as the final argument. If you need to display only the number of days in numbers, for Zabbix, you can specify the -n or --number key.

## Getting started

By default, when the program is executed, the date is displayed in a human-readable format. To get the date, just add the domain name as an argument:

```
# sslexpire.py yakunin.dev
Out:

90 days, 14:40:07.901854
```

If you need to get only numbers, for monitoring systems or for anything else, use the -n or --number key:

```
# sslexpire.py -n yakunin.dev
Out:

90
```

Also, it is possible to output in json format, use -j or --json key:

```
# sslexpire.py -j yakunin.dev
Out:

{
   "yakunin.dev": 90,
   "domain": "yakunin.dev",
   "expire": 90
}
```
