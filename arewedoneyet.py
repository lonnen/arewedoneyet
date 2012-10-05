import datetime
import subprocess

from websites import websites

# set up the branches if they don't exist
for name in websites.iterkeys():
    try:
        subprocess.check_output(['git', 'checkout', '-b', name])
        subprocess.call(['git', 'rm', '-f', 'content/*'])
        subprocess.call(['git', 'commit', '-am', 'init'])
    except subprocess.CalledProcessError:
        pass

subprocess.call(['git', 'checkout', 'master'])

for name, attributes in websites.iteritems():
    host = attributes['host']
    subprocess.call(['git', 'checkout', name])
    for resource in attributes['resources']:
        subprocess.call(['git', 'rm', '-f', 'content/*'])
        filename = 'content/' + resource.replace('/', '_')
        f = open(filename, 'w')
        subprocess.call(['curl', "%s%s" % (host, resource)], stdout=f)
        f.close()
        subprocess.call(['git', 'add', '-f', filename])
    iso8601_now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
    subprocess.call(['git', 'commit', '-am', '%s' % (iso8601_now)])
    subprocess.call(['git', 'push', 'origin', name])

subprocess.call(['git', 'checkout', 'master'])
