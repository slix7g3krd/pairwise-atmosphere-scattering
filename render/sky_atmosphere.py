"""第 63 批：从海边一路开到山顶，天空从蓝变灰再变黑，太阳落山时地平线出现一条..."""

import math


def density_at(altitude, scale_height):
    """海拔密度：随海拔指数衰减，不再钳到同一值。"""
    return math.exp(-altitude / scale_height)


def rayleigh_coeff(wavelength):
    """瑞利系数：与波长四次方成反比。"""
    return 1.0 / (wavelength ** 4)


def mie_phase(cos_theta, g):
    """米氏相位：Henyey-Greenstein，g=0 时退化为各向同性 1/(4π)。"""
    denom = (1.0 + g * g - 2.0 * g * cos_theta) ** 1.5
    return (1.0 - g * g) / (4.0 * math.pi * denom)


def transmittance(optical_depth):
    """透射率：exp(-τ)。"""
    return math.exp(-optical_depth)


def sun_angular_radius(radius, distance):
    """太阳盘角半径：asin(r/d)，与天空 LUT 共用同一几何。"""
    return math.asin(radius / distance)


def horizon_blend(altitude, max_altitude):
    """地平线混合：按海拔线性归一。"""
    return altitude / max_altitude


def planet_shadow(sun_direction_y):
    """行星阴影：太阳在地平线以下即处于阴影。"""
    return sun_direction_y < 0


def cloud_shadow(cloud, ground):
    """云影注入：云覆盖率乘地面光照，参与大气积分。"""
    return cloud * ground


def exposure_scale(ev):
    """曝光唯一：单一 2^EV 缩放，HDR 与补偿不重复计算。"""
    return 2.0 ** ev


def medium_switch(underwater, space):
    """介质切换：水下 / 太空 / 空气。"""
    if underwater:
        return "water"
    if space:
        return "space"
    return "air"


def lut_sync(cpu_version, gpu_version):
    """LUT 同步：CPU 与 GPU 版本一致才算同步。"""
    return cpu_version == gpu_version


def weather_coeff(rain, base):
    """天气系数：换预设时散射系数随降水缩放。"""
    return base * (1.0 + rain)


def airmass(cos_zenith):
    """大气质量：1/cos(天顶角)。"""
    return 1.0 / cos_zenith


def multiple_scatter(optical_depth, coeff):
    """多次散射：系数随光学深度缩放，不再固定。"""
    return optical_depth * coeff


def sun_disk_visible(sun_y, horizon_y):
    """日月盘一致：太阳中心不低于地平线即可见。"""
    return sun_y >= horizon_y
