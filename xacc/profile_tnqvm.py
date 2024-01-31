import random
import numpy as np
#import _pyxacc as xacc
import xacc
import argparse
import sys
import time



def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',type=int,required=True)
    parser.add_argument('-l',type=int,required=True)
    parser.add_argument('-i', default="tnqvm")
    parser.add_argument('-d',type=int, default=-1)
    opts = parser.parse_args(args)
    return opts

from io import StringIO
def write_qasm(nQ, rounds):
    file = StringIO()
    file.write("__qpu__ void f(AcceleratorBuffer b) {\n")
    local_gates = ('X', 'Y', 'Z', 'RX', 'RY', 'RZ', 'H')
    
    if nQ%2==0: # even
        evens = tuple((i, i+1) for i in range(nQ) if i%2==0)
        odds = tuple((i, i+1) for i in range(nQ-1) if i%2==1)
    
    if nQ%2==1: # odd
        evens = tuple((i, i+1) for i in range(nQ-2) if i%2==0)
        odds = tuple((i, i+1) for i in range(nQ) if i%2==1)
        
    for i in range(nQ): 
        file.write('H ' + str(i) + '\n')  # initial Hadamards

    # random gates
    for i in range(rounds):
        for j in range(nQ): 
            gate = random.choice(local_gates)
            if 'R' in gate:
                angle = str(np.random.uniform(0,np.pi));
                file.write('{} '.format(str(gate) + '('+str(angle)+')') + str(j) + '\n')
            else:
                file.write('{} '.format(str(gate)) + str(j) + ' \n')
                       
        for e in evens:
            file.write('CNOT {0} {1}\n'.format(*e))
            
        for e in odds:
            file.write('CNOT {0} {1}\n'.format(*e))
            
    file.write("}")
    return file.getvalue()
    ## w/o file.close()
    
@profile
def execute(nq, rounds, backend, dim):
    src = write_qasm(nq, rounds)
    #qpu = xacc.getAccelerator('tnqvm')
    #qpu = xacc.getAccelerator('tnqvm:exatn-mps:float')
    if (dim<0):
     qpu = xacc.getAccelerator(backend)
    else:
     qpu = xacc.getAccelerator(backend,{'max-bond-dim':dim})
    #xacc.setOption('tnqvm-verbose',0)
    ir = xacc.getCompiler('quil').compile(src)
    f = ir.getComposite('f')
    buf = xacc.qalloc(nq)
    qpu.execute(buf, f)

if __name__ == '__main__':

    #random.seed(7777)
    opts = parse_args(sys.argv[1:])
    xacc.Initialize()
    t0 = time.time()
    execute(opts.n,opts.l, opts.i, opts.d)
    print("Time_in_sec: %s" % (time.time() - t0))