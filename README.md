# rmass
In this repo I will present the procedure to compute reduced mass and force constant, which are used as the input in Holstein model Hamiltonian.

The idea is inspired from [this link](https://physics.stackexchange.com/questions/401370/normal-modes-how-to-get-reduced-masses-from-displacement-vectors-atomic-masses).

## The proceudres
1. Recompile the Phonon module of Quantum Espresso after inlcuding the updated write_eigenvectors.f90 and matdyn.f90 scripts

2. Performing the normal modes calculation and in particular obtain the data file of normalized displacement

3. python rmass.py, this is actually the main step

4. The frequencies, reduced mass, and force constant will be written in the output file.

Please note that we only evaluate the Gamma phonons because of the much large computational expenses. 
