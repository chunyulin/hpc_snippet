import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as ticker

BASE="profile_tnqvm"
#BASE="tnqvm_n1"

co = ['b','r','g','m','y']
layers = [4,6,8,10,12]
#co = ['b','r','g','m']
#layers = [4,6,8,10]

co.reverse()
layers.reverse()

#= Plot parameter ==========================
#plt.rc('font', family='serif', serif='cm10')
#plt.rc('text', usetex=False)
#plt.rcParams['text.latex.preamble'] = [r'\boldmath']
plt.rc('xtick', labelsize=20)
plt.rc('ytick', labelsize=20)
plt.rc('legend', fontsize=20)
plt.rc('lines', lw=2)
plt.rc('axes', linewidth=2)
#plt.rcParams["font.weight"] = "bold"
#======================================

def getdata(l):
 fname = "{}_{}_layers.csv".format(BASE,l)
 ##fname = "stats_profile_tnqvm_{}_rounds.csv".format(l)
 return np.loadtxt(fname, delimiter=',')

def genstat(d):
 stat = []
 for nq in np.unique(d[:,1]):
  mask = (d[:,1]==nq)
  mem,ti = d[:,2][mask], d[:,3][mask]
  stat += [[nq, np.mean(mem), np.std(mem), np.mean(ti), np.std(ti)]]
 return np.array(stat)

r={}
s={}

for l in layers:
 r[l] = getdata(l)
 s[l] = genstat(r[l])
 
fig = plt.figure(figsize=(15,10))

plt.xlabel(r'Number of Qubits', fontsize=20)
plt.ylabel(r'Memory (MB)', fontsize=20)

#### Error bar
ax = fig.add_subplot(1, 1, 1)
ax.set_xscale("log", base=2, nonpositive='clip')
ax.set_yscale("log", nonpositive='clip')
ax.xaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: ('{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(y),0)))).format(y)))

for l,c in zip(layers,co):
 #print(l, len(np.unique(r[l]['n'])) ,len( r_avg[l]) , len(r_std[l]))
 ax.errorbar(s[l][:,0], s[l][:,1], yerr=s[l][:,2], capsize=5, color=c, label="{} layers".format(l))


plt.legend()
plt.savefig("{}_mem.png".format(BASE),bbox_inches='tight')


################
fig = plt.figure(figsize=(15,10))
plt.xlabel(r'Number of Qubits', fontsize=20)
plt.ylabel(r'Time (Secs)', fontsize=20)

# Error bar
ax = fig.add_subplot(1, 1, 1)
ax.set_xscale("log", base=2, nonpositive='clip')
ax.set_yscale("log", nonpositive='clip')
ax.xaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: ('{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(y),0)))).format(y)))

for l,c in zip(layers,co):
 ax.errorbar(s[l][:,0], s[l][:,3], yerr=s[l][:,4], capsize=5, color=c, label="{} layers".format(l))
plt.legend()
plt.savefig("{}_time.png".format(BASE),bbox_inches='tight')

