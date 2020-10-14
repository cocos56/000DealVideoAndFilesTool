from Name.api import Recover
from Storer.api import Timestamp, commit

Recover.delFsStr(Timestamp(20, 10, 13, 22, 27, 41))
commit()
