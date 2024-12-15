import pytest
import numpy as np
import pyfar as pf
import numpy.testing as npt


@pytest.mark.parametrize((
        "temperature", "frequency", "relative_humidity", "expected"), [
    (10, 1000, .1, 2.16e1*1e-3),
    (10, 100, .1, 5.85e-1*1e-3),
])
def test_air_attenuation_iso(
        temperature, frequency, relative_humidity, expected):
    temperature = 10
    air_attenuation, accuracy = pf.constants.air_attenuation_iso(
        temperature, frequency, relative_humidity, calculate_accuracy=True)
    npt.assert_allclose(air_attenuation, expected, atol=1e-3)
    npt.assert_allclose(accuracy, 10)


@pytest.mark.parametrize("temperature", [
        np.array([10, 10]),
        [10, 10],
        10,
])
@pytest.mark.parametrize("frequency", [
        np.array([1000, 1000]),
        [1000, 1000],
        1000,
])
@pytest.mark.parametrize("relative_humidity", [
        np.array([.1, .1]),
        [.1, .1],
        .1,
])
def test_air_attenuation_iso_array(temperature, frequency, relative_humidity):
    result = pf.constants.air_attenuation_iso(
        temperature, frequency, relative_humidity)
    expected = 2.16e1*1e-3 + np.zeros_like(result)
    npt.assert_allclose(result, expected, atol=1e-3)


def test_air_attenuation_iso_inputs():
    temperature = 10
    frequency = 1000
    relative_humidity = .1
    with pytest.raises(TypeError, match='must be a number or'):
        pf.constants.air_attenuation_iso(
            'test', frequency, relative_humidity, calculate_accuracy=True)
    with pytest.raises(TypeError, match='must be a number or'):
        pf.constants.air_attenuation_iso(
            temperature, 'frequency', relative_humidity,
            calculate_accuracy=True)
    with pytest.raises(TypeError, match='must be a number or'):
        pf.constants.air_attenuation_iso(
            temperature, frequency, 'relative_humidity',
            calculate_accuracy=True)
    with pytest.raises(TypeError, match='must be a bool'):
        pf.constants.air_attenuation_iso(
            temperature, frequency, relative_humidity, calculate_accuracy=5)
