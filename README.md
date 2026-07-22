# 🌍 The Earth Kept a Record. Here It Is.

<div align="center">

### 80+ Years of Climate Change Through Interactive Visualizations

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)

### 📊 Making Climate Change Easier to Understand Through Interactive Data Visualization

<br>

<!-- Add Homepage Screenshot Here -->

</div>

---

# 📖 Overview

Climate change is one of the biggest challenges our planet faces, yet most people only experience it through headlines, scientific reports, or complex datasets. While the information is available, it is often difficult to explore, compare, and truly understand.

**The Earth Kept a Record. Here It Is.** transforms more than **80 years of historical climate data** into an interactive dashboard where users can explore how temperatures have changed across cities and countries through engaging visualizations.

Instead of simply presenting numbers, this project encourages exploration. Users can compare locations, discover long-term warming patterns, identify which regions have warmed the most, visualize decades through heatmaps, and even explore possible future temperature trends using machine learning.

The goal of this project is not only to visualize climate data but also to make climate change more accessible, understandable, and engaging for everyone.

---
---
# 🚀 Live Demo

You can explore the project here:

🌍 **The Earth Kept a Record. Here It Is.**

👉 https://your-streamlit-url.streamlit.app

No installation is required — simply open the link in your browser and start exploring.

---

# 🌡️ What is a Temperature Anomaly?

A **temperature anomaly** measures **how much warmer or cooler a location is compared to its long-term average temperature**, rather than showing the actual temperature itself.

For example:

- If the long-term average temperature of a city is **20°C**
- and this year the average temperature is **21.5°C**

then the temperature anomaly is:

**+1.5°C**

Likewise,

- If the average temperature becomes **18.8°C**

the anomaly becomes:

**−1.2°C**

Scientists prefer using temperature anomalies instead of actual temperatures because they make it much easier to compare climate changes between different locations around the world, regardless of whether those places are naturally hot or cold.

Throughout this project:

🟥 **Positive anomalies** indicate temperatures **warmer than the historical average.**

🟦 **Negative anomalies** indicate temperatures **cooler than the historical average.**

---

# ✨ Features

## 📈 Temperature Trends

Explore how temperatures have changed across more than **80 years** for both cities and countries.

- Interactive line graphs
- City mode
- Country mode
- Historical temperature visualization
- Long-term warming analysis

---

## 🌡️ Climate Comparison

Compare multiple cities or countries on the same graph.

- Compare up to 7 locations simultaneously
- Random comparison mode
- Observe warming differences
- Easily identify similar and different climate patterns

---

## 🏆 Heat Ranking

Discover which locations have experienced the greatest increase in temperature.

- Top warming cities
- Top warming countries
- Ranked bar charts
- Quickly identify climate hotspots

---

## 🗺️ Temperature Heatmap

Visualize decades of climate change through colour.

- Decade-wise averages
- Easy-to-read heatmaps
- Compare warming intensity
- Observe long-term climate patterns

---

## 🔮 Future Temperature Predictor

Explore how temperatures may continue changing in the future using machine learning.

Features include:

- Polynomial Regression prediction
- Historical + predicted trends
- Adjustable climate factors
- Educational future estimates
- Interactive prediction graph

---

# 🖥️ Dashboard Walkthrough


---

# 🏠 Homepage

<div align="center">

<!-- Insert Homepage Screenshot -->

</div>

The homepage serves as the central navigation hub of the application.

It introduces the project, displays key information about the dataset, and provides users with direct access to every visualization. Instead of overwhelming users with complex controls immediately, the homepage gives a quick overview of what can be explored and encourages interactive learning.

The homepage contains:

- 🌍 Project introduction
- 📅 80+ years of climate records
- 🌎 Climate visualization overview
- 🚀 Quick navigation to all five graphs
- 📂 Link to the GitHub repository

---

# 📈 Graph 1 — Temperature Trends

<div align="center">

<!-- Insert Graph 1 Screenshot -->

</div>

The **Temperature Trends** page allows users to explore how temperatures have changed over time for a single location.

Users can choose between:

- 🏙️ City Mode
- 🌍 Country Mode

After selecting a location, an interactive line graph displays its temperature history across more than **80 years**.

This visualization helps users:

- Observe long-term warming patterns.
- Identify years with unusually high or low temperatures.
- Compare historical climate changes within a single location.
- Understand how temperatures have evolved over decades.

---

# 🌡️ Graph 2 — Climate Comparison

<div align="center">

<!-- Insert Graph 2 Screenshot -->

</div>

The Climate Comparison graph allows users to compare several locations on the same graph.

Users may:

- Select up to **7 cities**
- Select up to **7 countries**
- Use the **Random Selection** button to automatically generate comparisons

Each location is displayed with its own coloured trend line, making it easy to compare warming rates over time.

This visualization allows users to:

- Compare different climates.
- Discover which locations warmed faster.
- Observe similarities between regions.
- Understand global warming from multiple perspectives.

---

# 🏆 Graph 3 — Heat Ranking

<div align="center">

<!-- Insert Graph 3 Screenshot -->

</div>

The Heat Ranking graph answers one simple question:

> **Which places have warmed the most?**

Instead of displaying the entire temperature history, this visualization calculates the total increase in temperature anomaly for every selected location and ranks them accordingly.

Users can switch between:

- 🌍 Countries
- 🏙️ Cities

The interactive bar chart makes it easy to:

- Identify the fastest warming locations.
- Compare total warming.
- Explore which regions have experienced the greatest climate change.

---

# 🗺️ Graph 4 — Temperature Heatmap

<div align="center">

<!-- Insert Graph 4 Screenshot -->

</div>

The Temperature Heatmap transforms decades of climate records into an easy-to-read colour map.

Instead of viewing individual years, temperatures are grouped into decades, making long-term climate patterns much easier to recognise.

Colours represent the average temperature anomaly during each decade.

The heatmap allows users to:

- Compare multiple locations simultaneously.
- Observe gradual warming over time.
- Quickly identify colder and warmer decades.
- Detect climate patterns using colour instead of numbers.

---

# 🔮 Graph 5 — Future Temperature Predictor

<div align="center">

<!-- Insert Graph 5 Screenshot -->

</div>

The Future Temperature Predictor is the most advanced part of the project.

Rather than only visualising historical climate data, this page estimates how temperatures may continue changing in the future using Machine Learning.

The graph combines:

- Historical temperature anomalies
- Predicted future anomalies
- Adjustable climate factors

Users can experiment with different future scenarios by changing several climate-related factors before generating predictions.

This encourages users to think about how human actions may influence future climate trends.

---

# 🤖 How the Prediction Works

Unlike many simple trend lines, this project uses **Polynomial Regression (Degree = 2)** to model temperature changes over time.

Historical climate records are first converted into polynomial features, allowing the model to capture gradual curves rather than assuming temperatures increase in a perfectly straight line.

The workflow follows these steps:

Historical Temperature Data

⬇️

Polynomial Feature Generation

⬇️

Polynomial Regression Model

⬇️

Future Temperature Prediction

The predicted values are then displayed alongside the historical observations, allowing users to compare the past with the estimated future.

---

## 🌱 Climate Factors

To make predictions more interactive, the application includes adjustable climate factors.

These factors allow users to simulate different future scenarios rather than viewing only one fixed prediction.

### 🌿 Positive Contributing Factors

Positive factors represent actions that may help reduce future warming.

Examples include:

- Increased afforestation
- Better environmental policies
- Greater use of renewable energy
- Reduced carbon emissions

Increasing these values reduces the projected warming trend.

---

### 🏭 Negative Contributing Factors

Negative factors represent activities that may increase future warming.

Examples include:

- Deforestation
- Industrial emissions
- Increased fossil fuel usage
- Higher greenhouse gas emissions

Increasing these values raises the projected warming trend.

---

## ⚠️ Educational Disclaimer

The prediction model is designed **for educational and visualization purposes only.**

Although Polynomial Regression is capable of identifying long-term historical patterns, it does **not** replace scientific climate models developed by climate researchers.

The predictions should therefore be interpreted as estimates that demonstrate how historical trends can be explored using machine learning rather than official climate forecasts.


# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Core programming language |
| 📊 Pandas | Data loading, cleaning, and preprocessing |
| 🎨 Streamlit | Interactive web application |
| 📈 Plotly | Interactive visualizations |
| 🤖 Scikit-Learn | Machine learning prediction model |

---

# 📂 Dataset

The project combines historical climate records from both **cities** and **countries**.

### Cities

The dashboard currently contains climate records for cities including:

- Bangkok
- Beijing
- Berlin
- Cairo
- Delhi
- Dubai
- London
- Madrid
- Moscow
- Multan
- New York
- Nuuk
- Oslo
- Paris
- Rome
- Seoul
- Singapore
- Sydney
- Tokyo
- Toronto

Each city dataset contains annual average temperatures spanning more than **80 years**.

---

### Countries

The project also includes temperature anomaly data for **200+ countries**, allowing users to compare climate change on a global scale.

Country data is represented using **temperature anomalies**, making comparisons between different climates more meaningful.

---

# 📁 Project Structure

```text
The-Earth-Kept-a-Record/
│
├── Homepage.py
│
├── pages/
│   ├── graph1.py
│   ├── graph2.py
│   ├── graph3.py
│   ├── graph4.py
│   └── graph5.py
│
├── Weather station csv/
│   ├── world_data.csv
│   ├── multan.csv
│   ├── london.csv
│   ├── ...
│
├── data_clean.py
├── requirements.txt
└── README.md
```

---

---

# 📸 Screenshots

## 🏠 Homepage

*![Homepage](assests/Homepage.png)*

---

## 📈 Temperature Trends

*![Tempeature Trends](assests/graph1.png)*

---

## 🌡️ Climate Comparison

*[Climate Comparison](assests/graph2.png)*

---

## 🏆 Heat Ranking

*[Heat Ranking](assests/graph3.png)*

---

## 🗺️ Temperature Heatmap

*[Tempeature Heatmap](assests/graph4.png)*

---

## 🔮 Future Temperature Predictor

*[Future Tempeature Predictor](assests/graph5.png)*

---

# Why I Built This

Climate change is often presented as numbers hidden inside research papers and reports.

I wanted to create something that allows anyone to explore climate data interactively without requiring any scientific background.

Instead of simply reading statistics, users can:

- Explore real historical data.
- Compare countries and cities.
- Discover long-term warming patterns.
- Visualize climate change through interactive graphs.
- Experiment with future predictions using machine learning.

My goal was to make climate data **interesting, interactive, and easy to understand.**

---

# Future Improvements

Some features I would like to add in future versions include:

- Interactive world map
- Search any city worldwide
- Additional climate indicators (rainfall, humidity, CO₂)
- Mobile-friendly layout
- Download graphs as images
- More advanced machine learning models
- Live climate data integration through APIs

---

# 👩‍💻 About the Developer

Hi! I'm **Shehma Ali** from Pakistan 🇵🇰.

I'm passionate about programming, problem solving, and building projects that combine creativity with technology.

Some of my experiences include:

- Harvard CS50P
- Stanford Code in Place 2026 (Experienced Student)
- NASA Stardance Participant
- Data Visualization Enthusiast

When I'm not coding, you'll probably find me watching movies, reading books, or learning something new.

---

# License

This project is intended for educational purposes.

Feel free to explore, learn from, and build upon it with proper attribution.

---

<div align="center">

## 🌍 The Earth kept a record...

### ...this project simply helps us read it.

If you enjoyed this project, consider giving it a star!

</div>