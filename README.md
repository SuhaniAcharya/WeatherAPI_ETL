Project Overview:
This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline for weather data. The pipeline extracts data from the OpenWeatherMap API, transforms and cleans it using Python and Pandas, and loads it into a PostgreSQL database for analysis. Visualizations are also generated to provide insights into hourly temperature patterns. This project showcases skills in ETL, data cleaning, API integration, database management, and data visualization, all of which are key for real-world data engineering workflows.

Technologies Used:
1. Python – Main programming language
2. Pandas – Data transformation and analysis
3. Requests – Fetching data from APIs
4. PostgreSQL – Relational database for storing processed data
5. SQLAlchemy – Database connection and table creation
6. Matplotlib & Seaborn – Visualization and heatmaps
7. Jupyter Notebook / VS Code – Development environment

Project Workflow:
1. Extract: Fetch weather data from OpenWeatherMap API using Python’s requests library. Hourly forecast for a specific city (configurable).

2. Transform: Parse JSON response and convert to a Pandas DataFrame. Handle missing data for rain/snow and other parameters. Convert timestamps to datetime objects for analysis.  Create pivot tables for day/hour heatmaps.

3. Load: Connect to a PostgreSQL database using SQLAlchemy. Load transformed data into the weather_data table. Supports replace or append modes for database updates.
  
5. Visualize: Line plots showing temperature trends over time. Heatmaps representing hourly temperature variations by day.

Future Improvements:
1. Schedule the ETL pipeline using cron jobs or Apache Airflow.
2. Store historical data for trend analysis over weeks/months.
3. Deploy on cloud platforms (AWS RDS / BigQuery) for large-scale data.

Screenshots:

<img width="1919" height="1019" alt="Screenshot 2025-08-15 175634" src="https://github.com/user-attachments/assets/b4b40741-eb4e-4869-9890-ab8c38b7883c" />
<img width="1913" height="1031" alt="Screenshot 2025-08-15 175701" src="https://github.com/user-attachments/assets/97e56de3-eadf-4282-b97e-4feab6e22778" />
