import pytest
from render import sky_atmosphere as mod

CASES = [
    ("density0", 'm.density_at(0, 8) == approx(1.0)'),
    ("density1", 'm.density_at(8, 8) == approx(0.367879441, rel=1e-5)'),
    ("rayleigh", 'm.rayleigh_coeff(500) == approx(1.0 / (500 ** 4))'),
    ("mie", 'm.mie_phase(1.0, 0.0) == approx(1.0 / (4 * 3.141592653589793))'),
    ("trans", 'm.transmittance(0) == approx(1.0)'),
    ("sun", 'm.sun_angular_radius(1, 1) == approx(1.5707963267948966)'),
    ("horizon", 'm.horizon_blend(50, 100) == approx(0.5)'),
    ("shadow", 'm.planet_shadow(-1) is True'),
    ("cloud", 'm.cloud_shadow(0.5, 1.0) == approx(0.5)'),
    ("exposure", 'm.exposure_scale(1) == approx(2.0)'),
    ("medium", 'm.medium_switch(True, False) == "water"'),
    ("sync", 'm.lut_sync(1, 1) is True'),
    ("weather", 'm.weather_coeff(0.5, 2.0) == approx(3.0)'),
    ("airmass", 'm.airmass(1.0) == approx(1.0)'),
    ("scatter", 'm.multiple_scatter(2, 3) == approx(6)')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
