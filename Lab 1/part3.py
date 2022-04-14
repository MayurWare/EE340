#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Part 3
# GNU Radio version: v3.8.2.0-57-gd71cd177

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget

from gnuradio import qtgui

class part3(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Part 3")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Part 3")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "part3")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.SampleRate = SampleRate = 48000
        self.Adjust_4 = Adjust_4 = 0.5
        self.Adjust_3 = Adjust_3 = 0.5
        self.Adjust_2 = Adjust_2 = 0.5
        self.Adjust_1 = Adjust_1 = 0.5
        self.Adjust_0 = Adjust_0 = 0.5

        ##################################################
        # Blocks
        ##################################################
        self._Adjust_4_range = Range(0, 1, 0.1, 0.5, 200)
        self._Adjust_4_win = RangeWidget(self._Adjust_4_range, self.set_Adjust_4, 'Adjust_4', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Adjust_4_win)
        self._Adjust_3_range = Range(0, 1, 0.1, 0.5, 200)
        self._Adjust_3_win = RangeWidget(self._Adjust_3_range, self.set_Adjust_3, 'Adjust_3', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Adjust_3_win)
        self._Adjust_2_range = Range(0, 1, 0.1, 0.5, 200)
        self._Adjust_2_win = RangeWidget(self._Adjust_2_range, self.set_Adjust_2, 'Adjust_2', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Adjust_2_win)
        self._Adjust_1_range = Range(0, 1, 0.1, 0.5, 200)
        self._Adjust_1_win = RangeWidget(self._Adjust_1_range, self.set_Adjust_1, 'Adjust_1', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Adjust_1_win)
        self._Adjust_0_range = Range(0, 1, 0.1, 0.5, 200)
        self._Adjust_0_win = RangeWidget(self._Adjust_0_range, self.set_Adjust_0, 'Adjust_0', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Adjust_0_win)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('E:\\Lab 1\\Audio Files\\Bach.wav', True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, SampleRate,True)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_4 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                Adjust_2,
                SampleRate,
                3000,
                6000,
                1,
                firdes.WIN_HAMMING,
                6.76))
        self.band_pass_filter_3 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                Adjust_1,
                SampleRate,
                500,
                3000,
                1,
                firdes.WIN_HAMMING,
                6.76))
        self.band_pass_filter_2 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                Adjust_0,
                SampleRate,
                20,
                500,
                1,
                firdes.WIN_HAMMING,
                6.76))
        self.band_pass_filter_1 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                Adjust_4,
                SampleRate,
                9000,
                15000,
                1,
                firdes.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                Adjust_3,
                SampleRate,
                6000,
                9000,
                1,
                firdes.WIN_HAMMING,
                6.76))
        self.audio_sink_0 = audio.sink(SampleRate, '', True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.band_pass_filter_1, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.band_pass_filter_2, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.band_pass_filter_3, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.band_pass_filter_4, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_1, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_2, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_3, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_4, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "part3")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_SampleRate(self):
        return self.SampleRate

    def set_SampleRate(self, SampleRate):
        self.SampleRate = SampleRate
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.Adjust_3, self.SampleRate, 6000, 9000, 1, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_1.set_taps(firdes.band_pass(self.Adjust_4, self.SampleRate, 9000, 15000, 1, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_2.set_taps(firdes.band_pass(self.Adjust_0, self.SampleRate, 20, 500, 1, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_3.set_taps(firdes.band_pass(self.Adjust_1, self.SampleRate, 500, 3000, 1, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_4.set_taps(firdes.band_pass(self.Adjust_2, self.SampleRate, 3000, 6000, 1, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.SampleRate)

    def get_Adjust_4(self):
        return self.Adjust_4

    def set_Adjust_4(self, Adjust_4):
        self.Adjust_4 = Adjust_4
        self.band_pass_filter_1.set_taps(firdes.band_pass(self.Adjust_4, self.SampleRate, 9000, 15000, 1, firdes.WIN_HAMMING, 6.76))

    def get_Adjust_3(self):
        return self.Adjust_3

    def set_Adjust_3(self, Adjust_3):
        self.Adjust_3 = Adjust_3
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.Adjust_3, self.SampleRate, 6000, 9000, 1, firdes.WIN_HAMMING, 6.76))

    def get_Adjust_2(self):
        return self.Adjust_2

    def set_Adjust_2(self, Adjust_2):
        self.Adjust_2 = Adjust_2
        self.band_pass_filter_4.set_taps(firdes.band_pass(self.Adjust_2, self.SampleRate, 3000, 6000, 1, firdes.WIN_HAMMING, 6.76))

    def get_Adjust_1(self):
        return self.Adjust_1

    def set_Adjust_1(self, Adjust_1):
        self.Adjust_1 = Adjust_1
        self.band_pass_filter_3.set_taps(firdes.band_pass(self.Adjust_1, self.SampleRate, 500, 3000, 1, firdes.WIN_HAMMING, 6.76))

    def get_Adjust_0(self):
        return self.Adjust_0

    def set_Adjust_0(self, Adjust_0):
        self.Adjust_0 = Adjust_0
        self.band_pass_filter_2.set_taps(firdes.band_pass(self.Adjust_0, self.SampleRate, 20, 500, 1, firdes.WIN_HAMMING, 6.76))





def main(top_block_cls=part3, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
