# QGIS NDVI Calculator

A QGIS Python plugin for calculating the Normalized Difference Vegetation Index (NDVI) from satellite imagery.

## Overview

NDVI Calculator helps users calculate NDVI from raster bands in a QGIS project and save the result as a GeoTIFF raster.

The plugin was developed as a learning project to explore Python development, PyQGIS, raster processing, and remote sensing.

## Features

- Select Red and Near-Infrared (NIR) raster layers from the current QGIS project.
- Calculate NDVI using the QGIS Raster Calculator API.
- Apply Landsat Collection 2 Level-2 Surface Reflectance scaling.
- Save the output as a GeoTIFF file.
- Automatically add the resulting raster layer to the current QGIS project.

## NDVI Formula

The Normalized Difference Vegetation Index is calculated as:

\[
NDVI = \frac{NIR - Red}{NIR + Red}
\]

For Landsat 9 Collection 2 Level-2 Surface Reflectance data, the reflectance scaling is:

\[
SR = DN \times 0.0000275 - 0.2
\]

The plugin applies this scaling to the selected Red and NIR bands before calculating NDVI.

## Supported Data

The plugin has been tested with Landsat 9 Surface Reflectance data:

- **Red:** Band 4 (`SR_B4`)
- **Near-Infrared:** Band 5 (`SR_B5`)

Other raster datasets may work if their bands are compatible. The selected rasters should have matching spatial coverage, resolution, and georeferencing.

## Requirements

- QGIS 3.44
- Landsat 9 Surface Reflectance raster bands or compatible raster data

## Installation

1. Download or clone this repository.
2. Copy the `ndvi_calculator` plugin folder into your QGIS Python plugins directory.
3. Restart QGIS if necessary.
4. Open **Plugins → Manage and Install Plugins**.
5. Enable **NDVI Calculator**.
6. Load the Red and NIR raster bands into your QGIS project.
7. Open the plugin, select the appropriate bands, and click **Calculate NDVI**.
8. Choose the output location for the GeoTIFF file.

## Limitations

- Cloud and cloud-shadow masking is not implemented yet.
- The input rasters should have compatible spatial characteristics.
- Additional validation for NoData values and zero denominators is planned.

## Technologies

- Python
- PyQGIS
- QGIS Raster Calculator API
- Raster data processing
- Landsat 9 Surface Reflectance

## Future Improvements

- Automatic NDVI color rendering.
- Cloud and cloud-shadow masking.
- Input raster compatibility checks.
- Improved error handling and progress feedback.
- Additional testing and documentation.

## Author

Developed by RustyPuppy10