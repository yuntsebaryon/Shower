#!/usr/bin/env python
# Author:  Yun-Tse Tsai
# Date:    2015/2/4
#
import sys
import ROOT

def makeOverlayPlot( hlist, config, srcConfigs, outdir ):

   ROOT.gStyle.SetOptStat(0)
   c = ROOT.TCanvas( config['HistogramName'], config['HistogramName'], 800, 600 )
   c.SetBottomMargin(0.15)
   c.SetLeftMargin(0.15)
   c.SetRightMargin(0.05)
   c.SetFrameLineWidth(2)

   lxmin = 0.2
   lxmax = 0.5
   lymin = 0.6
   lymax = 0.8

   if 'LegendXmin' in config.keys():
      lxmin = config['LegendXmin']
   if 'LegendXmax' in config.keys():
      lxmax = config['LegendXmax']
   if 'LegendYmin' in config.keys():
      lymin = config['LegendYmin']
   if 'LegendYmax' in config.keys():
      lymax = config['LegendYmax']

   l = ROOT.TLegend( lxmin, lymin, lxmax, lymax )
   l.SetBorderSize(0)
   l.SetFillStyle(0)

   Ymax = 0.
   for src in hlist.keys():
      h = hlist[src]
      srcConfig = srcConfigs[src]
      # Set the source specific config
      h.SetLineWidth( 3 )
      if 'LineStyle' in srcConfig.keys():
         h.SetLineStyle( srcConfig['LineStyle'] )
      if 'Color' in srcConfig.keys():
         h.SetLineColor( srcConfig['Color'] )
      if 'Scale' in srcConfig.keys():
         h.Scale( srcConfig['Scale'] )
      if 'LegendName' in srcConfig.keys():
         l.AddEntry( h, srcConfig['LegendName'] )
      # Determine the Ymaximum
      if h.GetMaximum() > Ymax:
         Ymax = h.GetMaximum()

   # Set the variable specific config
   for src in hlist.keys():
      h = hlist[src]
      h.SetTitle( config['Title'] )
      if 'XTitleSize' in config.keys():
         h.GetXaxis().SetTitleSize( config['XTitleSize'] )
      else:
         h.GetXaxis().SetTitleSize(0.06)
      h.GetYaxis().SetTitleSize(0.07)
      h.GetXaxis().SetLabelSize(0.06)
      h.GetYaxis().SetLabelSize(0.06)
      h.GetXaxis().SetTitleOffset(1.1)
      if 'YTitleOffSet' in config.keys():
         h.GetYaxis().SetTitleOffset( config['YTitleOffSet'] )
      else:
         h.GetYaxis().SetTitleOffset(0.8)
      h.SetMaximum( 1.1* Ymax )

      if 'Xmin' in config.keys() and 'Xmax' in config.keys():
         h.GetXaxis().SetRangeUser( config['Xmin'], config['Xmax'] )
      if 'Ymin' in config.keys():
         h.GetYaxis().SetRangeUser( config['Ymin'], 1.1*Ymax )
      if 'LogY' in config.keys() and config['LogY']:
         c.SetLogy()

      if 'DrawOpt' not in config.keys():
         config['DrawOpt'] = "same"

      h.Draw( config['DrawOpt'] )

   if 'DrawOpt' not in config.keys() or config['DrawOpt'] == "same" or config['DrawOpt'] == "SAME":
      l.Draw()
      PlotName = "%s/%s" %( outdir, config['PlotName'] )
      c.SaveAs( PlotName )
      PlotName = PlotName.split('.')[0]
      PlotName = '%s.png' % PlotName
      c.SaveAs( PlotName )

# makeOverlayPlot()

def make2DPlot( hlist, config, srcConfigs, outdir ):

   ROOT.gStyle.SetOptStat(0)
   c = ROOT.TCanvas( config['HistogramName'], config['HistogramName'], 800, 600 )
   c.SetBottomMargin(0.15)
   c.SetLeftMargin(0.15)
   c.SetRightMargin(0.05)
   c.SetFrameLineWidth(2)

   for src in hlist.keys():
      h = hlist[src]
      h.SetTitle( config['Title'] )
      if 'XTitleSize' in config.keys():
         h.GetXaxis().SetTitleSize( config['XTitleSize'] )
      else:
         h.GetXaxis().SetTitleSize(0.06)
      h.GetYaxis().SetTitleSize(0.07)
      h.GetXaxis().SetLabelSize(0.06)
      h.GetYaxis().SetLabelSize(0.06)
      h.GetXaxis().SetTitleOffset(1.1)
      if 'YTitleOffSet' in config.keys():
         h.GetYaxis().SetTitleOffset( config['YTitleOffSet'] )
      else:
         h.GetYaxis().SetTitleOffset(0.8)

      if 'Xmin' in config.keys() and 'Xmax' in config.keys():
         h.GetXaxis().SetRangeUser( config['Xmin'], config['Xmax'] )
      if 'Ymin' in config.keys():
         h.GetYaxis().SetRangeUser( config['Ymin'], config['Ymax'] )

      h.Draw( config['DrawOpt'] )
      srcName = srcConfigs[src]['LegendName'].replace(' ','')
      PlotName = "%s/%s_%s" %( outdir, srcName, config['PlotName'] )
      c.SaveAs( PlotName )
      PlotName = PlotName.split('.')[0]
      PlotName = '%s.png' % PlotName
      c.SaveAs( PlotName )

# make2DPlot()
