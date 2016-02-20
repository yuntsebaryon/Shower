#!/usr/bin/env python
# Author:  Yun-Tse Tsai
# Date:    2015/2/6
#

import ROOT
import sys

def getTree( fName, tName ):

   t = ROOT.TChain( tName )
   t.AddFile( fName )

   t.SetDirectory(0)
   return t
# getTree()

def getHistogram( fName, hName ):
   f = ROOT.TFile( fName, "READ" )
   if not f:
      print >> sys.stderr, "Cannot open %s" % fName
      sys.exit( 1 )

   h = f.Get( hName )
   if not h:
      print >> sys.stderr, "Cannot get histogram %s in file %s" % ( hName, fName )
      sys.exit( 1 )

   h.SetDirectory(0)
   return h
# getHistograms()
