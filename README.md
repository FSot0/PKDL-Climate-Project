# PKDL-Climate-Project
Climate project automation using PKDL A1 climate data logger

<p align="center">
   <img src="https://github.com/FSot0/PKDL-Climate-Project/blob/main/images/PKDLA1.jpg" width="300" height="300">
</p>

- Setting Up the Climate Data Logger:

    - The device measures temperature (in °C) and humidity (%) every 5 minutes, exporting the data in a CSV file.
    - You will need to configure the date and frequency using the LIDL software, you can find it in 

- Data Cleaning and Preparation:

    - We loaded and cleaned the CSV file for processing in Python, including formatting dates, cleaning columns, and normalizing data.
    
- Generating Graphs:

    - We created daily and monthly trend graphs for temperature and humidity using matplotlib.
    
- Deploying the Dashboard on Streamlit Cloud:
    
    - We uploaded all necessary files to the GitHub repository.
    - Configured pekadele.py to read data from the GitHub CSV file, allowing data access without manual uploads.
