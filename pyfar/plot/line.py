"""Line plots for time and frequency domain signals."""
from pyfar.plot.utils import context
from . import _line
from . import _interaction as ia


def time(signal, dB=False, log_prefix=20, log_reference=1, unit="s",
         ax=None, style='light', mode='real', **kwargs):
    """Plot the time signal.

    Plots ``signal.time`` and passes keyword arguments (`kwargs`) to
    :py:func:`matplotlib.pyplot.plot`.

    Parameters
    ----------
    signal : Signal, TimeData
        The input data to be plotted. Multidimensional data are flattened for
        plotting, e.g, a signal of ``signal.cshape = (2, 2)`` would be plotted
        in the order ``(0, 0)``, ``(0, 1)``, ``(1, 0)``, ``(1, 1)``.
    dB : bool
        Indicate if the data should be plotted in dB in which case
        ``log_prefix * np.log10(signal.time / log_reference)`` is used. The
        default is ``False``.
    log_prefix : integer, float
        Prefix for calculating the logarithmic time data. The default is
        ``20``.
    log_reference : integer
        Reference for calculating the logarithmic time data. The default is
        ``1``.
    unit : str, None
        Set the unit of the time axis.

        ``'s'`` (default)
            seconds
        ``'ms'``
            milliseconds
        ``'mus'``
            microseconds
        ``'samples'``
            samples
        ``'auto'``
            Use seconds, milliseconds, or microseconds depending on the length
            of the data.
    ax : matplotlib.axes.Axes
        Axes to plot on. The default is ``None``, which uses the current axis
        or creates a new figure if none exists.
    style : str
        ``light`` or ``dark`` to use the pyfar plot styles or a plot style from
        :py:data:`matplotlib.style.available`. Pass a dictionary to set
        specific plot parameters, for example
        ``style = {'axes.facecolor':'black'}``. Pass an empty dictionary
        ``style = {}`` to use the currently active plotstyle. The default is
        ``light``.
    mode : str, optional
        ``real``, ``imag``, or ``abs`` to specify if the real part, imaginary
        part or absolute value of the time data is plotted. ``'imag'`` and
        ``'abs'``` can only be used for complex Signals.
        The default is ``real``.
    **kwargs
        Keyword arguments that are passed to :py:func:`matplotlib.pyplot.plot`.

    Returns
    -------
    ax : matplotlib.axes.Axes
        Axes or array of axes containing the plot.

    Examples
    --------
    .. plot::

        >>> import pyfar as pf
        >>> sine = pf.signals.sine(100, 4410)
        >>> pf.plot.time(sine, unit='ms')

    """

    with context(style):
        ax = _line._time(signal.flatten(), dB, log_prefix, log_reference, unit,
                         ax, mode, **kwargs)

    # manage interaction
    plot_parameter = ia.PlotParameter(
        'time', dB_time=dB, log_prefix_time=log_prefix,
        log_reference=log_reference, unit_time=unit, mode=mode)
    interaction = ia.Interaction(
        signal, ax, None, style, plot_parameter, **kwargs)
    ax.interaction = interaction

    return ax


def freq(signal, dB=True, log_prefix=None, log_reference=1, freq_scale='log',
         ax=None, style='light', side='right', **kwargs):
    """
    Plot the magnitude spectrum.

    Plots ``abs(signal.freq)`` and passes keyword arguments (`kwargs`) to
    :py:func:`matplotlib.pyplot.plot`.

    Parameters
    ----------
    signal : Signal, FrequencyData
        The input data to be plotted. Multidimensional data are flattened for
        plotting, e.g, a signal of ``signal.cshape = (2, 2)`` would be plotted
        in the order ``(0, 0)``, ``(0, 1)``, ``(1, 0)``, ``(1, 1)``.
    dB : bool
        Indicate if the data should be plotted in dB in which case
        ``log_prefix * np.log10(abs(signal.freq) / log_reference)`` is used.
        The default is ``True``.
    log_prefix : integer, float
        Prefix for calculating the logarithmic frequency data. The default is
        ``None``, so ``10`` is chosen if ``signal.fft_norm`` is ``'power'`` or
        ``'psd'`` and ``20`` otherwise.
    log_reference : integer, float
        Reference for calculating the logarithmic frequency data. The default
        is ``1``.
    freq_scale : str
        ``linear`` or ``log`` to plot on a linear or logarithmic frequency
        axis. The default is ``log``.
    ax : matplotlib.axes.Axes
        Axes to plot on. The default is ``None``, which uses the current axis
        or creates a new figure if none exists.
    style : str
        ``light`` or ``dark`` to use the pyfar plot styles or a plot style from
        :py:data:`matplotlib.style.available`. Pass a dictionary to set
        specific plot parameters, for example
        ``style = {'axes.facecolor':'black'}``. Pass an empty dictionary
        ``style = {}`` to use the currently active plotstyle. The default is
        ``light``.
    side : str, optional
        ``'right'`` to plot the right-sided spectrum containing the positive
        frequencies, or ``'left'`` to plot the left-sided spectrum containing
        the negative frequencies (only possible for complex Signals). The
        default is ``'right'``.
    **kwargs
        Keyword arguments that are passed to :py:func:`matplotlib.pyplot.plot`.

    Returns
    -------
    ax : matplotlib.axes.Axes
        Axes or array of axes containing the plot.

    Example
    -------

    .. plot::

        >>> import pyfar as pf
        >>> sine = pf.signals.sine(100, 4410)
        >>> pf.plot.freq(sine)
    """

    with context(style):
        ax = _line._freq(signal.flatten(), dB, log_prefix, log_reference,
                         freq_scale, ax, side, **kwargs)

    # manage interaction
    plot_parameter = ia.PlotParameter(
        'freq', dB_freq=dB, log_prefix_freq=log_prefix,
        log_reference=log_reference, xscale=freq_scale, side=side)
    interaction = ia.Interaction(
        signal, ax, None, style, plot_parameter, **kwargs)
    ax.interaction = interaction

    return ax


def phase(signal, deg=False, unwrap=False, freq_scale='log', ax=None,
          style='light', side='right', **kwargs):
    """Plot the phase of the spectrum.

    Plots ``angle(signal.freq)`` and passes keyword arguments (`kwargs`) to
    :py:func:`matplotlib.pyplot.plot`.

    Parameters
    ----------
    signal : Signal, FrequencyData
        The input data to be plotted. Multidimensional data are flattened for
        plotting, e.g, a signal of ``signal.cshape = (2, 2)`` would be plotted
        in the order ``(0, 0)``, ``(0, 1)``, ``(1, 0)``, ``(1, 1)``.
    deg : bool
        Plot the phase in degrees. The default is ``False``, which plots the
        phase in radians.
    unwrap : bool, str
        True to unwrap the phase or ``'360'`` to unwrap the phase to 2 pi. The
        default is ``False``, which plots the wrapped phase.
    freq_scale : str
        ``linear`` or ``log`` to plot on a linear or logarithmic frequency
        axis. The default is ``log``.
    ax : matplotlib.axes.Axes
        Axes to plot on. The default is ``None``, which uses the current axis
        or creates a new figure if none exists.
    style : str
        ``light`` or ``dark`` to use the pyfar plot styles or a plot style from
        :py:data:`matplotlib.style.available`. Pass a dictionary to set
        specific plot parameters, for example
        ``style = {'axes.facecolor':'black'}``. Pass an empty dictionary
        ``style = {}`` to use the currently active plotstyle. The default is
        ``light``.
    side : str, optional
        ``'right'`` to plot the right-sided spectrum containing the positive
        frequencies, or ``'left'`` to plot the left-sided spectrum containing
        the negative frequencies (only possible for complex Signals). The
        default is ``'right'``.
    **kwargs
        Keyword arguments that are passed to :py:func:`matplotlib.pyplot.plot`.

    Returns
    -------
    ax : matplotlib.axes.Axes
        Axes or array of axes containing the plot.

    Example
    -------

    .. plot::

        >>> import pyfar as pf
        >>> impulse = pf.signals.impulse(100, 10)
        >>> pf.plot.phase(impulse, unwrap=True)
    """

    with context(style):
        ax = _line._phase(
            signal.flatten(), deg, unwrap, freq_scale, ax, side=side, **kwargs)

    # manage interaction
    plot_parameter = ia.PlotParameter(
        'phase', deg=deg, unwrap=unwrap, xscale=freq_scale, side=side)
    interaction = ia.Interaction(
        signal, ax, None, style, plot_parameter, **kwargs)
    ax.interaction = interaction

    return ax


def group_delay(signal, unit="s", freq_scale='log', ax=None, style='light',
                side='right', **kwargs):
    """Plot the group delay.

    Plots ``pyfar.dsp.group_delay(signal.freq)`` and passes keyword arguments
    (`kwargs`) to :py:func:`matplotlib.pyplot.plot`.

    Parameters
    ----------
    signal : Signal
        The input data to be plotted. Multidimensional data are flattened for
        plotting, e.g, a signal of ``signal.cshape = (2, 2)`` would be plotted
        in the order ``(0, 0)``, ``(0, 1)``, ``(1, 0)``, ``(1, 1)``.
    unit : str, None
        Set the unit of the time axis.

        ``'s'`` (default)
            seconds
        ``'ms'``
            milliseconds
        ``'mus'``
            microseconds
        ``'samples'``
            samples
        ``'auto'``
            Use seconds, milliseconds, or microseconds depending on the length
            of the data.
    freq_scale : str
        ``linear`` or ``log`` to plot on a linear or logarithmic frequency
        axis. The default is ``log``.
    ax : matplotlib.axes.Axes
        Axes to plot on. The default is ``None``, which uses the current axis
        or creates a new figure if none exists.
    style : str
        ``light`` or ``dark`` to use the pyfar plot styles or a plot style from
        :py:data:`matplotlib.style.available`. Pass a dictionary to set
        specific plot parameters, for example
        ``style = {'axes.facecolor':'black'}``. Pass an empty dictionary
        ``style = {}`` to use the currently active plotstyle. The default is
        ``light``.
    side : str, optional
        ``'right'`` to plot the right-sided spectrum containing the positive
        frequencies, or ``'left'`` to plot the left-sided spectrum containing
        the negative frequencies (only possible for complex Signals). The
        default is ``'right'``.
    **kwargs
        Keyword arguments that are passed to :py:func:`matplotlib.pyplot.plot`.

    Returns
    -------
    ax : matplotlib.axes.Axes
        Axes or array of axes containing the plot.

    Examples
    --------
    .. plot::

        >>> import pyfar as pf
        >>> impulse = pf.signals.impulse(100, 10)
        >>> pf.plot.group_delay(impulse, unit='samples')
    """

    with context(style):
        ax = _line._group_delay(
            signal.flatten(), unit, freq_scale, ax, side=side, **kwargs)

    # manage interaction
    plot_parameter = ia.PlotParameter(
        'group_delay', unit_gd=unit, xscale=freq_scale, side=side)
    interaction = ia.Interaction(
        signal, ax, None, style, plot_parameter, **kwargs)
    ax.interaction = interaction

    return ax


def time_freq(signal, dB_time=False, dB_freq=True, log_prefix_time=20,
              log_prefix_freq=None, log_reference=1, freq_scale='log',
              unit="s", ax=None, style='light',
              mode='real', side='right', **kwargs):
    """
    Plot the time signal and magnitude spectrum (2 by 1 subplot).

    Plots ``signal.time`` and ``abs(signal.freq)`` passes keyword arguments
    (`kwargs`) to :py:func:`matplotlib.pyplot.plot`.

    Parameters
    ----------
    signal : Signal
        The input data to be plotted. Multidimensional data are flattened for
        plotting, e.g, a signal of ``signal.cshape = (2, 2)`` would be plotted
        in the order ``(0, 0)``, ``(0, 1)``, ``(1, 0)``, ``(1, 1)``.
    dB_time : bool
        Indicate if the data should be plotted in dB in which case
        ``log_prefix * np.log10(signal.time / log_reference)`` is used. The
        default is ``False``.
    dB_freq : bool
        Indicate if the data should be plotted in dB in which case
        ``log_prefix * np.log10(abs(signal.freq) / log_reference)`` is used.
        The default is ``True``.
    log_prefix_time : integer, float
        Prefix for calculating the logarithmic time data.
        The default is ``20``.
    log_prefix_freq : integer, float
        Prefix for calculating the logarithmic frequency data. The default is
        ``None``, so ``10`` is chosen if ``signal.fft_norm`` is ``'power'`` or
        ``'psd'`` and ``20`` otherwise.
    log_reference : integer
        Reference for calculating the logarithmic time/frequency data.
        The default is ``1``.
    freq_scale : str
        ``linear`` or ``log`` to plot on a linear or logarithmic frequency
        axis. The default is ``log``.
    unit : str, None
        Set the unit of the time axis.

        ``'s'`` (default)
            seconds
        ``'ms'``
            milliseconds
        ``'mus'``
            microseconds
        ``'samples'``
            samples
        ``'auto'``
            Use seconds, milliseconds, or microseconds depending on the length
            of the data.
    ax : matplotlib.axes.Axes
        Array or list with two axes to plot on. The default is ``None``, which
        uses the current axis or creates a new figure if none exists.
    style : str
        ``light`` or ``dark`` to use the pyfar plot styles or a plot style from
        :py:data:`matplotlib.style.available`. Pass a dictionary to set
        specific plot parameters, for example
    mode : str
        ``'real'``, ``'imag'``, or ``'abs'`` to specify if the real part,
        imaginary part or absolute value of the time data is plotted.
        ``'imag'`` and ``'abs'``` can only be used for complex Signals.
        The default is ``'real'``.
    side : str, optional
        ``'right'`` to plot the right-sided spectrum containing the positive
        frequencies, or ``'left'`` to plot the left-sided spectrum containing
        the negative frequencies (only possible for complex Signals). The
        default is ``'right'``.
    **kwargs
        Keyword arguments that are passed to :py:func:`matplotlib.pyplot.plot`.

    Returns
    -------
    ax : matplotlib.axes.Axes
        Axes or array of axes containing the plot.

    Examples
    --------
    .. plot::

        >>> import pyfar as pf
        >>> sine = pf.signals.sine(100, 4410)
        >>> pf.plot.time_freq(sine, unit='ms')
    """

    with context(style):
        ax = _line._time_freq(signal.flatten(), dB_time, dB_freq,
                              log_prefix_time, log_prefix_freq,
                              log_reference, freq_scale, unit, ax,
                              mode=mode, side=side,
                              **kwargs)

    # manage interaction
    plot_parameter = ia.PlotParameter(
        'time_freq', dB_time=dB_time, dB_freq=dB_freq,
        log_prefix_time=log_prefix_time, log_prefix_freq=log_prefix_freq,
        log_reference=log_reference, xscale=freq_scale, unit_time=unit,
        mode=mode, side=side)
    interaction = ia.Interaction(
        signal, ax, None, style, plot_parameter, **kwargs)
    ax[0].interaction = interaction

    return ax


def freq_phase(signal, dB=True, log_prefix=None, log_reference=1,
               freq_scale='log', deg=False, unwrap=False, ax=None,
               style='light', side='right', **kwargs):
    """Plot the magnitude and phase spectrum (2 by 1 subplot).

    Plots ``abs(signal.freq)`` and ``angle(signal.freq)`` and passes keyword
    arguments (`kwargs`) to :py:func:`matplotlib.pyplot.plot`.

    Parameters
    ----------
    signal : Signal, FrequencyData
        The input data to be plotted. Multidimensional data are flattened for
        plotting, e.g, a signal of ``signal.cshape = (2, 2)`` would be plotted
        in the order ``(0, 0)``, ``(0, 1)``, ``(1, 0)``, ``(1, 1)``.
    dB : bool
        Indicate if the data should be plotted in dB in which case
        ``log_prefix * np.log10(abs(signal.freq) / log_reference)`` is used.
        The default is ``True``.
    log_prefix : integer, float
        Prefix for calculating the logarithmic frequency data. The default is
        ``None``, so ``10`` is chosen if ``signal.fft_norm`` is ``'power'`` or
        ``'psd'`` and ``20`` otherwise.
    log_reference : integer
        Reference for calculating the logarithmic frequency data. The default
        is ``1``.
    deg : bool
        Flag to plot the phase in degrees. The default is ``False``.
    unwrap : bool, str
        True to unwrap the phase or ``'360'`` to unwrap the phase to 2 pi. The
        default is ``False``.
    freq_scale : str
        ``linear`` or ``log`` to plot on a linear or logarithmic frequency
        axis. The default is ``log``.
    ax : matplotlib.axes.Axes
        Array or list with two axes to plot on. The default is ``None``, which
        uses the current axis or creates a new figure if none exists.
    style : str
        ``light`` or ``dark`` to use the pyfar plot styles or a plot style from
        :py:data:`matplotlib.style.available`. Pass a dictionary to set
        specific plot parameters, for example
        ``style = {'axes.facecolor':'black'}``. Pass an empty dictionary
        ``style = {}`` to use the currently active plotstyle. The default is
        ``light``.
    side : str, optional
        ``'right'`` to plot the right-sided spectrum containing the positive
        frequencies, or ``'left'`` to plot the left-sided spectrum containing
        the negative frequencies (only possible for complex Signals). The
        default is ``'right'``.
    **kwargs
        Keyword arguments that are forwarded to matplotlib.pyplot.plot

    Returns
    -------
    ax : matplotlib.axes.Axes
        Axes or array of axes containing the plot.

    Examples
    --------
    .. plot::

        >>> import pyfar as pf
        >>> impulse = pf.signals.impulse(100, 10)
        >>> pf.plot.freq_phase(impulse, unwrap=True)
    """

    with context(style):
        ax = _line._freq_phase(signal.flatten(), dB, log_prefix, log_reference,
                               freq_scale, deg, unwrap, ax, side=side,
                               **kwargs)

    # manage interaction
    plot_parameter = ia.PlotParameter(
        'freq_phase', dB_freq=dB, log_prefix_freq=log_prefix,
        log_reference=log_reference, xscale=freq_scale, deg=deg,
        unwrap=unwrap, side=side)
    interaction = ia.Interaction(
        signal, ax, None, style, plot_parameter, **kwargs)
    ax[0].interaction = interaction

    return ax


def freq_group_delay(signal, dB=True, log_prefix=None, log_reference=1,
                     unit="s", freq_scale='log', ax=None, style='light',
                     side='right', **kwargs):
    """Plot the magnitude and group delay spectrum (2 by 1 subplot).

    Plots ``abs(signal.freq)`` and ``pyfar.dsp.group_delay(signal.freq)`` and
    passes keyword arguments (`kwargs`) to :py:func:`matplotlib.pyplot.plot`.

    Parameters
    ----------
    signal : Signal
        The input data to be plotted. Multidimensional data are flattened for
        plotting, e.g, a signal of ``signal.cshape = (2, 2)`` would be plotted
        in the order ``(0, 0)``, ``(0, 1)``, ``(1, 0)``, ``(1, 1)``.
    dB : bool
        Flag to plot the logarithmic magnitude spectrum. The default is
        ``True``.
    log_prefix : integer, float
        Prefix for calculating the logarithmic frequency data. The default is
        ``None``, so ``10`` is chosen if ``signal.fft_norm`` is ``'power'`` or
        ``'psd'`` and ``20`` otherwise.
    log_reference : integer
        Reference for calculating the logarithmic frequency data. The default
        is ``1``.
    unit : str, None
        Set the unit of the time axis.

        ``'s'`` (default)
            seconds
        ``'ms'``
            milliseconds
        ``'mus'``
            microseconds
        ``'samples'``
            samples
        ``'auto'``
            Use seconds, milliseconds, or microseconds depending on the length
            of the data.
    freq_scale : str
        ``linear`` or ``log`` to plot on a linear or logarithmic frequency
        axis. The default is ``log``.
    ax : matplotlib.axes.Axes
        Array or list with two axes to plot on. The default is ``None``, which
        uses the current axis or creates a new figure if none exists.
    style : str
        ``light`` or ``dark`` to use the pyfar plot styles or a plot style from
        :py:data:`matplotlib.style.available`. Pass a dictionary to set
        specific plot parameters, for example
        ``style = {'axes.facecolor':'black'}``. Pass an empty dictionary
        ``style = {}`` to use the currently active plotstyle. The default is
        ``light``.
    side : str, optional
        ``'right'`` to plot the right-sided spectrum containing the positive
        frequencies, or ``'left'`` to plot the left-sided spectrum containing
        the negative frequencies (only possible for complex Signals). The
        default is ``'right'``.
    **kwargs
        Keyword arguments that are passed to :py:func:`matplotlib.pyplot.plot`.

    Returns
    -------
    ax : matplotlib.axes.Axes
        Axes or array of axes containing the plot.

    Examples
    --------
    .. plot::

        >>> import pyfar as pf
        >>> impulse = pf.signals.impulse(100, 10)
        >>> pf.plot.freq_group_delay(impulse, unit='samples')
    """

    with context(style):
        ax = _line._freq_group_delay(
            signal.flatten(), dB, log_prefix, log_reference,
            unit, freq_scale, ax, side=side, **kwargs)

    # manage interaction
    plot_parameter = ia.PlotParameter(
        'freq_group_delay', dB_freq=dB, log_prefix_freq=log_prefix,
        log_reference=log_reference, unit_gd=unit, xscale=freq_scale,
        side=side)
    interaction = ia.Interaction(
        signal, ax, None, style, plot_parameter, **kwargs)
    ax[0].interaction = interaction

    return ax


def custom_subplots(signal, plots, ax=None, style='light', **kwargs):
    """
    Plot multiple pyfar plots with a custom layout and default parameters.

    The plots are passed as a list of :py:mod:`pyfar.plot` function handles.
    The subplot layout is taken from the shape of that list
    (see example below).

    Parameters
    ----------
    signal : Signal
        The input data to be plotted. Multidimensional data are flattened for
        plotting, e.g, a signal of ``signal.cshape = (2, 2)`` would be plotted
        in the order ``(0, 0)``, ``(0, 1)``, ``(1, 0)``, ``(1, 1)``.
    plots : list, nested list
        Function handles for plotting.
    ax : matplotlib.axes.Axes
        Axes to plot on. The default is ``None``, which uses the current axis
        or creates a new figure if none exists.
    style : str
        ``light`` or ``dark`` to use the pyfar plot styles or a plot style from
        :py:data:`matplotlib.style.available`. Pass a dictionary to set
        specific plot parameters, for example
        ``style = {'axes.facecolor':'black'}``. Pass an empty dictionary
        ``style = {}`` to use the currently active plotstyle. The default is
        ``light``.
    **kwargs
        Keyword arguments that are passed to :py:func:`matplotlib.pyplot.plot`.

    Returns
    -------
    ax : list of matplotlib.axes.Axes
        List of axes handles

    Examples
    --------
    Generate a two by two subplot layout

    .. plot::

        >>> import pyfar as pf
        >>> impulse = pf.signals.impulse(100, 10)
        >>> plots = [[pf.plot.time, pf.plot.phase],
        ...          [pf.plot.freq, pf.plot.group_delay]]
        >>> pf.plot.custom_subplots(impulse, plots)

    """

    with context(style):
        ax = _line._custom_subplots(signal.flatten(), plots, ax, **kwargs)

    return ax
