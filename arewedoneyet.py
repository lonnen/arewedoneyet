import datetime
import subprocess

websites = {
    "dev": {
        "host": "http://crash-stats-dev.allizom.org/",
        "resources":  [
            "products/Firefox",
            "status"
        ],
    },
    "stage": {
        "host": "http://crash-stats.allizom.org/",
        "resources":  [
            "products/Firefox",
            "status"
        ],
    },
}

for name, attributes in websites.iteritems():
    host = attributes['host']
    subprocess.call(['git', 'checkout', '-b', name])
    for resource in attributes['resources']:
        f = open(resource, 'w')
        f.write("%s%s" % (host, resource))
        f.close()
    iso8601_now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
    subprocess.call(['git', 'commit', '-am', '%s' % (iso8601_now)])
