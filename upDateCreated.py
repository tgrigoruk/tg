#! python3
# changes file Date Created to date&time specified in file name
# eg abcd20170203_153025efg.mp4

import os, re, sys, shutil
from pathlib import Path

dir = Path.cwd()
if not (dir / 'processed').exists():
    os.mkdir(dir / 'processed')
filelist = os.listdir(dir)  # list(dir.glob('*.mp4'))
fileNameRegex = re.compile(r'''
    (\d{4})         # YYYY
    (\s|-|_|\.)?    # separator   
    (\d{2})         # MM
    (\s|-|_|\.)?    # separator
    (\d{2})         # DD
    (\s|-|_|\.)?    # separator
    (\d{6}|\d{,4})  # TIME (hhmmss)
    ''', re.VERBOSE)

errors = 0
processed = 0
print(f'Processing files in {str(dir)}')
for f in filelist:
    # filename:Path ==> f.stem dot f.suffix
    filename = f.rpartition('.')
    if '' in filename or f == Path(sys.argv[0]).name:  # ignore folder, hidden file, etc.
        errors += 1
        continue
    filestem = fileNameRegex.search(filename[0])
    if not filestem:
        print(f'• "{f}" does not meet filename criteria')
        errors += 1
    else:
        hhmm = '1200'
        ss = '00'
        YYYY, s1, MM, s2, DD, s3, TIME = filestem.groups()
        if len(TIME) == 6:
            hhmm = TIME[:4]
            ss = TIME[4:]
        elif len(TIME) == 4:
            hhmm = TIME
        elif len(TIME) > 0:
            hhmm = str((int(TIME) // 60 + 12) % 24).rjust(4, '0')
            ss = str(int(TIME) % 60).rjust(2, '0')
        os.system(f'touch -c -mt {YYYY}{MM}{DD}{hhmm}.{ss} "{f}"')
        shutil.move(dir / f, dir / 'processed' / f)
        processed += 1

print('Done!')
print(f'{processed} files had Date Created modified and were moved to /processed.')
print(f'{errors} files/folders were ignored.')
if errors > 0:
    print('Filenames must contain YYYYMMDD_HHMMSS style date/time.')

