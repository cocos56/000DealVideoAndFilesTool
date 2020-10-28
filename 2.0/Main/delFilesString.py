from Name.api import delFsStrWithRe, delFilesNameStr,\
    delFilesStr, delDsStr, stripFileName
from Storer.api import commit
from datetime import datetime

now = datetime.now()

exe = False
exe = True

pat = r'(.+)\(.+\)'
# pat = r'(\d+)'
pat = r'\d+.(.+)\(.+'
# delFsStrWithRe(pat, exe)

string = r'会员版(2.0)-就业课-'

# delFilesStr(string, r'', exe)

# delFilesNameStr(string, r'', exe)

# stripFileName('', exe)

while True:
    if delDsStr(string, r'', exe) == 'FileNotFoundError':
        pass
    else:
        break

print('总历时：', datetime.now() - now)
commit()
