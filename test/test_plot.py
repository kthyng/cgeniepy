from cgeniepy.array import GriddedData
import numpy as np
import xarray as xr
import cartopy.crs as ccrs
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt


def create_testdata():
    lat = np.linspace(-89.5,89.5,180)
    lon = np.linspace(0,359,360)
    np.random.seed(12349)
    data = np.random.rand(lat.size,lon.size)
    xdata = xr.DataArray(data, coords=[('lat',lat),('lon',lon)],
                         attrs={'long_name':'random data', 'units':'uniteless'})   
    return GriddedData(xdata,False, attrs=xdata.attrs)

@image_comparison(baseline_images=['test_line'], remove_text=True,
                  extensions=['png'], style='mpl20')
def test_map():
    data = create_testdata()
    fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})
    data.plot(ax=ax)
    return fig

def test_line():
    data = create_testdata()
    fig, ax = plt.subplots()
    data.mean(dim='lon').plot(ax=ax)
    return fig