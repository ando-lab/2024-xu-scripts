# ChimeraX script to batch generate mask for the beta subunit

import os
os.chdir("/path/to/working/folder")

from chimerax.core.commands import run

import glob
pdb_list = glob.glob('output/fit_pdb/*.pdb')

if not os.path.exists('output/beta_mask'):
    os.makedirs('output/beta_mask')

for pdb in pdb_list:
    run(session, 'open ../kmeans1000/vol_000.mrc')
    run(session, 'open '+pdb)
    run(session, 'molmap #2/E,F 20 onGrid #1')
    run(session, 'volume threshold #3 minimum 0.1 set 0')
    run(session, 'volume threshold #4 maximum 0.09 setMaximum 1')
    run(session, 'save output/beta_mask/'+pdb.split('/')[-1].split('.')[0]+'_beta_mask.mrc models #5')
    run(session, 'close all')
