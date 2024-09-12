# ChimeraX script to generate molmap and masks for alpha, beta, and TrxA. 6mt9_TrxA.pdb contains alpha subunit (chain A) and AF2 prediciton of TrxA (chain B) in complex.
import os
os.chdir("/path/to/working/folder")

from chimerax.core.commands import run

idx_to_use = 0
pixel_size = 2.034 # map pixel size

if not os.path.exists('output/other_map_and_masks'):
    os.makedirs('output/other_map_and_masks')

run(session, f'open ../kmeans1000/vol_{str(idx_to_use).zfill(3)}.mrc')
run(session, f'open output/fit_pdb/vol_{str(idx_to_use).zfill(3)}_fit.pdb')
run(session, 'molmap #2/A,C 20 onGrid #1')
run(session, 'volume threshold #3 minimum 0.1 set 0')
run(session, 'volume threshold #4 maximum 0.09 setMaximum 1')
run(session, f'save output/other_map_and_masks/vol_{str(idx_to_use).zfill(3)}_fit_alpha_mask.mrc models #5')
run(session, f'molmap #2/A,B,C,D {pixel_size*2} onGrid #1')
run(session, f'save output/other_map_and_masks/vol_{str(idx_to_use).zfill(3)}_fit_molmap_alpha_{str(pixel_size*2).replace(".","")}.mrc models #6')
run(session, f'molmap #2/E,F {pixel_size*2} onGrid #1')
run(session, f'save output/other_map_and_masks/vol_{str(idx_to_use).zfill(3)}_fit_molmap_beta_{str(pixel_size*2).replace(".","")}.mrc models #7')
run(session, 'open input_structure/6mt9_TrxA.pdb')
run(session, 'match #8/A to #2/A')
run(session, 'molmap #8/B 20 onGrid #1')
run(session, 'volume threshold #9 minimum 0.1 set 0')
run(session, 'volume threshold #10 maximum 0.09 setMaximum 1')
run(session, f'save output/other_map_and_masks/vol_{str(idx_to_use).zfill(3)}_fit_TrxA_chain_A_mask.mrc models #11')
run(session, 'open input_structure/6mt9_TrxA.pdb')
run(session, 'match #12/A to #2/C')
run(session, 'molmap #12/B 20 onGrid #1')
run(session, 'volume threshold #13 minimum 0.1 set 0')
run(session, 'volume threshold #14 maximum 0.09 setMaximum 1')
run(session, f'save output/other_map_and_masks/vol_{str(idx_to_use).zfill(3)}_fit_TrxA_chain_C_mask.mrc models #15')
run(session, f'molmap #12/B {pixel_size*2} onGrid #1')
run(session, f'save output/other_map_and_masks/vol_{str(idx_to_use).zfill(3)}_fit_TrxA_molmap_{str(pixel_size*2).replace(".","")}.mrc models #13')
run(session, 'close all')
