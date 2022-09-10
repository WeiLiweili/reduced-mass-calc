'''
rmass: calculate reduced mass using eigenmode
Wei Li
email: liwei0099@gmail.com

use it to compute the reduced mass and force constant of k-th normal mode
please email me if there are any questions or errors
'''

import numpy as np 

filename = "ch4.disp"
fileout = "data.txt"

f=open(filename, "r")
fr=f.readlines()
f.close()

fline = [] #containing the index of the line with the frequency
freqs = [] #in cm-1
amass=[] #in amu
eigenmode = [] # eigenmode, dimensionless, dividd by M^1/2 before diagonalization and then normalized, it is actually the d/|sqrt(d^2)|, 
               # note that eigenvector of the dynamical matrix multipled M^1/2

for i in range(len(fr)):
    line = fr[i].strip().split()
    #print (line)
    if  "freq" in line:
        fline.append(i)
        freqs.append(float(line[4]))

#print (fline)

for i in range(len(fline)):

    if fline[i] == fline[-1]:
        lines = fr[fline[-1]+1:]

    else:
        lines = fr[fline[i]+1:fline[i+1]]

        #print (lines)
    mass=[]; em=[]

    for line in lines:
        tmp=[float(x) for x in line.strip().split()]
        mass.append(tmp[0]);  mass.append(tmp[3]);   mass.append(tmp[6])
        em.append(tmp[1]);    em.append(tmp[4]);     em.append(tmp[7]) 
        # we extract the real part since only the Gamma phonons calculated

    amass.append(mass); eigenmode.append(u)

#print (amass)
#print (eigenmode)

freqs = np.array(freqs)
amass = np.array(amass)
eigenmode = np.array(eigenmode)

rmass = np.zeros(len(freqs))
# 1/u_k = sum(E_i,k^2/m_i)
#https://physics.stackexchange.com/questions/401370/normal-modes-how-to-get-reduced-masses-from-displacement-vectors-atomic-masses
rmass = 1 / (np.sum(eigenmode**2/amass, axis=1)) # in amu

'''
http://openmopac.net/manual/Hessian_Matrix.html
omega = 2*pi*c*sqrt(k/u) 
k, in millidyne / A 
u, reduced mass in amu 
omega = 1302.79 *sqrt(k/u) in cm^-1
=> k = (omega/1302.79)^2 * u
k= (freqs/1302.79)**2 * rmass
'''

header = '{0:^10s}        {1:^10s}     {2:^10s} '.format('freq (cm^-1)', 'reduced mass (amu)', 'force constant (millidyne/A)')
np.savetxt(fileout, np.column_stack([freqs, rmass, k]), fmt=['%10.3f','%16.3f','%20.3f'], header=header)

