#!../../anaconda2/bin/python
import pickle

import CRFfeature
from itertools import chain

userPostDic = pickle.load( open( "postLevelPerUserDic.p", "rb" ) )

print('number of user:',len(userPostDic.keys()))


