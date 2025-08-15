Project Overview:
This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline for weather data. The pipeline extracts data from the OpenWeatherMap API, transforms and cleans it using Python and Pandas, and loads it into a PostgreSQL database for analysis. Visualizations are also generated to provide insights into hourly temperature patterns. This project showcases skills in ETL, data cleaning, API integration, database management, and data visualization, all of which are key for real-world data engineering workflows.

Technologies Used:
  Python – Main programming language
  Pandas – Data transformation and analysis
  Requests – Fetching data from APIs
  PostgreSQL – Relational database for storing processed data
  SQLAlchemy – Database connection and table creation
  Matplotlib & Seaborn – Visualization and heatmaps
  Jupyter Notebook / VS Code – Development environment

Project Workflow:
  1. Extract
    Fetch weather data from OpenWeatherMap API using Python’s requests library.
    Hourly forecast for a specific city (configurable).
  
  2. Transform
    Parse JSON response and convert to a Pandas DataFrame.
    Handle missing data for rain/snow and other parameters.
    Convert timestamps to datetime objects for analysis.
    Create pivot tables for day/hour heatmaps.
  
  3. Load
    Connect to a PostgreSQL database using SQLAlchemy.
    Load transformed data into the weather_data table.
    Supports replace or append modes for database updates.
  
  4. Visualize
    Line plots showing temperature trends over time.

    Heatmaps representing hourly temperature variations by day.

Future Improvements:
  Schedule the ETL pipeline using cron jobs or Apache Airflow.
  Store historical data for trend analysis over weeks/months.
  Deploy on cloud platforms (AWS RDS / BigQuery) for large-scale data.




