#!/usr/bin/env python
# Author:  Yun-Tse Tsai
# Date:    2015/2/4
# Update:  2016/2/19
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
      if line.strip()[:1] == '#':
         continue
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

def getFileList( listName ):
   print 'Reading in file list: %s' % listName
   f = open( listName, 'r' )
   fList = {}

   for line in f:
      if line.strip()[:1] == '#':
         continue
      try:
         key, value = line.split(':')
         key = key.strip()
         value = value.strip()
      except:
         continue

      params = key.split('.')
      i = int(params[1])
      param = params[2]
      d = {}
      if i in fList.keys():
         d = fList[i]
      d[param] = value
      fList[i] = d

   nSources = len( fList )
   # print 'nSources: %d' % nSources
   # print fList

   for i in fList:
      d = fList[i]
      if not 'File' in d.keys():
         raise KeyError( 'No file name specified in source %d!' % i )
      if 'FillStyle' in d.keys():
         try: d['FillStyle'] = int(d['FillStyle'])
         except TypeError: pass
      if 'Color' in d.keys():
         try: d['Color'] = int(d['Color'])
         except TypeError: pass
      if 'FillColor' in d.keys():
         try: d['FillColor'] = int(d['FillColor'])
         except TypeError: pass
      if 'Scale' in d.keys():
         try: d['Scale'] = float(d['Scale'])
         except TypeError: print >> sys.stderr, 'Scale of source %d must be a float!' % i
      if 'LineStyle' in d.keys():
         try: d['LineStyle'] = int(d['LineStyle'])
         except TypeError: print >> sys.stderr, 'LineStyle of source %d must be an integer!' % i

   return nSources, fList
# getFileList()

def getSelection( selName ):
   print 'Reading in the selection criteria from %s' % selName
   f = open( selName, 'r' )
   selection = {}

   for line in f:
      if line.strip()[:1] == '#':
         continue
      try:
         key, value = line.split(':')
         key = key.strip()
         value = value.strip()
      except:
         continue  

      if ( key.find('NRecoShowers') > 0 ) or ( key.find('NMCShowers') > 0 ):
         try: value = int(value)
         except TypeError: print sys.stderr >> 'Cannot parse the selection criterion %s: %s!' %( key, value )
      else:
         try: value = float(value)
         except TypeError: print sys.stderr >> 'Cannot parse the selection criterion %s: %s!' %( key, value )
      selection[key] = value

   return selection
# getSelection()

def getHistoNames( histoList ):
   print 'Reading the list of histograms from %s' % histoList
   f = open( histoList, 'r' )
   histos = {}

   for line in f:
      if line.strip()[:1] == '#':
         continue
      try:
         key, value = line.split(':')
         key = key.strip()
         value = value.strip()
      except:
         continue

      if key == 'Tree':
         tree = value
      elif key == 'SelectionType':
         selectionType = value
      else:
         histos[key] = value

   return tree, selectionType, histos
# getHistoNames()

if __name__ == "__main__":

   listName = sys.argv[1]
   print listName
   nSources, fList = getFileList( listName )
# if __name__ == "__main__"
