#!/usr/bin/env python
# Author:  Yun-Tse Tsai
# Date:    2016/4/27
#

import ROOT

def showerSelection( tree, criteria, hList ):

   n = 0
   for i in tree:
      # Selection
      if ( 'AngleDiffMax' in criteria.keys() ) and ( i.mc_reco_anglediff > criteria['AngleDiffMax'] ):
         continue
      if ( 'StartingPointAccMax' in criteria.keys() ) and ( i.mc_reco_dist > criteria['StartingPointAccMax'] ):
         continue
      if ( 'dQdxUMin' in criteria.keys() ) and ( i.reco_dqdx_U < criteria['dQdxUMin'] ):
         continue
      if ( 'dQdxUMax' in criteria.keys() ) and ( i.reco_dqdx_U > criteria['dQdxUMax'] ):
         continue
      if ( 'dQdxVMin' in criteria.keys() ) and ( i.reco_dqdx_V < criteria['dQdxVMin'] ):
         continue
      if ( 'dQdxVMax' in criteria.keys() ) and ( i.reco_dqdx_V > criteria['dQdxVMax'] ):
         continue
      if ( 'dQdxYMin' in criteria.keys() ) and ( i.reco_dqdx_Y < criteria['dQdxYMin'] ):
         continue
      if ( 'dQdxYMax' in criteria.keys() ) and ( i.reco_dqdx_Y > criteria['dQdxYMax'] ):
         continue
      if ( 'ClusterEffQualU' in criteria.keys() ) and ( i.cluster_eff_U <= 0. ):
         continue
      if ( 'ClusterEffQualV' in criteria.keys() ) and ( i.cluster_eff_V <= 0. ):
         continue
      if ( 'ClusterEffQualY' in criteria.keys() ) and ( i.cluster_eff_Y <= 0. ):
         continue
      if ( 'NRecoShowers' in criteria.keys() ) and ( i.n_recoshowers != criteria['NRecoShowers'] ):
         continue

      if ( 'RecoCosThetaMax' in criteria.keys() ) and ( i.RecoCosTheta > criteria['RecoCosThetaMax'] ):
         continue
      if ( 'RecoE1Min' in criteria.keys() ) and ( i.RecoE1 < criteria['RecoE1Min'] ):
         continue
      if ( 'RecoE2Min' in criteria.keys() ) and ( i.RecoE2 < criteria['RecoE2Min'] ):
         continue
      if ( 'RecoCosThetaMax' in criteria.keys() ) and ( i.RecoCosTheta > criteria['RecoCosThetaMax'] ):
         continue
      if ( 'RecoCosThetaMin' in criteria.keys() ) and ( i.RecoCosTheta < criteria['RecoCosThetaMin'] ):
         continue
      if ( 'DCA1Max' in criteria.keys() ) and ( i.mc_reco_dca1 > criteria['DCA1Max'] ):
         continue
      if ( 'DCA2Max' in criteria.keys() ) and ( i.mc_reco_dca2 > criteria['DCA2Max'] ):
         continue
      if ( 'MCContainment1Min' in criteria.keys() ) and ( i.mc_containment1 < criteria['MCContainment1Min'] ):
         continue
      if ( 'MCContainment2Min' in criteria.keys() ) and ( i.mc_containment2 < criteria['MCContainment2Min'] ):
         continue

      n += 1
      # Calculate the variables of interest
      # Event tree
      if 'NRecoShowers' in hList.keys():
         hList['NRecoShowers'].Fill( i.n_recoshowers )
      if 'NMCShowers' in hList.keys():
         hList['NMCShowers'].Fill( i.n_mcshowers )
      if 'PerfectRecoE1' in hList.keys():
         hList['PerfectRecoE1'].Fill( i.PerfectRecoE1 )
      if 'PerfectRecoE2' in hList.keys():
         hList['PerfectRecoE2'].Fill( i.PerfectRecoE2 )
      if 'PerfectRecoCosTheta' in hList.keys():
         hList['PerfectRecoCosTheta'].Fill( i.PerfectRecoCosTheta )
      if 'PerfectRecoPi0Mass' in hList.keys():
         hList['PerfectRecoPi0Mass'].Fill( i.PerfectRecoPi0Mass )
      if 'RecoE1' in hList.keys():
         hList['RecoE1'].Fill( i.RecoE1 )
      if 'RecoE2' in hList.keys():
         hList['RecoE2'].Fill( i.RecoE2 )
      if 'RecoCosTheta' in hList.keys():
         hList['RecoCosTheta'].Fill( i.RecoCosTheta )
      if 'RecoPi0Mass' in hList.keys():
         hList['RecoPi0Mass'].Fill( i.RecoPi0Mass )
      if 'PerfectRecoERecoThetaPi0Mass' in hList.keys():
         hList['PerfectRecoERecoThetaPi0Mass'].Fill( i.PerfectRecoERecoThetaPi0Mass )
      if 'RecoEPerfectRecoThetaPi0Mass' in hList.keys():
         hList['RecoEPerfectRecoThetaPi0Mass'].Fill( i.RecoEPerfectRecoThetaPi0Mass )
      if 'DCA' in hList.keys():
         hList['DCA'].Fill( i.mc_reco_dca1, i.mc_reco_dca2 )

      # Shower tree
      if 'EnergyResU' in hList.keys():
         hList['EnergyResU'].Fill( ( i.mc_energy - i.reco_energy_U )/i.mc_energy )
      if 'EnergyResV' in hList.keys():
         hList['EnergyResV'].Fill( ( i.mc_energy - i.reco_energy_V )/i.mc_energy )
      if 'EnergyResY' in hList.keys():
         hList['EnergyResY'].Fill( ( i.mc_energy - i.reco_energy_Y )/i.mc_energy )
      if 'EnergyAsymU' in hList.keys():
         hList['EnergyAsymU'].Fill( ( i.mc_energy - i.reco_energy_U )/ ( i.mc_energy + i.reco_energy_U ) )
      if 'EnergyAsymV' in hList.keys():
         hList['EnergyAsymV'].Fill( ( i.mc_energy - i.reco_energy_V )/ ( i.mc_energy + i.reco_energy_V ) )
      if 'EnergyAsymY' in hList.keys():
         hList['EnergyAsymY'].Fill( ( i.mc_energy - i.reco_energy_Y )/ ( i.mc_energy + i.reco_energy_Y ) )
      if 'EnergyDiffU' in hList.keys():
         hList['EnergyDiffU'].Fill( ( i.mc_energy - i.reco_energy_U ) )
      if 'EnergyDiffV' in hList.keys():
         hList['EnergyDiffV'].Fill( ( i.mc_energy - i.reco_energy_V ) )
      if 'EnergyDiffY' in hList.keys():
         hList['EnergyDiffY'].Fill( ( i.mc_energy - i.reco_energy_Y ) )
      if 'StartingPointAcc' in hList.keys():
         hList['StartingPointAcc'].Fill( i.mc_reco_dist )
      if 'AngleDiff' in hList.keys():
         hList['AngleDiff'].Fill( i.mc_reco_anglediff )
      if 'dEdxU' in hList.keys():
         hList['dEdxU'].Fill( i.reco_dedx_U )
      if 'dEdxV' in hList.keys():
         hList['dEdxV'].Fill( i.reco_dedx_V )
      if 'dEdxY' in hList.keys():
         hList['dEdxY'].Fill( i.reco_dedx_Y )
      if 'dEdx' in hList.keys():
         hList['dEdx'].Fill( i.reco_dedx )
      if 'dQdxU' in hList.keys():
         hList['dQdxU'].Fill( i.reco_dqdx_U )
      if 'dQdxV' in hList.keys():
         hList['dQdxV'].Fill( i.reco_dqdx_V )
      if 'dQdxY' in hList.keys():
         hList['dQdxY'].Fill( i.reco_dqdx_Y )
      if 'dQdx' in hList.keys():
         hList['dQdx'].Fill( i.reco_dqdx )
      if 'ClusterEffU' in hList.keys():
         hList['ClusterEffU'].Fill( i.cluster_eff_U )
      if 'ClusterEffV' in hList.keys():
         hList['ClusterEffV'].Fill( i.cluster_eff_V )
      if 'ClusterEffY' in hList.keys():
         hList['ClusterEffY'].Fill( i.cluster_eff_Y )
      if 'Length' in hList.keys():
         hList['Length'].Fill( i.reco_length )
      if 'LongWidth' in hList.keys():
         hList['LongWidth'].Fill( i.reco_width1 )
      if 'ShortWidth' in hList.keys():
         hList['ShortWidth'].Fill( i.reco_width2 )
      if 'EnergyCorrU' in hList.keys():
         hList['EnergyCorrU'].Fill( i.mc_energy, i.reco_energy_U )
      if 'EnergyCorrV' in hList.keys():
         hList['EnergyCorrV'].Fill( i.mc_energy, i.reco_energy_V )
      if 'EnergyCorrY' in hList.keys():
         hList['EnergyCorrY'].Fill( i.mc_energy, i.reco_energy_Y )

   print 'Number of reconstructed pi0: %d' % n
   return hList, n

# def selection() 

def pi0Selection( tree, criteria, hList ):

   n = 0
   for i in tree:
      # Selection
      if ( 'NRecoShowers' in criteria.keys() ) and ( i.n_recoshowers != criteria['NRecoShowers'] ):
         continue
      if ( 'RecoCosThetaMax' in criteria.keys() ) and ( i.RecoCosTheta >= criteria['RecoCosThetaMax'] ):
         continue
      if ( 'RecoEMin' in criteria.keys() ) and ( ( i.reco_energy[0] <= criteria['RecoEMin'] ) or ( i.reco_energy[1] <= criteria['RecoEMin'] ) ):
         continue

      n += 1
      # Calculate the variables of interest
      # Fill the tree
      if 'NRecoShowers' in hList.keys():
         hList['NRecoShowers'].Fill( i.n_recoshowers )
      if 'NMCShowers' in hList.keys():
         hList['NMCShowers'].Fill( i.n_mcshowers )
      if 'MCPi0Mass' in hList.keys():
         hList['MCPi0Mass'].Fill( i.MCPi0Mass )
      if 'DepERecoThetaPi0Mass' in hList.keys():
         hList['DepERecoThetaPi0Mass'].Fill( i.DepERecoThetaPi0Mass )
      if 'RecoEMCThetaPi0Mass' in hList.keys():
         hList['RecoEMCThetaPi0Mass'].Fill( i.RecoEMCThetaPi0Mass )
      if 'PerfectRecoPi0Mass' in hList.keys():
         hList['PerfectRecoPi0Mass'].Fill( i.PerfectRecoPi0Mass )
      if 'MCCosTheta' in hList.keys():
         hList['MCCosTheta'].Fill( i.MCCosTheta )
      if 'MCTheta' in hList.keys():
         hList['MCTheta'].Fill( i.MCTheta )
      if 'RecoCosTheta' in hList.keys():
         hList['RecoCosTheta'].Fill( i.RecoCosTheta )
      if 'RecoPi0Mass' in hList.keys():
         hList['RecoPi0Mass'].Fill( i.RecoPi0Mass )
      if 'RecoDCA' in hList.keys():
         hList['RecoDCA'].Fill( i.reco_dca[0], i.reco_dca[1] )
      if 'DCA' in hList.keys():
         hList['DCA'].Fill( i.mcv_reco_dca[0], i.mcv_reco_dca[1] )
      if 'MCDCA' in hList.keys():
         hList['MCDCA'].Fill( i.recov_mc_dca[0], i.recov_mc_dca[1] )
      if 'RecoE1' in hList.keys():
         hList['RecoE1'].Fill( i.reco_energy[0] )
      if 'RecoE2' in hList.keys():
         hList['RecoE2'].Fill( i.reco_energy[1] )
      if 'Energy1ResU' in hList.keys():
         hList['Energy1ResU'].Fill( ( i.mc_energy[0] - i.reco_energy_U[0] )/i.mc_energy[0] )
      if 'Energy1ResV' in hList.keys():
         hList['Energy1ResV'].Fill( ( i.mc_energy[0] - i.reco_energy_V[0] )/i.mc_energy[0] )
      if 'Energy1ResY' in hList.keys():
         hList['Energy1ResY'].Fill( ( i.mc_energy[0] - i.reco_energy_Y[0] )/i.mc_energy[0] )
      if 'Energy2ResU' in hList.keys():
         hList['Energy2ResU'].Fill( ( i.mc_energy[1] - i.reco_energy_U[1] )/i.mc_energy[1] )
      if 'Energy2ResV' in hList.keys():
         hList['Energy2ResV'].Fill( ( i.mc_energy[1] - i.reco_energy_V[1] )/i.mc_energy[1] )
      if 'Energy2ResY' in hList.keys():
         hList['Energy2ResY'].Fill( ( i.mc_energy[1] - i.reco_energy_Y[1] )/i.mc_energy[1] )
      if 'Energy1AsymU' in hList.keys():
         hList['Energy1AsymU'].Fill( ( i.mc_energy[0] - i.reco_energy_U[0] )/ ( i.mc_energy[0] + i.reco_energy_U[0] ) )
      if 'Energy1AsymV' in hList.keys():
         hList['Energy1AsymV'].Fill( ( i.mc_energy[0] - i.reco_energy_V[0] )/ ( i.mc_energy[0] + i.reco_energy_V[0] ) )
      if 'Energy1AsymY' in hList.keys():
         hList['Energy1AsymY'].Fill( ( i.mc_energy[0] - i.reco_energy_Y[0] )/ ( i.mc_energy[0] + i.reco_energy_Y[0] ) )
      if 'Energy2AsymU' in hList.keys():
         hList['Energy2AsymU'].Fill( ( i.mc_energy[1] - i.reco_energy_U[1] )/ ( i.mc_energy[1] + i.reco_energy_U[1] ) )
      if 'Energy2AsymV' in hList.keys():
         hList['Energy2AsymV'].Fill( ( i.mc_energy[1] - i.reco_energy_V[1] )/ ( i.mc_energy[1] + i.reco_energy_V[1] ) )
      if 'Energy2AsymY' in hList.keys():
         hList['Energy2AsymY'].Fill( ( i.mc_energy[1] - i.reco_energy_Y[1] )/ ( i.mc_energy[1] + i.reco_energy_Y[1] ) )
      if 'Energy1DiffU' in hList.keys():
         hList['Energy1DiffU'].Fill( ( i.mc_energy[0] - i.reco_energy_U[0] ) )
      if 'Energy1DiffV' in hList.keys():
         hList['Energy1DiffV'].Fill( ( i.mc_energy[0] - i.reco_energy_V[0] ) )
      if 'Energy1DiffY' in hList.keys():
         hList['Energy1DiffY'].Fill( ( i.mc_energy[0] - i.reco_energy_Y[0] ) )
      if 'Energy2DiffU' in hList.keys():
         hList['Energy2DiffU'].Fill( ( i.mc_energy[1] - i.reco_energy_U[1] ) )
      if 'Energy2DiffV' in hList.keys():
         hList['Energy2DiffV'].Fill( ( i.mc_energy[1] - i.reco_energy_V[1] ) )
      if 'Energy2DiffY' in hList.keys():
         hList['Energy2DiffY'].Fill( ( i.mc_energy[1] - i.reco_energy_Y[1] ) )
      if 'StartingPoint1Acc' in hList.keys():
         hList['StartingPoint1Acc'].Fill( i.mc_reco_dist[0] )
      if 'StartingPoint2Acc' in hList.keys():
         hList['StartingPoint2Acc'].Fill( i.mc_reco_dist[1] )
      if 'Angle1Diff' in hList.keys():
         hList['Angle1Diff'].Fill( i.mc_reco_anglediff[0] )
      if 'Angle2Diff' in hList.keys():
         hList['Angle2Diff'].Fill( i.mc_reco_anglediff[1] )
      if 'dEdx1U' in hList.keys():
         hList['dEdx1U'].Fill( i.reco_dedx_U[0] )
      if 'dEdx1V' in hList.keys():
         hList['dEdx1V'].Fill( i.reco_dedx_V[0] )
      if 'dEdx1Y' in hList.keys():
         hList['dEdx1Y'].Fill( i.reco_dedx_Y[0] )
      if 'dEdx1' in hList.keys():
         hList['dEdx1'].Fill( i.reco_dedx[0] )
      if 'dEdx2U' in hList.keys():
         hList['dEdx2U'].Fill( i.reco_dedx_U[1] )
      if 'dEdx2V' in hList.keys():
         hList['dEdx2V'].Fill( i.reco_dedx_V[1] )
      if 'dEdx2Y' in hList.keys():
         hList['dEdx2Y'].Fill( i.reco_dedx_Y[1] )
      if 'dEdx2' in hList.keys():
         hList['dEdx2'].Fill( i.reco_dedx[1] )
      if 'dQdx1U' in hList.keys():
         hList['dQdx1U'].Fill( i.reco_dqdx_U[0] )
      if 'dQdx1V' in hList.keys():
         hList['dQdx1V'].Fill( i.reco_dqdx_V[0] )
      if 'dQdx1Y' in hList.keys():
         hList['dQdx1Y'].Fill( i.reco_dqdx_Y[0] )
      if 'dQdx1' in hList.keys():
         hList['dQdx1'].Fill( i.reco_dqdx[0] )
      if 'dQdx2U' in hList.keys():
         hList['dQdx2U'].Fill( i.reco_dqdx_U[1] )
      if 'dQdx2V' in hList.keys():
         hList['dQdx2V'].Fill( i.reco_dqdx_V[1] )
      if 'dQdx2Y' in hList.keys():
         hList['dQdx2Y'].Fill( i.reco_dqdx_Y[1] )
      if 'dQdx2' in hList.keys():
         hList['dQdx2'].Fill( i.reco_dqdx[1] )
      if 'ClusterEff1' in hList.keys():
         hList['ClusterEff1'].Fill( i.cluster_eff[0] )
      if 'ClusterEff2' in hList.keys():
         hList['ClusterEff2'].Fill( i.cluster_eff[1] )

   print 'Number of reconstructed pi0: %d' % n
   return hList, n
# pi0Selection()

def ECalSelection( tree, criteria, hList ):

   n = [ 0, 0, 0 ]
   r = [ 0., 0., 0. ]
   p = [ 0., 0., 0. ]
   for i in tree:
      # Selection
      if ( i.reco_energy_U == 0. ):
         pass
      elif ( 'RecoEMin' in criteria.keys() ) and ( i.reco_energy_U < criteria['RecoEMin'] ):
         pass
      elif ( 'RatioMin' in criteria.keys() ) and ( i.reco_energy_U/i.mc_energy < criteria['RatioMin'] ):
         pass
      else:
         n[0] += 1
         ratio = i.reco_energy_U / i.mc_energy
         r[0] += ratio
         hList['EnergyRatioU'].Fill( ratio )

      if ( i.reco_energy_V == 0. ):
         pass
      elif ( 'RecoEMin' in criteria.keys() ) and ( i.reco_energy_V < criteria['RecoEMin'] ):
         pass
      elif ( 'RatioMin' in criteria.keys() ) and ( i.reco_energy_V/i.mc_energy < criteria['RatioMin'] ):
         pass
      else:
         n[1] += 1
         ratio = i.reco_energy_V / i.mc_energy
         r[1] += ratio
         hList['EnergyRatioV'].Fill( ratio )

      if ( i.reco_energy_Y == 0. ):
         pass
      elif ( 'RecoEMin' in criteria.keys() ) and ( i.reco_energy_Y < criteria['RecoEMin'] ):
         pass
      elif ( 'RatioMin' in criteria.keys() ) and ( i.reco_energy_Y/i.mc_energy < criteria['RatioMin'] ):
         pass
      else:
         n[2] += 1
         ratio = i.reco_energy_Y / i.mc_energy
         r[2] += ratio
         hList['EnergyRatioY'].Fill( ratio )

   for i in xrange( 0, len(r) ):
      # print 'Plane %d: Sum(ratio): %f, Sum(n): %d' % ( i, r[i], n[i] )
      r[i] = r[i]/float(n[i])
   ibin = hList['EnergyRatioU'].GetMaximumBin()
   p[0] = hList['EnergyRatioU'].GetXaxis().GetBinCenter( ibin )
   ibin = hList['EnergyRatioV'].GetMaximumBin()
   p[1] = hList['EnergyRatioV'].GetXaxis().GetBinCenter( ibin )
   ibin = hList['EnergyRatioY'].GetMaximumBin()
   p[2] = hList['EnergyRatioY'].GetXaxis().GetBinCenter( ibin )


   return hList, n, r, p
# ECalSelection()


def dataPi0Selection( tree, criteria, hList ):

   n = 0
   for i in tree:
      # Selection
      if ( 'NRecoShowers' in criteria.keys() ) and ( i.n_recoshowers != criteria['NRecoShowers'] ):
         continue
      if ( 'RecoCosThetaMax' in criteria.keys() ) and ( i.RecoCosTheta >= criteria['RecoCosThetaMax'] ):
         continue
      if ( 'RecoEMin' in criteria.keys() ) and ( ( i.reco_energy[0] <= criteria['RecoEMin'] ) or ( i.reco_energy[1] <= criteria['RecoEMin'] ) ):
         continue

      n += 1
      # Calculate the variables of interest
      if 'RecoPi0Mass' in hList.keys():
         hList['RecoPi0Mass'].Fill( i.RecoPi0Mass[0] )
   print 'Number of reconstructed pi0: %d' % n
   return hList, n
# dataPi0Selection()
