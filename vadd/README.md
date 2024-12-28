### Quick start on H100
```
$ . ./gocom
$ sbatch h100.sub
```

### Note
- The pure cpu code DGX[01-12] (JID 6650, 6653) is slower than HGX[13-24] (JID 6651, 6652), with and without core-binding.
- The lscpu shows that DGX has more cpu flags enabled: `vmx tpr_shadow vnmi flexpriority ept vpid ept_admx`


