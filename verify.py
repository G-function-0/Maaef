import sys
sys.stdout.reconfigure(encoding='utf-8')
files = ['index.html','about.html','contact.html','services.html','expertise.html','pinhole.html']
for f in files:
    with open(f, encoding='utf-8') as fh:
        c = fh.read()
    tapes = c.count('Police Tape')
    tops = []
    for line in c.split('\n'):
        if 'ftape from-' in line and 'top:' in line:
            val = line.split('top:')[1].split(';')[0].strip()
            tops.append(val)
    print(f'{f}: {tapes} tapes | positions: {tops}')
