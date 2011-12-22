#!/usr/bin/env python
# -*- coding: utf-8 -*-
# distrubuted under the GPL GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
# written by n3uromanc3r 2011

import wx
import os

class Frame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.button = wx.Button(self, -1, "Select eBook file to convert...")
        self.text_ctrl = wx.TextCtrl(self, -1, "")
        self.label = wx.StaticText(self, -1, "What do you want to convert to?")
        self.choice = wx.Choice(self, -1, choices=["epub", "fb2", "lit", "lrf", "mobi", "oeb", "pdb", "pdf", "pml", "rb", "rtf", "tcr", "txt"])
        self.button_2 = wx.Button(self, -1, "Convert!")

        self.__set_properties()
        self.__do_layout()
        
        self.Bind(wx.EVT_BUTTON, self.onClicked, self.button)
        self.Bind(wx.EVT_BUTTON, self.onClicked2, self.button_2)

    def __set_properties(self):
        self.SetTitle("eBook Converter")
        self.SetSize((500, 170))
        self.text_ctrl.SetMinSize((250, 27))
        self.choice.SetSelection(0)
        self.button_2.SetMinSize((100, 40))

    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.button, 0, wx.LEFT|wx.TOP|wx.ADJUST_MINSIZE, 15)
        sizer_3.Add(self.text_ctrl, 0, wx.LEFT|wx.TOP|wx.ADJUST_MINSIZE, 15)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_4.Add(self.label, 0, wx.LEFT|wx.RIGHT|wx.TOP|wx.ADJUST_MINSIZE, 15)
        sizer_4.Add(self.choice, 0, wx.LEFT|wx.TOP|wx.ADJUST_MINSIZE, 9)
        sizer_2.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_2.Add(self.button_2, 0, wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 15)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.SetSize((500, 170))
        
    def onClicked(self, event):
		self.dirname = ''
		dlg = wx.FileDialog(self, "Choose an eBook file to convert", self.dirname,"", "*.*", wx.OPEN)
		if dlg.ShowModal()==wx.ID_OK:
			self.filename=dlg.GetFilename()
			self.dirname=dlg.GetDirectory()		
			dlg.Destroy()
			ebookworkingdir = self.dirname
			ebookfile = self.filename
			global ebookfilename
			ebookfilename = os.path.splitext(ebookfile)[0]
			global fullebookpathandfilename
			fullebookpathandfilename = "%s/%s" % (ebookworkingdir, ebookfile)
			global destinationebookpathandfilename
			destinationebookpathandfilename = "%s/%s" % (ebookworkingdir, ebookfilename)
			self.text_ctrl.SetValue(ebookfilename)
		
    def onClicked2(self, event):
        global selectedfiletype
        selectedfiletype = self.choice.GetStringSelection()
        cmd="ebook-convert '%(var1)s' '%(var2)s'.'%(var3)s'"
        cmd = cmd % { 'var1' : fullebookpathandfilename, 'var2' : destinationebookpathandfilename, 'var3' : selectedfiletype } 
        os.system(cmd)
        os.system('notify-send Conversion complete!')
    
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = Frame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
