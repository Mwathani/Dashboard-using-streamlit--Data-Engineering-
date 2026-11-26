# Streamlit Data Engineering Dashboard

A hands-on Streamlit project demonstrating how to display, style, and visualize data using Python. The project includes a pandas-based table example and an interactive sales dashboard built from an Excel dataset.

## Live Demo

[![Open the live dashboard](https://img.shields.io/badge/Streamlit-Open%20Live%20Dashboard-FF4B4B?logo=streamlit&logoColor=white)](https://sales-region-dashboard.streamlit.app/)

**Live application:** [sales-region-dashboard.streamlit.app](https://sales-region-dashboard.streamlit.app/)

## Overview

This repository explores common data engineering and data visualization workflows:

- Loading tabular data with pandas
- Reading Excel files with openpyxl
- Displaying dataframes and tables in Streamlit
- Visualizing product sales by region
- Creating line, bar, scatter, and area charts
- Calculating key sales metrics
- Caching data to improve application performance

## Features

- **Data display** — Render tabular data in Streamlit
- **Line charts** — Compare total sales over time by region
- **Bar charts** — Summarize sales by region
- **Scatter plots** — Explore the relationship between unit price and quantity
- **Area charts** — Visualize sales trends
- **KPIs** — Display total revenue as a dashboard metric
- **Excel integration** — Load regional product sales data directly from an `.xlsx` file
- **Cached loading** — Prevent unnecessary reloading of the source dataset

## Project Structure

```text
.
├── 01_Display_&_Style_Data.py
├── README.md
├── requirements.txt
└── Data_Visualization/
    ├── 01_Line_Chart.py
    ├── Dashboard.py
    ├── Product-Sales-Region.xlsx
    └── requirements.txt
```

## Technology Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly Express](https://plotly.com/python/plotly-express/)
- [Altair](https://altair-viz.github.io/)
- [OpenPyXL](https://openpyxl.readthedocs.io/)
- [Excel](https://www.microsoft.com/microsoft-365/excel)

## Getting Started

### Prerequisites

- Python 3.10 or later
- pip

### Installation

Clone the repository:

```bash
git clone https://github.com/Mwathani/Dashboard-using-streamlit--Data-Engineering-.git
cd Dashboard-using-streamlit--Data-Engineering-
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

For the visualization application, you can install the dedicated dependencies:

```bash
pip install -r Data_Visualization/requirements.txt
```

## Running the Project

### Display and style data

From the repository root:

```bash
streamlit run "01_Display_&_Style_Data.py"
```

### Run the sales visualization application

```bash
streamlit run Data_Visualization/01_Line_Chart.py
```

Streamlit will normally open the application at:

```text
http://localhost:8501
```

## Dashboard Overview

The sales dashboard reads `Product-Sales-Region.xlsx`, calculates the total revenue, and presents the data using multiple visualizations:

- Total sales over time
- Sales distribution by region
- Unit price compared with quantity
- Cumulative sales-area visualization
- Filterable and scrollable data tables

## Data Handling

The visualization script loads data using `st.cache_data`, which improves performance by caching the dataframe after the Excel file has been processed.

```python
@st.cache_data
def load_data():
    script_dir = Path(__file__).parent
    file_path = script_dir / "Product-Sales-Region.xlsx"
    return pd.read_excel(file_path)
```

The `OrderDate` column is converted to a datetime type before creating time-based charts:

```python
chart_data["OrderDate"] = pd.to_datetime(chart_data["OrderDate"])
```

## Future Improvements

- Add sidebar filters for region, product, and date range
- Convert the project into a complete multi-page Streamlit application
- Add data validation and error handling
- Connect the dashboard to a database or cloud data source
- Introduce automated tests
- Add an example `.env` configuration
- Add screenshots or a demo GIF
- Add a license

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add a new feature"
   ```

4. Push the branch:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a pull request

## Author

**Mwathani**

- GitHub: [@Mwathani](https://github.com/Mwathani)
