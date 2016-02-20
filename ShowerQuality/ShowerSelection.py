#!/usr/bin/env python
# Author:  Yun-Tse Tsai
# Date:    2015/2/2
# Update:  2016/2/19
#
import sys
import os
import ROOT
import math
from optparse import OptionParser
import AccessROOTUtils
import PlotUtils
import ConfigUtils

Usage = """%prog  [options]

Does something.
"""
Version = "%prog version 2.0"

def decodeCommandLine():
   parser = OptionParser( usage = Usage, version = Version )

   parser.add_option( "-i", "--inlist", dest = "inList",
      help = "list of the input files [mandatory]" )
   parser.add_option( "-c", "--histolist", dest = "histoList",
      help = "list of the histograms [mandatory]" )
   parser.add_option( "-o", "--outdir", dest = "outDir",
      help = "path of the output plots and files [mandatory]" )
   parser.add_option( "-s", "--selection", dest = "selectionList",
      help = "list of the selection criteria" )

   ( options, args ) = parser.parse_args()

   for mand_option in [ 'inList', 'histoList', 'outDir', ]:
      if options.__dict__[mand_option] is None:
         print >> sys.stderr, "Mandantory option for %s is missing!\n" % mand_option
         parser.print_help()
         sys.exit( 1 )
   # for all mandatory options

   return options, args
# decodeCommandLine()

def createDir():
   if not os.path.exists( options.outDir ):
      os.mkdir( options.outDir )
      print "   Creating the output directory %s " % options.outDir
   else:
      print "   The output directory already exists"

# createDir()

def writeSelection( outdir, criteria ):

   fname = "%s/SELECTION" % outdir
   ftxt  = open( fname, 'w' )

   for criterion in criteria.keys():
      ftxt.write("%s:    %s\n" % ( criterion, criteria[criterion] ) )

# writeSelection()

def bookHistograms( srcName, hconfigs ):

   hList = {}

   for histo in hconfigs.keys():
      hName = "%s_%s" % ( srcName, histo )
      hconfig = hconfigs[histo]
      if 'DrawOpt' in hconfig.keys() and ( hconfig['DrawOpt'] == 'COLZ' or hconfig['DrawOpt'] == 'colz' ):
         hList[histo] = ROOT.TH2D( hName, "%s; %s; %s" % ( hconfig["Title"], hconfig["XTitle"], hconfig["YTitle"] ), hconfig["NXBins"], hconfig["Xmin"], hconfig["Xmax"], hconfig['NYBins'], hconfig["Ymin"], hconfig["Ymax"] )
      else:
         hList[histo] = ROOT.TH1D( hName, "%s; %s; %s" % ( hconfig["Title"], hconfig["XTitle"], hconfig["YTitle"] ), hconfig["NXBins"], hconfig["Xmin"], hconfig["Xmax"] )

   return hList

# def bookHistograms()

def selection( tree, criteria, hList ):

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

      # Calculate the variables of interest
      if 'hNRecoShowers' in hList.keys():
         hList['hNRecoShowers'].Fill( i.n_recoshowers )
      if 'hNMCShowers' in hList.keys():
         hList['hNMCShowers'].Fill( i.n_mcshowers )
      if 'hEnergyResU' in hList.keys():
         hList['hEnergyResU'].Fill( ( i.mc_energy - i.reco_energy_U )/i.mc_energy )
      if 'hEnergyResV' in hList.keys():
         hList['hEnergyResV'].Fill( ( i.mc_energy - i.reco_energy_V )/i.mc_energy )
      if 'hEnergyResY' in hList.keys():
         hList['hEnergyResY'].Fill( ( i.mc_energy - i.reco_energy_Y )/i.mc_energy )
      if 'hEnergyAsymU' in hList.keys():
         hList['hEnergyAsymU'].Fill( ( i.mc_energy - i.reco_energy_U )/ ( i.mc_energy + i.reco_energy_U ) )
      if 'hEnergyAsymV' in hList.keys():
         hList['hEnergyAsymV'].Fill( ( i.mc_energy - i.reco_energy_V )/ ( i.mc_energy + i.reco_energy_V ) )
      if 'hEnergyAsymY' in hList.keys():
         hList['hEnergyAsymY'].Fill( ( i.mc_energy - i.reco_energy_Y )/ ( i.mc_energy + i.reco_energy_Y ) )
      if 'hEnergyDiffU' in hList.keys():
         hList['hEnergyDiffU'].Fill( ( i.mc_energy - i.reco_energy_U ) )
      if 'hEnergyDiffV' in hList.keys():
         hList['hEnergyDiffV'].Fill( ( i.mc_energy - i.reco_energy_V ) )
      if 'hEnergyDiffY' in hList.keys():
         hList['hEnergyDiffY'].Fill( ( i.mc_energy - i.reco_energy_Y ) )
      if 'hStartingPointAcc' in hList.keys():
         hList['hStartingPointAcc'].Fill( i.mc_reco_dist )
      if 'hAngleDiff' in hList.keys():
         hList['hAngleDiff'].Fill( i.mc_reco_anglediff )
      if 'hdEdxU' in hList.keys():
         hList['hdEdxU'].Fill( i.reco_dedx_U )
      if 'hdEdxV' in hList.keys():
         hList['hdEdxV'].Fill( i.reco_dedx_V )
      if 'hdEdxY' in hList.keys():
         hList['hdEdxY'].Fill( i.reco_dedx_Y )
      if 'hdEdx' in hList.keys():
         hList['hdEdx'].Fill( i.reco_dedx )
      if 'hdQdxU' in hList.keys():
         hList['hdQdxU'].Fill( i.reco_dqdx_U )
      if 'hdQdxV' in hList.keys():
         hList['hdQdxV'].Fill( i.reco_dqdx_V )
      if 'hdQdxY' in hList.keys():
         hList['hdQdxY'].Fill( i.reco_dqdx_Y )
      if 'hdQdx' in hList.keys():
         hList['hdQdx'].Fill( i.reco_dqdx )
      if 'hClusterEffU' in hList.keys():
         hList['hClusterEffU'].Fill( i.cluster_eff_U )
      if 'hClusterEffV' in hList.keys():
         hList['hClusterEffV'].Fill( i.cluster_eff_V )
      if 'hClusterEffY' in hList.keys():
         hList['hClusterEffY'].Fill( i.cluster_eff_Y )
      if 'hLength' in hList.keys():
         hList['hLength'].Fill( i.reco_length )
      if 'hEnergyCorrU' in hList.keys():
         hList['hEnergyCorrU'].Fill( i.mc_energy, i.reco_energy_U )
      if 'hEnergyCorrV' in hList.keys():
         hList['hEnergyCorrV'].Fill( i.mc_energy, i.reco_energy_V )
      if 'hEnergyCorrY' in hList.keys():
         hList['hEnergyCorrY'].Fill( i.mc_energy, i.reco_energy_Y )

   return hList

# def selection()


if __name__ == "__main__":

   # Decode the input augument
   options, args = decodeCommandLine()
   print "Input filelist    : %s" % options.inList
   print "Histogram list    : %s" % options.histoList
   print "Output directory  : %s" % options.outDir
   if options.selectionList:
      print "Selection criteria: %s" % options.selctionList
   else:
      print "No selection criterion is applied."

   # Read in the input filelist
   sList = {}
   nSources, sList = ConfigUtils.getFileList( options.inList )

   # Read in the histogram list
   Histos = {}
   tree, Histos = ConfigUtils.getHistoNames( options.histoList )

   # Create the output directory
   createDir()
   # Copy the input file list to the output directory
   os.system('cp %s %s' % ( options.inList, options.outDir ) )

   # Read in the selection criteria
   Selection = {}
   if options.selectionList:
      Selection = ConfigUtils.getSelection( options.selctionList )

   # Create a text file in the output directory to record the selection criteria
   writeSelection( options.outDir, Selection )

   hConfig = {}
   hDict = {}

   for histo in Histos.keys():
      hConfig[histo] = ConfigUtils.getPlotConfig( Histos[histo] )

   for src in sList.keys():
      fname = sList[src]['File']
      print 'Open %s...' % fname
      t = AccessROOTUtils.getTree( fname, tree )
      srcName = sList[src]['LegendName'].replace( ' ', '')
      hDict[src] = bookHistograms( srcName, hConfig )
      hDict[src] = selection( t, Selection, hDict[src] )

   for histo in Histos.keys():
      hList = {}

      for src in sList.keys():
         hList[src] = hDict[src][histo]

      hCfg = hConfig[histo]
      if 'DrawOpt' in hCfg.keys() and ( hCfg['DrawOpt'] == 'COLZ' or hCfg['DrawOpt'] == 'colz' ):
         PlotUtils.make2DPlot( hList, hConfig[histo], sList, options.outDir )
      else:
         PlotUtils.makeOverlayPlot( hList, hConfig[histo], sList, options.outDir )

# if __name__ == "__main__"
