### Quick start on H100
```
$ . ./gocom
$ sbatch h100.sub
```

### Note
- The pure cpu code DGX[01-12] (JID 6650, 6653) is faster than HGX[13-24] (JID 6651, 6652), with and without core-binding.
- From the cpu info, DGX has vmx enabled. Can it be the root cause that slow cpu code?


