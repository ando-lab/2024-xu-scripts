# ChimeraX script for fitting atomic models of alpha and beta subunits into the clusters.
# The starting locations of the alpha and beta subunit need to be close to the consensus map.

import os
os.chdir("/path/to/working/folder")

pixel_size = 2.034 # map pixel size

def threshold_by_perc(session, volumes, perc, step = None, subregion = None):
    from chimerax.map.measure import _subregion_description
    for v in volumes:
        reg = _subregion_description(v, step, subregion)
        if reg:
            reg = ', ' + reg
        m = v.matrix(step = step, subregion = subregion)
        from numpy import float64, sqrt
        mean = m.mean(dtype=float64)
        mmax = m.max()
        from chimerax.map_filter.vopcommand import volume_threshold
        volume_threshold(session, volumes, maximum = mean+(mmax-mean)*perc)

def register_command(session):
    from chimerax.core.commands import CmdDesc, register, FloatArg
    from chimerax.map.mapargs import MapsArg, MapRegionArg, MapStepArg
    desc = CmdDesc(required=[('volumes', MapsArg),
                             ('perc', FloatArg)],
                   keyword=[('step', MapStepArg),
                            ('subregion', MapRegionArg)],
                   synopsis='Thresholding map by percentage between max and mean')
    register('thresholdbyperc', desc, threshold_by_perc, logger=session.logger)

register_command(session)

from chimerax.core.commands import run

if not os.path.exists('output'):
    os.makedirs('output')

if not os.path.exists('output/fit_pdb'):
    os.makedirs('output/fit_pdb')

for idx in range(1000):
    run(session, 'open input_structure/preturnover_refined_S_fitted.pdb')
    run(session, 'open input_structure/4dr0_modified_fitted_removed_N.pdb')
    run(session, 'open ../kmeans1000/vol_'+str(idx).zfill(3)+'.mrc')
    run(session, 'fitmap #1 inMap #3')
    run(session, f'molmap #1 {pixel_size*2} onGrid #3')
    run(session, 'volume subtract #3 #4 minRms true')
    run(session, 'thresholdbyperc #5 0.25')
    run(session, 'fitmap #2 inMap #6')
    run(session, 'combine #1-2')
    run(session, 'save output/fit_pdb/vol_'+str(idx).zfill(3)+'_fit.pdb models #7 relModel #3')
    run(session, 'close all')
