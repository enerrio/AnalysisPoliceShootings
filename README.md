# AnalysisPoliceShootings
Analysis of The Washington Post's Fatal Police Shootings database

The original data is published under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License](https://creativecommons.org/licenses/by-nc-sa/4.0/) and that license is included here as well.

The Washington Post has been collecting data about fatal police shootings since 2015 until present. The data is hosted [here](https://github.com/washingtonpost/data-police-shootings) on Github and is regularly updated. The purpose of this project is to explore that data and create interactive visualizations for anyone to use and interpret.

This project is split into 3 notebooks:

1. **DataPreparation.ipynb**: Load the dataset, take a initial look at the columns, print out basic info. Geocode cities/states into latitude/longitude coordinates. Create new columns that will make plotting easier.
2. **FindIncorrectCoord.ipynb**: Visualize geocoding errors.
3. **PoliceShootingsAnalysis.ipynb**: Main notebook that creates several visualizations of the data using plotly

There is also a `utils.py` file that contains code that geocodes cities, adds missing coordinates, fixes incorrect coordinates, and serializes data. In addition to this all the plots (except the map plots) are downloaded as png files and stored in the plots folder.

## Viewing Notebooks
Plotly plots don't render correctly when viewed in Github, so the best way to view the notebooks that use plotly is to view them on [nbviewer.jupyter.org](http://nbviewer.jupyter.org). Below are links to view the notebooks on that website.

**PoliceShootingsAnalysis.ipynb**: http://nbviewer.jupyter.org/github/enerrio/AnalysisPoliceShootings/blob/master/PoliceShootingsAnalysis.ipynb
**FindIncorrectCoord.ipynb**: http://nbviewer.jupyter.org/github/enerrio/AnalysisPoliceShootings/blob/master/FindIncorrectCoord.ipynb

## Dependencies
* numpy: 1.14.2
* pandas: 0.20.3
* plotly: 3.0.0
* notebook: 5.5.0
