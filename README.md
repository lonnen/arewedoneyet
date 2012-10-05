are we done yet?
----------------

While the Socorro team is rewriting the webapp (reporter) from php to python,
we have a goal of making the two webapps produce the same output, warts and all,
for the same urls.

To assist in achieving this, arewedoneyet.py parses its internal `websites`
variable, creating a new branch in this git repo if it doesn't exist,
and populating it with the contents of each repo. The changes are commited with
the utc timestamp as the message.

The script is pretty brittle and kind of dumb. You'll have to hand maintain a
list of resources to get for each of websites. We'll run it on a cron and use
github's awesome diff tools to determine when we're done.

e.x. https://github.com/lonnen/arewedoneyet/compare/socorro-crashstats...prod
