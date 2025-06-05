# Ground Temperature Analysis (1960-2024)

In this project I analyzed the evolution of ground temperature between 1960 and 2024, using data from meteorological sites around the world. It uses Python for data processing, visualization, and statistical analysis to understand temperature trendsin these ~64 years of data. 

---

## Features

- Extracts and processes temperature data from meteorological sites.
- Identifies relevant sites within a given geographical region using bounding boxes.
- Visualizes the data on an interactive map using **Folium**.
- Filters and analyzes temperature data for trends, including linear regression.
- Uses bootstrap methods to estimate confidence intervals for regression parameters.
- Visualizes results, including temperature trends and bootstrap distributions.

---

## Dependencies

This project requires the following Python libraries:

- `numpy`
- `pandas`
- `matplotlib`
- `plotly`
- `folium`
- `geopy`
- `scipy`
- `IPython`
- Custom module: `get_coords` (for retrieving city coordinates)
- Custom module: `bootstrap_err` (for bootstrap analysis on the rate of temperature change: degrees/yr)

Install dependencies using:

```bash
pip install numpy pandas matplotlib plotly folium geopy scipy ipython
```

---

## Usage

1. Clone the repository and navigate to the project directory.

2. Ensure the input data files are available in the specified paths (you can download them usin the Google Drive Link):

   - Site metadata file: `ghcnm.tavg.v4.0.1.20250108.qcf.inv`
   - Temperature data file: `ghcnm.tavg.v4.0.1.20250108.qcf.dat`

3. Run the main script:

```bash
python temperature_analysis.py
```

4. Specify the target city for analysis by updating the `city_name` variable in the script.

---

## Data Workflow

1. **Data Loading**:
   - Load site metadata and temperature data from files.
   - Extract and filter data based on the specified region and time range (1960-2024).

2. **Visualization**:
   - Display the region of interest and meteorological sites on a map.
   - Plot temperature trends and statistical summaries.

3. **Statistical Analysis**:
   - Perform linear regression to determine temperature trends.
   - Use bootstrap methods to estimate errors and confidence intervals.

---

## Results

- The total temperature increase (1960-2024) and the rate of increase per year are calculated and displayed.
- Plots include:
  - Temperature trends with linear regression and confidence intervals.
  - Bootstrap distribution of the regression slope.

---

## Example Output

**Map Visualization**:
- Displays the center of the selected region, bounding box, and meteorological sites.

**Temperature Trend Analysis**:
- Example for a city (e.g., Canberra):
  
  - **Total Increase in Temperature (1960-2024):** ~1.5°C ± 0.1°C
  - **Rate of Increase in Temperature (per year):** ~0.02°C/year
  

---

## Acknowledgments

- **National Centers for Environmental Information (NCEI)**: For providing the raw temperature data.
- Python libraries and contributors for enabling seamless data analysis.

For more details, check out the source code and accompanying comments.
