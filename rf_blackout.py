#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Rf Blackout
# Generated: Fri Mar 29 02:56:55 2019
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx


class rf_blackout(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Rf Blackout")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.target_freq = target_freq = 91.1E6
        self.samp_rate = samp_rate = 5e6
        self.rf_gain = rf_gain = 10
        self.bandwidth_size = bandwidth_size = 10e6
        self.sample_rate = sample_rate = samp_rate
        self.gain = gain = rf_gain
        self.cent_freq = cent_freq = target_freq
        self.bandwidth = bandwidth = bandwidth_size

        ##################################################
        # Blocks
        ##################################################
        _sample_rate_sizer = wx.BoxSizer(wx.VERTICAL)
        self._sample_rate_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_sample_rate_sizer,
        	value=self.sample_rate,
        	callback=self.set_sample_rate,
        	label='Sample rate',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._sample_rate_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_sample_rate_sizer,
        	value=self.sample_rate,
        	callback=self.set_sample_rate,
        	minimum=2e6,
        	maximum=20e6,
        	num_steps=10,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_sample_rate_sizer)
        _gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_gain_sizer,
        	value=self.gain,
        	callback=self.set_gain,
        	label='RF gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_gain_sizer,
        	value=self.gain,
        	callback=self.set_gain,
        	minimum=10,
        	maximum=60,
        	num_steps=10,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_gain_sizer)
        _cent_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._cent_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_cent_freq_sizer,
        	value=self.cent_freq,
        	callback=self.set_cent_freq,
        	label='Target Frequency',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._cent_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_cent_freq_sizer,
        	value=self.cent_freq,
        	callback=self.set_cent_freq,
        	minimum=70e6,
        	maximum=6000e6,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_cent_freq_sizer)
        _bandwidth_sizer = wx.BoxSizer(wx.VERTICAL)
        self._bandwidth_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_bandwidth_sizer,
        	value=self.bandwidth,
        	callback=self.set_bandwidth,
        	label='Bandwidth Size',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._bandwidth_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_bandwidth_sizer,
        	value=self.bandwidth,
        	callback=self.set_bandwidth,
        	minimum=2e6,
        	maximum=50e6,
        	num_steps=10,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_bandwidth_sizer)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_subdev_spec('A:A', 0)
        self.uhd_usrp_sink_0.set_samp_rate(sample_rate)
        self.uhd_usrp_sink_0.set_center_freq(cent_freq, 0)
        self.uhd_usrp_sink_0.set_gain(gain, 0)
        self.uhd_usrp_sink_0.set_bandwidth(bandwidth, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 50, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.uhd_usrp_sink_0, 0))

    def get_target_freq(self):
        return self.target_freq

    def set_target_freq(self, target_freq):
        self.target_freq = target_freq
        self.set_cent_freq(self.target_freq)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_sample_rate(self.samp_rate)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self.set_gain(self.rf_gain)

    def get_bandwidth_size(self):
        return self.bandwidth_size

    def set_bandwidth_size(self, bandwidth_size):
        self.bandwidth_size = bandwidth_size
        self.set_bandwidth(self.bandwidth_size)

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self._sample_rate_slider.set_value(self.sample_rate)
        self._sample_rate_text_box.set_value(self.sample_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.sample_rate)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self._gain_slider.set_value(self.gain)
        self._gain_text_box.set_value(self.gain)
        self.uhd_usrp_sink_0.set_gain(self.gain, 0)


    def get_cent_freq(self):
        return self.cent_freq

    def set_cent_freq(self, cent_freq):
        self.cent_freq = cent_freq
        self._cent_freq_slider.set_value(self.cent_freq)
        self._cent_freq_text_box.set_value(self.cent_freq)
        self.uhd_usrp_sink_0.set_center_freq(self.cent_freq, 0)

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        self._bandwidth_slider.set_value(self.bandwidth)
        self._bandwidth_text_box.set_value(self.bandwidth)
        self.uhd_usrp_sink_0.set_bandwidth(self.bandwidth, 0)


def main(top_block_cls=rf_blackout, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
