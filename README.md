# rmass
In this repo I will present the procedure to compute reduced mass and force constant, which are used as the input in Holstein model Hamiltonian.

The idea is inspired from [this link](https://physics.stackexchange.com/questions/401370/normal-modes-how-to-get-reduced-masses-from-displacement-vectors-atomic-masses).

## The proceudres
1. Recompile the Phonon module of Quantum Espresso after inlcuding the updated write_eigenvectors.f90 and matdyn.f90 scripts

2. Performing the normal modes calculation and in particular obtain the data file of normalized displacement, i.e., ch4.disp. I did it by `mpirun matdyn.x <phdos.in> phdos.out`, this command will use the write_eigenvectors module. Please do compute just the Gamma phonon, below is an example phdos.in file:

```
 &input
    asr='simple'
    flfrc='ch4.fc'
    flfrq='ch4.freq'
    flvec='ch4.disp'
    fleig='ch4.vec'
    fldyn='ch4-matdyn.dyn'
    dos=.true.,
    nk1=1,nk2=1,nk3=1
    fldos='ch4.dos'
    DeltaE = 0.1
    ndos = 50
 /
```

3. python rmass.py, this is actually the main step

4. The frequencies, reduced mass, and force constant will be written in the output file.

Please note that we only evaluate the Gamma phonon because of the much large computational expenses. 
