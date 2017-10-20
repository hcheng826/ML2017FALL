import pandas as pd
import numpy as np
from util import *

x_test = pd.read_csv('data/proc_x_test')
x_test = np.concatenate((x_test, np.ones((x_test.shape[0],1))), axis=1)
w = pd.read_csv('para/logistic_para')

f = sigmoid(np.dot(x_test, w))
ans = np.array(determine_ans(f))
ans = np.concatenate((np.arange(1,len(ans)+1).reshape(ans.shape), ans),axis=1)
pd.DataFrame(ans).to_csv('ans/logsitic_ans',index=False,header=['id','label'])