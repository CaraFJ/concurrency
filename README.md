# compare concurrent methods

## example
- example is based on example given in https://realpython.com/python-concurrency/ , made modifications to help better understanding.

### example background:
for each url, download the contents from it and get the size.

Notes: 
Using a Session object from requests can accelerate process!

It is possible to simply use get() from requests directly, but creating a Session object allows requests to do some fancy networking tricks and really speed things up.

### Result
assume with session if not mentioned
- without io: 35.08285307884216 seconds / 34.32341909408569 seconds  (run 2 times)
- io with print: 35.89998483657837 seconds
- io with log: 48.693845987319946 seconds / 37.30951499938965 seconds
- io without session: 72.58061599731445 seconds / 86.126944065094 seconds

