import numpy as np
import numpy.testing as npt
import pytest

import pyfar as pf
import pyfar.classes.audio as signal
from pyfar import Signal, TimeData, FrequencyData


# test adding two Signals
def test_add_two_signals_time():
    # generate test signal
    x = Signal([1, 0, 0], 44100)

    # time domain
    y = pf.add((x, x), 'time')
    # check if old signal did not change
    npt.assert_allclose(x.time, np.atleast_2d([1, 0, 0]), atol=1e-15)
    # check result
    assert isinstance(y, Signal)
    assert y.domain == 'time'
    npt.assert_allclose(y.time, np.atleast_2d([2, 0, 0]), atol=1e-15)


# test adding two complex time signals
def test_add_two_signals_time_complex():
    # generate test signal
    x = Signal([1, 0, 0], 44100, is_complex=True)

    # time domain
    y = pf.add((x, x), 'time')

    # check if old signal did not change
    npt.assert_allclose(x.time, np.atleast_2d([1, 0, 0]), atol=1e-15)
    # check result
    assert isinstance(y, Signal)
    assert y.complex
    assert y.domain == 'time'
    npt.assert_allclose(y.time, np.atleast_2d([2 + 0j, 0, 0]), atol=1e-15)


# test adding two complex time signals
def test_add_two_signal_time_real_and_complex():
    # generate test signal
    x = Signal([1, 0, 0], 44100, is_complex=True)
    y = Signal([1, 0, 0], 44100, is_complex=False)

    # time domain
    z = pf.add((x, y), 'time')

    # check if old signals did not change
    npt.assert_allclose(x.time, np.atleast_2d([1+0j, 0+0j, 0+0j]), atol=1e-15)
    npt.assert_allclose(y.time, np.atleast_2d([1, 0, 0]), atol=1e-15)

    # check result
    assert isinstance(z, Signal)
    assert z.complex
    assert z.domain == 'time'
    npt.assert_allclose(z.time, np.atleast_2d([2 + 0j, 0 + 0j, 0 + 0j]),
                        atol=1e-15)


# test adding two Signals
def test_add_two_signals_freq():
    # generate test signal
    x = Signal([1, 0, 0], 44100)

    # frequency domain
    y = pf.add((x, x), 'freq')
    # check if old signal did not change
    npt.assert_allclose(x.time, np.atleast_2d([1, 0, 0]), atol=1e-15)
    # check result
    assert isinstance(y, Signal)
    assert y.domain == 'freq'
    npt.assert_allclose(y.freq, np.atleast_2d([2, 2]), atol=1e-15)


# test adding two Signals
def test_add_two_signals_freq_complex():
    # generate test signal
    x = Signal([1, 0, 0], 44100, is_complex=True)

    # frequency domain
    y = pf.add((x, x), 'freq')
    # check if old signal did not change
    npt.assert_allclose(x.time, np.atleast_2d([1 + 0j, 0 + 0j, 0 + 0j]),
                        atol=1e-15)

    # check result
    assert isinstance(y, Signal)
    assert y.domain == 'freq'
    assert y.complex
    npt.assert_allclose(y.freq, np.atleast_2d([2 + 0j, 2 + 0j, 2 + 0j]),
                        atol=1e-15)


# test adding two Signals
def test_add_two_signals_freq_real_and_complex():
    # generate test signal
    x = Signal([1, 0, 0], 44100, is_complex=True)
    y = Signal([1, 0, 0], 44100, is_complex=False)

    # frequency domain
    z = pf.add((x, x), 'freq')
    # check if old signal did not change
    npt.assert_allclose(x.time, np.atleast_2d([1 + 0j, 0 + 0j, 0 + 0j]),
                        atol=1e-15)
    npt.assert_allclose(y.time, np.atleast_2d([1, 0, 0]), atol=1e-15)

    # check result
    assert isinstance(z, Signal)
    assert z.domain == 'freq'
    assert z.complex
    npt.assert_allclose(z.freq, np.atleast_2d([2 + 0j, 2 + 0j, 2 + 0j]),
                        atol=1e-15)


# test adding three signals
def test_add_three_signals():
    # generate and add signals
    x = Signal([1, 0, 0], 44100)
    y = pf.add((x, x, x), 'time')

    # check if old signal did not change
    npt.assert_allclose(x.time, np.atleast_2d([1, 0, 0]), atol=1e-15)

    # check result
    assert isinstance(y, Signal)
    assert y.domain == 'time'
    npt.assert_allclose(y.time, np.atleast_2d([3, 0, 0]), atol=1e-15)


# test add Signals and number
def test_add_signal_and_number():
    # generate and add signals
    x = Signal([1, 0, 0], 44100)
    y = pf.add((x, 1), 'time')

    # check if old signal did not change
    npt.assert_allclose(x.time, np.atleast_2d([1, 0, 0]), atol=1e-15)

    # check result
    assert isinstance(y, Signal)
    assert y.domain == 'time'
    npt.assert_allclose(y.time, np.atleast_2d([2, 1, 1]), atol=1e-15)


# test add Signals and number
def test_add_signal_and_complex_number():
    # generate and add signals
    x = Signal([1, 0, 0], 44100)
    y = pf.add((x, 1 + 1j), 'time')

    # check if old signal did not change
    npt.assert_allclose(x.time, np.atleast_2d([1, 0, 0]), atol=1e-15)

    # check result
    assert isinstance(y, Signal)
    assert y.domain == 'time'
    assert y.complex
    npt.assert_allclose(y.time, np.atleast_2d([2 + 1j, 1 + 1j, 1 + 1j]),
                        atol=1e-15)


# test add number and Signal
def test_add_number_and_signal():
    # generate and add signals
    x = Signal([1, 0, 0], 44100)
    y = pf.add((1, x), 'time')

    # check if old signal did not change
    npt.assert_allclose(x.time, np.atleast_2d([1, 0, 0]), atol=1e-15)

    # check result
    assert isinstance(y, Signal)
    assert y.domain == 'time'
    npt.assert_allclose(y.time, np.atleast_2d([2, 1, 1]), atol=1e-15)


# test add number and complex signal
def test_add_number_and_complex_signal():
    # generate and add signals
    x = Signal([1, 0, 0], 44100, is_complex=True)
    y = pf.add((1, x), 'time')

    # check if old signal did not change
    npt.assert_allclose(x.time, np.atleast_2d([1, 0, 0]), atol=1e-15)

    # check result
    assert isinstance(y, Signal)
    assert y.domain == 'time'
    assert y.complex
    npt.assert_allclose(y.time, np.atleast_2d([2 + 0j, 1 + 0j, 1 + 0j]),
                        atol=1e-15)


# test add number and complex signal
def test_add_number_and_complex_signal_freq():
    # generate and add signals
    x = Signal([1, 0, 0], 44100, is_complex=True)
    y = pf.add((1, x), 'freq')

    # check if old signal did not change
    npt.assert_allclose(x.time, np.atleast_2d([1, 0, 0]), atol=1e-15)

    # check result
    assert isinstance(y, Signal)
    assert y.domain == 'freq'
    assert y.complex
    npt.assert_allclose(y.freq, np.atleast_2d([2 + 0j, 2 + 0j, 2 + 0j]),
                        atol=1e-15)


def test_add_time_data_and_number():
    # generate and add signals
    x = TimeData([1, 0, 0], [0, .1, .5])
    y = pf.add((x, 1), 'time')

    # check if old signal did not change
    npt.assert_allclose(x.time, np.atleast_2d([1, 0, 0]), atol=1e-15)
    npt.assert_allclose(x.times, np.atleast_1d([0, .1, .5]), atol=1e-15)

    # check result
    assert isinstance(y, TimeData)
    npt.assert_allclose(y.time, np.atleast_2d([2, 1, 1]), atol=1e-15)
    npt.assert_allclose(y.times, np.atleast_1d([0, .1, .5]), atol=1e-15)


def test_add_time_data_and_time_data():
    # generate and add signals
    x = TimeData([1, 0, 0], [0, .1, .5])
    y = pf.add((x, x), 'time')

    # check if old signal did not change
    npt.assert_allclose(x.time, np.atleast_2d([1, 0, 0]), atol=1e-15)
    npt.assert_allclose(x.times, np.atleast_1d([0, .1, .5]), atol=1e-15)

    # check result
    assert isinstance(y, TimeData)
    npt.assert_allclose(y.time, np.atleast_2d([2, 0, 0]), atol=1e-15)
    npt.assert_allclose(y.times, np.atleast_1d([0, .1, .5]), atol=1e-15)


def test_add_time_data_and_number_wrong_domain():
    # generate and add signals
    x = TimeData([1, 0, 0], [0, .1, .5])
    match = "The domain must be 'time'."
    with pytest.raises(ValueError, match=match):
        pf.add((x, 1), 'freq')


def test_add_time_data_and_number_wrong_times():
    # generate and add signals
    x = TimeData([1, 0, 0], [0, .1, .5])
    y = TimeData([1, 0, 0], [0, .1, .4])
    match = 'The times does not match.'
    with pytest.raises(ValueError, match=match):
        pf.add((x, y), 'time')


def test_add_frequency_data_and_number():
    # generate and add signals
    x = FrequencyData([1, 0, 0], [0, .1, .5])
    y = pf.add((x, 1), 'freq')
    match = "The domain must be 'freq'."
    with pytest.raises(ValueError, match=match):
        pf.add((x, 1), 'time')

    # check if old signal did not change
    npt.assert_allclose(x.freq, np.atleast_2d([1, 0, 0]), atol=1e-15)
    npt.assert_allclose(x.frequencies, np.atleast_1d([0, .1, .5]), atol=1e-15)

    # check result
    assert isinstance(y, FrequencyData)
    npt.assert_allclose(y.freq, np.atleast_2d([2, 1, 1]), atol=1e-15)
    npt.assert_allclose(y.frequencies, np.atleast_1d([0, .1, .5]), atol=1e-15)


def test_add_frequency_data_and_frequency_data():
    # generate and add signals
    x = FrequencyData([1, 0, 0], [0, .1, .5])
    y = pf.add((x, x), 'freq')

    # check if old signal did not change
    npt.assert_allclose(x.freq, np.atleast_2d([1, 0, 0]), atol=1e-15)
    npt.assert_allclose(x.frequencies, np.atleast_1d([0, .1, .5]), atol=1e-15)

    # check result
    assert isinstance(y, FrequencyData)
    npt.assert_allclose(y.freq, np.atleast_2d([2, 0, 0]), atol=1e-15)
    npt.assert_allclose(y.frequencies, np.atleast_1d([0, .1, .5]), atol=1e-15)


def test_add_frequency_data_and_number_wrong_domain():
    # generate and add signals
    x = FrequencyData([1, 0, 0], [0, .1, .5])
    match = "The domain must be 'freq'."
    with pytest.raises(ValueError, match=match):
        pf.add((x, 1), 'time')


def test_add_frequency_data_and_number_wrong_frequencies():
    # generate and add signals
    x = FrequencyData([1, 0, 0], [0, .1, .5])
    y = FrequencyData([1, 0, 0], [0, .1, .4])
    match = 'The frequencies do not match.'
    with pytest.raises(ValueError, match=match):
        pf.add((x, y), 'freq')


def test_add_array_and_signal():
    # shapes match
    x = np.arange(2 * 3 * 4).reshape((2, 3, 4))
    y = pf.signals.impulse(10, amplitude=np.ones((2, 3, 4)))
    z = pf.add((x, y))
    npt.assert_allclose(
        z.freq, np.ones_like(z.freq)*x[..., None] + 1, atol=1e-15)
    # broadcasting
    x = np.arange(3 * 4).reshape((3, 4))
    y = pf.signals.impulse(10, amplitude=np.ones((2, 3, 4)))
    z = pf.add((x, y))
    npt.assert_allclose(
        z.freq, np.ones_like(z.freq)*x[..., None] + 1, atol=1e-15)


def test_add_signal_and_array():
    # shapes match
    x = pf.signals.impulse(10, amplitude=np.ones((2, 3, 4)))
    y = np.arange(2 * 3 * 4).reshape((2, 3, 4))
    z = pf.add((x, y))
    npt.assert_allclose(
        z.freq, np.ones_like(z.freq)*y[..., None] + 1, atol=1e-15)
    # broadcasting
    x = pf.signals.impulse(10, amplitude=np.ones((2, 3, 4)))
    y = np.arange(3 * 4).reshape((3, 4))
    z = pf.add((x, y))
    npt.assert_allclose(
        z.freq, np.ones_like(z.freq)*y[..., None] + 1, atol=1e-15)


def test_add_arrays():
    # With broadcasting
    x = np.arange(2 * 3 * 4).reshape((2, 3, 4))
    y = np.arange(2 * 3 * 4).reshape((2, 3, 4))
    z = pf.add((x, y))
    npt.assert_allclose(
        z, x + y, atol=1e-15)


@pytest.mark.parametrize('fft_norm', ['none', 'rms'])
def test_signal_inversion(fft_norm):
    """Test signal inversion with different FFT norms."""

    signal = pf.Signal([2, 0, 0], 44100, fft_norm=fft_norm)
    signal_inv = 1 / signal
    npt.assert_allclose(signal.time.flatten(), [2, 0, 0])
    npt.assert_allclose(signal_inv.time.flatten(), [.5, 0, 0])


def test_subtraction():
    # only test one case - everything else is tested below
    x = Signal([1, 0, 0], 44100)
    y = Signal([0, 1, 0], 44100)
    z = pf.subtract((x, y), 'time')

    # check result
    npt.assert_allclose(z.time, np.atleast_2d([1, -1, 0]), atol=1e-15)


def test_multiplication():
    # only test one case - everything else is tested below
    x = Signal([1, 0, 0], 44100)
    y = Signal([0, 1, 0], 44100)
    z = pf.multiply((x, y), 'time')

    # check result
    npt.assert_allclose(z.time, np.atleast_2d([0, 0, 0]), atol=1e-15)


def test_complex_multiplication():
    # only test one case - everything else is tested below
    x = Signal([1, 0, 0], 44100, is_complex=True)
    y = Signal([0, 1, 0], 44100, is_complex=True)
    z = pf.multiply((x, y), 'time')

    # check result
    npt.assert_allclose(z.time, np.atleast_2d([0 + 0j, 0 + 0j, 0 + 0j]),
                        atol=1e-15)


def test_complex_real_multiplication():
    # only test one case - everything else is tested below
    x = Signal([1, 0, 0], 44100)
    y = Signal([0, 1, 0], 44100, is_complex=True)
    z = pf.multiply((x, y), 'time')

    # check result
    npt.assert_allclose(z.time, np.atleast_2d([0 + 0j, 0 + 0j, 0 + 0j]),
                        atol=1e-15)

    x = Signal([1, 0, 0], 44100, is_complex=True)
    y = Signal([0, 1, 0], 44100)
    z = pf.multiply((x, y), 'time')

    # check result
    npt.assert_allclose(z.time, np.atleast_2d([0 + 0j, 0 + 0j, 0 + 0j]),
                        atol=1e-15)


def test_complex_real_multiplication_freq():
    # only test one case - everything else is tested below
    x = Signal([1, 0, 0], 44100)
    y = Signal([0, 1, 0], 44100, is_complex=True)
    z = pf.multiply((x, y), 'freq')

    # check result
    x.complex = True
    ref = x.freq * y.freq
    npt.assert_allclose(z.freq, ref, atol=1e-15)

    x = Signal([1, 0, 0], 44100, is_complex=True)
    y = Signal([0, 1, 0], 44100)
    z = pf.multiply((x, y), 'freq')

    # check result
    y.complex = True
    ref = x.freq * y.freq
    npt.assert_allclose(z.freq, ref, atol=1e-15)


def test_division():
    # only test one case - everything else is tested below
    x = Signal([1, 0, 0], 44100)
    y = Signal([2, 2, 2], 44100)
    z = pf.divide((x, y), 'time')

    # check result
    npt.assert_allclose(z.time, np.atleast_2d([0.5, 0, 0]), atol=1e-15)


def test_complex_division():
    # only test one case - everything else is tested below
    x = Signal([1, 0, 0], 44100)
    y = Signal([2, 2, 2], 44100, is_complex=True)
    z = pf.divide((x, y), 'time')

    # check result
    npt.assert_allclose(z.time, np.atleast_2d([0.5 + 0j, 0 + 0j, 0 + 0j]),
                        atol=1e-15)


def test_power():
    # only test one case - everything else is tested below
    x = Signal([2, 1, 0], 44100)
    y = Signal([2, 2, 2], 44100)
    z = pf.power((x, y), 'time')

    # check result
    npt.assert_allclose(z.time, np.atleast_2d([4, 1, 0]), atol=1e-15)


def test_overloaded_operators_signal():
    x = Signal([3, 2, 1], 44100, n_samples=5, domain='freq')
    y_s = Signal([2, 2, 2], 44100, n_samples=5, domain='freq')

    for y in [y_s, 2]:
        # addition
        z = x + y
        npt.assert_allclose(z.freq, np.array([5, 4, 3], ndmin=2), atol=1e-15)
        z = y + x
        npt.assert_allclose(z.freq, np.array([5, 4, 3], ndmin=2), atol=1e-15)
        # subtraction
        z = x - y
        npt.assert_allclose(z.freq, np.array([1, 0, -1], ndmin=2), atol=1e-15)
        z = y - x
        npt.assert_allclose(z.freq, np.array([-1, 0, 1], ndmin=2), atol=1e-15)
        # multiplication
        z = x * y
        npt.assert_allclose(z.freq, np.array([6, 4, 2], ndmin=2), atol=1e-15)
        z = y * x
        npt.assert_allclose(z.freq, np.array([6, 4, 2], ndmin=2), atol=1e-15)
        # division
        z = x / y
        npt.assert_allclose(
            z.freq, np.array([1.5, 1, .5], ndmin=2), atol=1e-15)
        z = y / x
        npt.assert_allclose(z.freq, np.array([2/3, 1, 2], ndmin=2), atol=1e-15)
        # power
        z = x**y
        npt.assert_allclose(z.freq, np.array([9, 4, 1], ndmin=2), atol=1e-15)
        z = y**x
        npt.assert_allclose(z.freq, np.array([8, 4, 2], ndmin=2), atol=1e-15)


def test_overloaded_operators_time_data():
    x = TimeData([3, 2, 1], [0, 1, 2])
    y_s = TimeData([2, 2, 2], [0, 1, 2])

    for y in [y_s, 2]:
        # addition
        z = x + y
        npt.assert_allclose(z.time, np.array([5, 4, 3], ndmin=2), atol=1e-15)
        z = y + x
        npt.assert_allclose(z.time, np.array([5, 4, 3], ndmin=2), atol=1e-15)
        # subtraction
        z = x - y
        npt.assert_allclose(z.time, np.array([1, 0, -1], ndmin=2), atol=1e-15)
        z = y - x
        npt.assert_allclose(z.time, np.array([-1, 0, 1], ndmin=2), atol=1e-15)
        # multiplication
        z = x * y
        npt.assert_allclose(z.time, np.array([6, 4, 2], ndmin=2), atol=1e-15)
        z = y * x
        npt.assert_allclose(z.time, np.array([6, 4, 2], ndmin=2), atol=1e-15)
        # division
        z = x / y
        npt.assert_allclose(
            z.time, np.array([1.5, 1, .5], ndmin=2), atol=1e-15)
        z = y / x
        npt.assert_allclose(z.time, np.array([2/3, 1, 2], ndmin=2), atol=1e-15)
        # power
        z = x**y
        npt.assert_allclose(z.time, np.array([9, 4, 1], ndmin=2), atol=1e-15)
        z = y**x
        npt.assert_allclose(z.time, np.array([8, 4, 2], ndmin=2), atol=1e-15)


def test_overloaded_operators_frequency_data():
    x = FrequencyData([3, 2, 1], [0, 1, 2])
    y_s = FrequencyData([2, 2, 2], [0, 1, 2])

    for y in [y_s, 2]:
        # addition
        z = x + y
        npt.assert_allclose(z.freq, np.array([5, 4, 3], ndmin=2), atol=1e-15)
        z = y + x
        npt.assert_allclose(z.freq, np.array([5, 4, 3], ndmin=2), atol=1e-15)
        # subtraction
        z = x - y
        npt.assert_allclose(z.freq, np.array([1, 0, -1], ndmin=2), atol=1e-15)
        z = y - x
        npt.assert_allclose(z.freq, np.array([-1, 0, 1], ndmin=2), atol=1e-15)
        # multiplication
        z = x * y
        npt.assert_allclose(z.freq, np.array([6, 4, 2], ndmin=2), atol=1e-15)
        z = y * x
        npt.assert_allclose(z.freq, np.array([6, 4, 2], ndmin=2), atol=1e-15)
        # division
        z = x / y
        npt.assert_allclose(
            z.freq, np.array([1.5, 1, .5], ndmin=2), atol=1e-15)
        z = y / x
        npt.assert_allclose(z.freq, np.array([2/3, 1, 2], ndmin=2), atol=1e-15)
        # power
        z = x**y
        npt.assert_allclose(z.freq, np.array([9, 4, 1], ndmin=2), atol=1e-15)
        z = y**x
        npt.assert_allclose(z.freq, np.array([8, 4, 2], ndmin=2), atol=1e-15)


def test_overloaded_operators_array_and_signal():
    x = np.arange(2 * 3 * 4).reshape(2, 3, 4) + 1
    y = Signal(np.ones((2, 3, 4, 5)), 44100, n_samples=8, domain='freq')

    # addition
    z = x + y
    npt.assert_allclose(
        z.freq, np.ones((2, 3, 4, 5)) * x[..., None] + 1, atol=1e-15)
    z = y + x
    npt.assert_allclose(
        z.freq, np.ones((2, 3, 4, 5)) * x[..., None] + 1, atol=1e-15)
    # subtraction
    z = x - y
    npt.assert_allclose(
        z.freq, np.ones((2, 3, 4, 5)) * x[..., None] - 1, atol=1e-15)
    z = y - x
    npt.assert_allclose(
        z.freq, -1 * (np.ones((2, 3, 4, 5)) * x[..., None] - 1), atol=1e-15)
    # multiplication
    z = x * y
    npt.assert_allclose(
        z.freq, np.ones((2, 3, 4, 5)) * x[..., None], atol=1e-15)
    z = y * x
    npt.assert_allclose(
        z.freq, np.ones((2, 3, 4, 5)) * x[..., None], atol=1e-15)
    # division
    z = x / y
    npt.assert_allclose(
        z.freq, np.ones((2, 3, 4, 5)) * x[..., None], atol=1e-15)
    z = y / x
    npt.assert_allclose(
        z.freq, np.ones((2, 3, 4, 5)) / x[..., None], atol=1e-15)
    # power
    z = x**y
    npt.assert_allclose(
        z.freq, np.ones((2, 3, 4, 5)) * x[..., None], atol=1e-15)
    z = y**x
    npt.assert_allclose(
        z.freq, np.ones((2, 3, 4, 5)), atol=1e-15)


def test_assert_match_for_arithmetic():
    s = Signal([1, 2, 3, 4], 44100)
    s1 = Signal([1, 2, 3, 4], 48000)
    s2 = Signal([1, 2, 3], 44100)
    s4 = Signal([1, 2, 3, 4], 44100, fft_norm="rms")
    s5 = Signal([1 + 1j, 2 + 2j, 3 + 3j, 4 + 4j], 48000, is_complex=True)
    s6 = FrequencyData([1 + 1j, 2 + 2j, 3 + 3j, 4 + 4j],
                       [10, 200, 1000, 20000])

    # check with two signals
    signal._assert_match_for_arithmetic(
        (s, s), 'time', division=False, matmul=False)
    # check with one signal and one array like
    signal._assert_match_for_arithmetic(
        (s, [1, 2]), 'time', division=False, matmul=False)
    # check with more than two inputs
    signal._assert_match_for_arithmetic(
        (s, s, s), 'time', division=False, matmul=False)

    # check output
    out = signal._assert_match_for_arithmetic(
        (s, s), 'time', division=False, matmul=False)
    assert out[0] == 44100
    assert out[1] == 4
    assert out[2] == 'none'
    assert out[6] == (1,)
    assert not out[7]
    out = signal._assert_match_for_arithmetic(
        (s, s4), 'time', division=False, matmul=False)
    assert out[2] == 'rms'

    # check if complex flag is set with two complex-valued
    # signals
    out = signal._assert_match_for_arithmetic(
        (s5, s5), 'time', division=False, matmul=False)
    assert out[7]

    # check if complex flag is not set with two real-valued
    # signals
    out = signal._assert_match_for_arithmetic(
        (s, s), 'time', division=False, matmul=False)
    assert not out[7]

    # check if complex flag is set with one complex and
    # one real-valued signal
    out = signal._assert_match_for_arithmetic(
        (s5, s1), 'time', division=False, matmul=False)
    assert out[7]

    # check if complex flag is set with one complex and
    # one real-valued signal
    out = signal._assert_match_for_arithmetic(
        (s1, s5), 'time', division=False, matmul=False)
    assert out[7]

    # check if complex flag is set with one real-valued
    # signal and one complex-valued number passed at position
    # position 1
    out = signal._assert_match_for_arithmetic(
        (1 + 1j, s5), 'time', division=False, matmul=False)
    assert out[7]

    # check if complex flag is set with one real-valued
    # signal and one complex-valued number passed at position
    # position 2
    out = signal._assert_match_for_arithmetic(
        (s5, 1 + 1j), 'time', division=False, matmul=False)
    assert out[7]

    # check if complex flag is not set with one real-valued
    # signal and one real-valued number passed at position
    # position 1
    out = signal._assert_match_for_arithmetic(
        (1, s), 'time', division=False, matmul=False)
    assert not out[7]

    # check if complex flag is not set with one real-valued
    # signal and one real-valued number passed at position
    # position 2
    out = signal._assert_match_for_arithmetic(
        (s, 1), 'time', division=False, matmul=False)
    assert not out[7]

    # check if complex flag is not set with one frequencyData
    # and one real-valued number passed at position 1
    out = signal._assert_match_for_arithmetic(
        (1, s6), 'freq', division=False, matmul=False)
    assert not out[7]

    # check if complex flag is not set with one frequencyData
    # and one complex-valued number passed at position 2
    out = signal._assert_match_for_arithmetic(
        (s6, 1), 'freq', division=False, matmul=False)
    assert not out[7]

    # check if complex flag is not set with one frequencyData
    # and one complex-valued number passed at position 1
    out = signal._assert_match_for_arithmetic(
        (1 + 1j, s6), 'freq', division=False, matmul=False)
    assert not out[7]

    # check if complex flag is not set with one frequencyData
    # and one complex-valued number passed at position 2
    out = signal._assert_match_for_arithmetic(
        (s6, 1 + 1j), 'freq', division=False, matmul=False)
    assert not out[7]

    # check with non-tuple input for first argument
    match = "Input argument 'data' must be a tuple."
    with pytest.raises(ValueError, match=match):
        signal._assert_match_for_arithmetic(
            s, 'time', division=False, matmul=False)
    # check with invalid data type in first argument
    match = 'Input must be of type Signal, int, float, or complex'
    with pytest.raises(ValueError, match=match):
        signal._assert_match_for_arithmetic(
            (s, ['str', 'ing']), 'time', division=False, matmul=False)
    # test signals with different sampling rates
    match = 'The sampling rates do not match'
    with pytest.raises(ValueError, match=match):
        signal._assert_match_for_arithmetic(
            (s, s1), 'time', division=False, matmul=False)
    # test signals with different n_samples
    match = 'The number of samples does not match'
    with pytest.raises(ValueError, match=match):
        signal._assert_match_for_arithmetic(
            (s, s2), 'time', division=False, matmul=False)


def test_get_arithmetic_data_with_array():
    data_in = np.asarray(1)
    data_out = signal._get_arithmetic_data(
        data_in, None, (1,), False, type(None), contains_complex=False)
    npt.assert_allclose(data_in, data_out)


def test_get_arithmetic_data_with_signal():
    # all possible combinations of `domain`, `signal_type`, and `fft_norm`
    meta = [['time', 'none'],
            ['freq', 'none'],
            ['time', 'unitary'],
            ['freq', 'unitary'],
            ['time', 'amplitude'],
            ['freq', 'amplitude'],
            ['time', 'rms'],
            ['freq', 'rms'],
            ['time', 'power'],
            ['freq', 'power'],
            ['time', 'psd'],
            ['freq', 'psd']]

    # reference signal - _get_arithmetic_data should return the data without
    # any normalization regardless of the input data
    s_ref = Signal([1, 0, 0], 44100)

    for m_in in meta:
        # create input signal with current domain, type, and norm
        s_in = Signal([1, 0, 0], 44100, fft_norm=m_in[1])
        s_in.domain = m_in[0]
        for domain in ['time', 'freq']:
            print(f"Testing from {m_in[0]} ({m_in[1]}) to {domain}.")

            # get output data
            data_out = signal._get_arithmetic_data(
                s_in, domain=domain, cshape=(1,), matmul=False,
                audio_type=Signal, contains_complex=False)
            if domain == 'time':
                npt.assert_allclose(s_ref.time, data_out, atol=1e-15)
            elif domain == 'freq':
                npt.assert_allclose(s_ref.freq, data_out, atol=1e-15)


def test_get_arithmetic_data_with_signal_complex_casting():
    s_in = Signal([1, 0, 0], 44100, is_complex=False)

    data_out = signal._get_arithmetic_data(
        s_in, 'time', (1,), False, type(None), contains_complex=True)

    assert data_out.dtype == 'complex'


def test_assert_match_for_arithmetic_data_different_audio_classes():
    match = 'The audio objects do not match.'
    with pytest.raises(ValueError, match=match):
        signal._assert_match_for_arithmetic(
            (Signal(1, 1), TimeData(1, 1)), 'time', division=False,
            matmul=False)


def test_assert_match_for_arithmetic_data_wrong_domain():
    match = 'domain must be time or freq but is space.'
    with pytest.raises(ValueError, match=match):
        signal._assert_match_for_arithmetic(
            (1, 1), 'space', division=False, matmul=False)


def test_assert_match_for_arithmetic_data_wrong_cshape():
    x = Signal(np.ones((2, 3, 4)), 44100)
    y = Signal(np.ones((5, 4)), 44100)
    with pytest.raises(ValueError, match="The cshapes"):
        signal._assert_match_for_arithmetic(
            (x, y), 'freq', division=False, matmul=False)


def test_get_arithmetic_data_wrong_domain():
    match = "domain must be 'time' or 'freq' but found space"
    with pytest.raises(ValueError, match=match):
        signal._get_arithmetic_data(
            Signal(1, 44100), 'space', (1,), False, Signal,
            contains_complex=False)


def test_array_broadcasting_errors():
    x = np.arange(2 * 3 * 4 * 10).reshape((2, 3, 4, 10))
    y = pf.signals.impulse(10, amplitude=np.ones((2, 3, 4)))
    with pytest.raises(ValueError, match="array dimension"):
        pf.add((x, y), domain='time')

    x = np.arange(2 * 3 * 4).reshape((2, 3, 4))
    y = pf.signals.impulse(10, amplitude=np.ones((2, 3, 5)))
    match = 'operands could not be broadcast together with shapes'
    with pytest.raises(ValueError, match=match):
        pf.add((x, y))


def test_matrix_multiplication_default():
    """Test default behavior for signals."""
    x = pf.signals.impulse(10, amplitude=np.array([[1, 2, 3], [4, 5, 6]]))
    y = pf.signals.impulse(10, amplitude=np.array([[1, 2], [3, 4], [5, 6]]))
    z = pf.matrix_multiplication((x, y))
    desired = np.array([[22, 28], [49, 64]])[..., None] * np.ones((2, 2, 6))
    npt.assert_allclose(z.freq, desired, atol=1e-15)


def test_matrix_multiplication_time_domain():
    """Time domain multiplication for signals."""
    x = pf.signals.impulse(10, amplitude=np.array([[1, 2, 3], [4, 5, 6]]))
    y = pf.signals.impulse(10, amplitude=np.array([[1, 2], [3, 4], [5, 6]]))
    z = pf.matrix_multiplication((x, y), domain='time')
    desired = np.zeros((2, 2, 10))
    desired[..., 0] = np.array([[22, 28], [49, 64]])
    npt.assert_allclose(z.time, desired, atol=1e-15)


def test_matrix_multiplication_operator():
    """Test overloaded @ operator."""
    x = pf.signals.impulse(10, amplitude=np.array([[1, 2, 3], [4, 5, 6]]))
    y = pf.signals.impulse(10, amplitude=np.array([[1, 2], [3, 4], [5, 6]]))
    z = x @ y
    desired = np.array([[22, 28], [49, 64]])[..., None] * np.ones((2, 2, 6))
    npt.assert_allclose(z.freq, desired, atol=1e-15)
    z = y @ x
    desired = np.array([[9, 12, 15], [19, 26, 33], [29, 40, 51]])[..., None] \
        * np.ones((3, 3, 6))
    npt.assert_allclose(z.freq, desired, atol=1e-15)


def test_matrix_multiplication_higher_shape():
    """Test correct multiplication nd signals."""
    x = pf.signals.impulse(10, amplitude=np.ones((2, 3, 4)))
    y = pf.signals.impulse(10, amplitude=np.ones((2, 4, 5)))
    z = pf.matrix_multiplication((x, y))
    desired = 4 * np.ones((2, 3, 5, 6))
    npt.assert_allclose(z.freq, desired, atol=1e-15)


def test_matrix_multiplication_shape_mismatch():
    """Test error for shape mismatch."""
    # Signals
    x = pf.signals.impulse(10, amplitude=np.array([[1, 2, 3], [4, 5, 6]]))
    y = pf.signals.impulse(10, amplitude=np.array([[1, 2], [3, 4]]))
    with pytest.raises(ValueError, match="matmul: Input operand 1"):
        pf.matrix_multiplication((x, y))
    # Signal and array
    y = np.ones((2, 2, 6)) * np.array([[1, 2], [3, 4]])[..., None]
    with pytest.raises(ValueError, match="matmul: Input operand 1"):
        pf.matrix_multiplication((x, y))


def test_matrix_multiplication_TimeData():
    """Test @ operate for TimeData."""
    times = np.arange(10)
    xdata = np.ones((2, 3, 10)) * np.array([[1, 2, 3], [4, 5, 6]])[..., None]
    ydata = np.ones((3, 2, 10)) * np.array([[1, 2], [3, 4], [5, 6]])[..., None]
    x = pf.TimeData(xdata, times)
    y = pf.TimeData(ydata, times)
    z = x @ y
    desired = np.array([[22, 28], [49, 64]])[..., None] * np.ones((2, 2, 10))
    npt.assert_allclose(z.time, desired, atol=1e-15)
    z = y @ x
    desired = np.array([[9, 12, 15], [19, 26, 33], [29, 40, 51]])[..., None] \
        * np.ones((3, 3, 10))
    npt.assert_allclose(z.time, desired, atol=1e-15)


def test_matrix_multiplication_FrequencyData():
    """Test @ operator for FrequencyData."""
    freqs = np.arange(10)
    xdata = np.ones((2, 3, 10)) * np.array([[1, 2, 3], [4, 5, 6]])[..., None]
    ydata = np.ones((3, 2, 10)) * np.array([[1, 2], [3, 4], [5, 6]])[..., None]
    x = pf.FrequencyData(xdata, freqs)
    y = pf.FrequencyData(ydata, freqs)
    z = x @ y
    desired = np.array([[22, 28], [49, 64]])[..., None] * np.ones((2, 2, 10))
    npt.assert_allclose(z.freq, desired, atol=1e-15)
    z = y @ x
    desired = np.array([[9, 12, 15], [19, 26, 33], [29, 40, 51]])[..., None] \
        * np.ones((3, 3, 10))
    npt.assert_allclose(z.freq, desired, atol=1e-15)


def test_matrix_multiplication_frequency_axis():
    """Test frequency dependent matrix explicitly."""
    freqs = np.arange(3)
    xdata = np.array([[[1, 2, 3], [4, 5, 6]]])
    ydata = np.array([[[1, 2, 3]], [[4, 5, 6]]])
    x = pf.FrequencyData(xdata, freqs)
    y = pf.FrequencyData(ydata, freqs)
    z = x @ y
    desired = np.array([[[17, 29, 45]]])
    npt.assert_allclose(z.freq, desired, atol=1e-15)
    assert isinstance(z, pf.FrequencyData)


def test_matrix_multiplication_signal_times_array():
    """Test multiplication of signal with array."""
    x = pf.signals.impulse(10, amplitude=np.array([[1, 2, 3], [4, 5, 6]]))
    y = np.ones((3, 2)) * np.array([[1, 2], [3, 4], [5, 6]])
    z = x @ y
    desired = np.array([[22, 28], [49, 64]])[..., None] * np.ones((2, 2, 6))
    npt.assert_allclose(z.freq, desired, atol=1e-15)
    z = y @ x
    desired = np.array([[9, 12, 15], [19, 26, 33], [29, 40, 51]])[..., None] \
        * np.ones((3, 3, 6))
    npt.assert_allclose(z.freq, desired, atol=1e-15)


def test_matrix_multiplication_TimeData_times_array():
    """Test multiplication of TimeData with array."""
    times = np.arange(10)
    xdata = np.ones((2, 3, 10)) * np.array([[1, 2, 3], [4, 5, 6]])[..., None]
    x = pf.TimeData(xdata, times)
    y = np.ones((3, 2)) * np.array([[1, 2], [3, 4], [5, 6]])
    z = x @ y
    desired = np.array([[22, 28], [49, 64]])[..., None] * np.ones((2, 2, 10))
    npt.assert_allclose(z.time, desired, atol=1e-15)
    z = y @ x
    desired = np.array([[9, 12, 15], [19, 26, 33], [29, 40, 51]])[..., None] \
        * np.ones((3, 3, 10))
    npt.assert_allclose(z.time, desired, atol=1e-15)


def test_matrix_multiplication_FrequencyData_times_array():
    """Test multiplication of FrequencyData with array."""
    times = np.arange(10)
    xdata = np.ones((2, 3, 10)) * np.array([[1, 2, 3], [4, 5, 6]])[..., None]
    x = pf.FrequencyData(xdata, times)
    y = np.ones((3, 2)) * np.array([[1, 2], [3, 4], [5, 6]])
    z = x @ y
    desired = np.array([[22, 28], [49, 64]])[..., None] * np.ones((2, 2, 10))
    npt.assert_allclose(z.freq, desired, atol=1e-15)
    z = y @ x
    desired = np.array([[9, 12, 15], [19, 26, 33], [29, 40, 51]])[..., None] \
        * np.ones((3, 3, 10))
    npt.assert_allclose(z.freq, desired, atol=1e-15)


def test_matrix_multiplication_axes():
    """Test axes parameter."""
    a = np.arange(2 * 3 * 5).reshape((2, 3, 5))
    b = np.arange(3 * 4 * 5).reshape((3, 4, 5))
    x = pf.signals.impulse(10, amplitude=a)
    y = pf.signals.impulse(10, amplitude=b)
    z = pf.matrix_multiplication((x, y), axes=[(0, 1), (0, 1), (0, 1)])
    des = np.matmul(a, b, axes=[(0, 1), (0, 1), (0, 1)])[..., None] \
        * np.ones((2, 4, 5, 6))
    npt.assert_allclose(z.freq, des, atol=1e-15)


@pytest.mark.parametrize(('sx', 'sy', 'az', 'sz'),
                         [((1, 3, 5), (3, 5, 4), 5, (3, 3, 4)),
                          ((2,), (3, 2, 4), 2, (3, 1, 4)),
                          ((1, 2), (3, 2, 4), 2, (3, 1, 4)),
                          ((2, 3, 4), (4,), 4, (2, 3, 1)),
                          ((2, 3, 4), (4, 1), 4, (2, 3, 1))])
def test_matrix_multiplication_broadcasting(sx, sy, az, sz):
    """Test broadcasting."""
    x = pf.signals.impulse(10, amplitude=np.ones(sx))
    y = pf.signals.impulse(10, amplitude=np.ones(sy))
    z = pf.matrix_multiplication((x, y))
    des = az * np.ones(sz + (6,))
    npt.assert_allclose(z.freq, des, atol=1e-15)


def test_matrix_multiplication_multiple():
    """Test 3 arguments in data."""
    a = np.ones((2, 3))
    b = np.ones((3, 4))
    c = np.ones((4, 5))
    x = pf.signals.impulse(10, amplitude=a)
    y = pf.signals.impulse(10, amplitude=b)
    z = pf.signals.impulse(10, amplitude=c)
    res = pf.matrix_multiplication((x, y, z))
    des = 12 * np.ones((2, 5, 6))
    npt.assert_allclose(res.freq, des, atol=1e-15)


@pytest.mark.parametrize(
    'x', [np.ones((2, 3)), pf.signals.impulse(10, amplitude=np.ones((2, 3)))])
@pytest.mark.parametrize(
    'y', [np.ones((3, 4)), pf.signals.impulse(10, amplitude=np.ones((3, 4)))])
@pytest.mark.parametrize(
    'z', [np.ones((4, 5)), pf.signals.impulse(10, amplitude=np.ones((4, 5)))])
def test_matrix_multiplication_multiple_arrays(x, y, z):
    """Test 2 arrays in 3 arguments."""
    if any(type(a) in (Signal, TimeData, FrequencyData) for a in [x, y, z]):
        des = 12 * np.ones((2, 5, 6))
        npt.assert_allclose(
            pf.matrix_multiplication((x, y, z)).freq, des, atol=1e-15)
    else:
        des = 12 * np.ones((2, 5))
        npt.assert_allclose(
            pf.matrix_multiplication((x, y, z)), des, atol=1e-15)


def test_matrix_multiplication_array_mismatch_errors():
    """Test errors for multiplication of signal with array."""
    x = pf.signals.impulse(10, amplitude=np.array([[1, 2, 3], [4, 5, 6]]))
    y = np.ones((3, 2, 1)) * np.array([[1, 2], [3, 4], [5, 6]])[..., None]
    with pytest.raises(ValueError, match='matmul'):
        x @ y
    with pytest.raises(ValueError, match='matmul'):
        y @ x


def test_matrix_multiplication_undocumented():
    """Test undesired, but not restricted multiplication along time axis."""
    x = pf.signals.impulse(10, amplitude=np.array([[1, 2, 3], [4, 5, 6]]))
    y = np.ones((3, 2, 10)) * np.array([[1, 2], [3, 4], [5, 6]])[..., None]
    pf.matrix_multiplication(
        (x, y), domain='time', axes=[(-2, -1), (-3, -2), (-2, -1)])


@pytest.mark.parametrize('audio_object', [
    pf.Signal([1, -1, 1], 1, fft_norm='none'),
    pf.Signal([1, -1, 1], 1, fft_norm='rms'),
    pf.FrequencyData([1, -1, 1], [0, 1, 3]),
    pf.TimeData([1, -1, 1], [1, 2, 3])])
@pytest.mark.parametrize('operation', [
    pf.add, pf.subtract, pf.multiply, pf.divide, pf.power])
def test_audio_object_and_number(audio_object, operation):
    """
    Test if arithmetic operations work regardless of the fft norm and
    audio object type if only one audio object is involved.
    """

    domain = 'time' if type(audio_object) is pf.TimeData else 'freq'

    result = operation((1, audio_object), domain=domain)
    assert type(result) is type(audio_object)

    result = operation((audio_object, 1), domain=domain)
    assert type(result) is type(audio_object)
