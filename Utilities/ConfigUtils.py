#!/usr/bin/env python
# Author:  Yun-Tse Tsai
# Date:    2015/2/4
#
import sys

def StringToBool( value ):
   value = str(value).lower() # make sure Value is a string, and convert it to lower case
   if value in [ 'true', 'yes' ]: return True
   if value in [ 'false', 'no' ]: return False
   raise ValueError( "Invalid boolean value: '%s'" % value )
# def StringToBool()

def getPlotConfig( cfgName ):
   print 'Reading in plot configuration file: %s' % cfgName
   config = {}
   f = open( cfgName, 'r' )

   for line in f:
      key, value = line.split(':')
      key = key.strip()
      value = value.strip()

      # Convert the configuration to the proper type
      if key in ['LogY']:
         try: value = StringToBool(value)
         except TypeError: print >> sys.stderr, 'LogY should be a bool!!'
      if key in ['Xmin', 'Xmax', 'Ymin', 'Ymax']:
         try: value = float(value)
         except TypeError: print >> sys.stderr, 'X/Ymin or X/Ymax should be a float!!'
      if key in ['NXBins', 'NYBins']:
         try: value = int(value)
         except TypeError: print >> sys.stderr, 'NXBins or NYBins should be an integer!!'
      if key in ['LegendXmin', 'LegendXmax', 'LegendYmin', 'LegendYmax']:
         try: value = float(value)
         except TypeError: print >> sys.stderr, 'LegendX/Ymin or LegendX/Ymax should be a float!!'
      if key in ['XTitleSize']:
         try: value = float(value)
         except TypeError: print >> sys.stderr, 'XTitleSize should be a float!'
      if key in ['YTitleOffSet']:
         try: value = float(value)
         except TypeError: print >> sys.stderr, 'YTitleOffSet should be a float!'

      # Fill the config dictionary
      config[key] = value

   f.close()
   return config
# getPlotConfig()

def getFileList( listName )
   print 'Reading in file list: %s' % listName
   f = open( listName, 'r' )
   flist = {}

   for line in f:
      fconfig = {}
      key, value = line.split(':')

# getFileList()
