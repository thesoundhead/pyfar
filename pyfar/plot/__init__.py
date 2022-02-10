# -*- coding: utf-8 -*-

"""
The following documents the pyfar plot functions. Refer to the
:py:mod:`concepts <pyfar._concepts.plots>` for more background information.
"""

from .line import (
    freq,
    time,
    phase,
    group_delay,
    time_freq,
    freq_phase,
    freq_group_delay,
    custom_subplots
)

from .two_d import (
    time2d,
    freq2d,
    phase2d,
    group_delay2d,
    time_freq2d,
    freq_phase2d,
    freq_group_delay2d,
    spectrogram
)

from .spatial import (
    scatter,
    quiver
)

from .utils import (
    plotstyle,
    context,
    use,
    color,
    shortcuts
)

__all__ = [
    'freq',
    'freq2d',
    'time',
    'time2d',
    'phase',
    'phase2d',
    'group_delay',
    'group_delay2d',
    'spectrogram',
    'time_freq',
    'time_freq2d',
    'freq_phase',
    'freq_phase2d',
    'freq_group_delay',
    'freq_group_delay2d',
    'custom_subplots',
    'scatter',
    'quiver',
    'plotstyle',
    'context',
    'use',
    'color',
    'shortcuts'
]
