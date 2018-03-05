#!/usr/bin/env python
""" Time Profile: IRI2016 """
import pyiri2016
from numpy import arange
from datetime import timedelta
from matplotlib.pyplot import figure, show
try:
    import ephem
except ImportError:
    ephem = None
# %% user parameters
hrlim = [0, 24] # [0,24] does whole day(s)
hrstp = 0.25 # time step [decimal hours]
#lat = -11.95; lon = -76.77
glat = 0
glon = 0
alt_km = arange(120, 180, 10)
# %% ru
sim = pyiri2016.timeprofile(('2012-08-21','2012-08-22'),timedelta(hours=0.25),
                            alt_km,glat,glon)

# %% Plots
Nplot=2


if Nplot>2:
    fig = figure(figsize=(16,12))
    axs = fig.subplots(2,2, sharex=True).ravel()
else:
    fig = figure(figsize=(16,6))
    axs = fig.subplots(1,2).ravel()

pn = axs[0]
#NmF1 = pyiri2016.IRI2016()._RmNeg(sim.b[2, :])
#NmE = sim.loc[4, :]
pn.plot(sim.time, sim.attrs['NmF2'], label='N$_m$F$_2$')
#pn.plot(sim.time, NmF1, label='N$_m$F$_1$')
#pn.plot(sim.time, NmE, label='N$_m$E')
pn.set_title(sim.title1)
pn.set_xlabel('Hour (UT)')
pn.set_ylabel('(m$^{-3}$)')
pn.set_yscale('log')
pn.legend(loc='best')

pn = axs[1]
hmF2 = sim.b[1, :]
hmF1 = pyiri2016.IRI2016()._RmNeg(sim.b[3, :])
hmE = sim.b[5, :]
pn.plot(sim.time, hmF2, label='h$_m$F$_2$')
pn.plot(sim.time, hmF1, label='h$_m$F$_1$')
pn.plot(sim.time, hmE, label='h$_m$E')
pn.set_title(sim.title2)
pn.set_xlabel('Hour (UT)')
pn.set_ylabel('(km)')
pn.legend(loc='best')

if Nplot > 2:
    pn = axs[2]

    for alt in alt_km:
        sim = pyiri2016.timeprofile(('2012-08-21','2012-08-22'),timedelta(hours=0.25),
                                    alt,glat,glon)

        pn.plot(sim.time, sim.loc[:,'ne'], marker='.', label=alt)
    pn.set_xlabel('time UTC (hours)')
    pn.set_ylabel('[m$^{-3}$]')
    pn.set_title(f'$N_e$ vs. altitude and time')
    pn.legend(loc='best')

if Nplot > 4:
    pn = axs[4]
    tec = sim.b[36, :]
    pn.plot(sim.time, tec, label=r'TEC')
    pn.set_xlabel('Hour (UT)')
    pn.set_ylabel('(m$^{-2}$)')
    #pn.set_yscale('log')
    pn.legend(loc='best')

    pn = axs[5]
    vy = sim.b[43, :]
    pn.plot(sim.time, vy, label=r'V$_y$')
    pn.set_xlabel('Hour (UT)')
    pn.set_ylabel('(m/s)')
    pn.legend(loc='best')

for a in axs.ravel():
    a.grid(True)


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='IRI2016 time profile plot')
    p.add_argument('-t','--trange',help='START STOP STEP (hours) time [UTC]',nargs=3,
                   default=('2012-08-21','2012-08-22',0.25))
    p.add_argument('--alt',help='START STOP STEP altitude [km]',type=float, nargs=3,default=(120,180,20))
    p.add_argument('-c','--latlon',help='geodetic coordinates of simulation',
                   type=float,default=(65,-147.5))
    p.add_argument('--f107',type=float,default=200.)
    p.add_argument('--f107a', type=float,default=200.)
    p.add_argument('--ap', type=int, default=4)
    p.add_argument('--species',help='species to plot',nargs='+',default=('ne'))
    p = p.parse_args()


show()
