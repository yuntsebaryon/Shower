#!/usr/bin/env python
# Author:  Yun-Tse Tsai
# Date:    2016/3/31
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
Version = "%prog version 1.0"

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
      # Fill the histograms
      if 'nHitsU' in hList.keys():
         hList['nHitsU'].Fill( i.nhits[0] )
      if 'nHitsV' in hList.keys():
         hList['nHitsV'].Fill( i.nhits[1] )
      if 'nHitsY' in hList.keys():
         hList['nHitsY'].Fill( i.nhits[2] )
      if 'ChargesU' in hList.keys():
         hList['ChargesU'].Fill( i.charges[0] )
      if 'ChargesV' in hList.keys():
         hList['ChargesV'].Fill( i.charges[1] )
      if 'ChargesY' in hList.keys():
         hList['ChargesY'].Fill( i.charges[2] )

   return hList

# def selection()


if __name__ == "__main__":

   # Decode the input augument
   options, args = decodeCommandLine()
   print "Input filelist    : %s" % options.inList
   print "Histogram list    : %s" % options.histoList
   print "Output directory  : %s" % options.outDir
   if options.selectionList:
      print "Selection criteria: %s" % options.selectionList
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
      Selection = ConfigUtils.getSelection( options.selectionList )

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
