import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import collections

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

print "Number of unique open credit lines is: " +str(len(freq))

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

chi, p = stats.chisquare(freq.values())
print "Chi test value = " + str(chi)
print "P stat = " + str(p) 