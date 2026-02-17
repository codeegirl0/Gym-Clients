Gym Clients Data Analysis

This project is designed to analyze gym member behaviors using various statistical analysis techniques. 

📊 Analysis Types

The project performs three levels of data exploration:

•	Univariate Analysis: Examining individual variables .

•	Bivariate Analysis: Exploring relationships between two variables .

•	Multivariate Analysis: Analyzing interactions between multiple data points to find deeper behavioral correlations.

________________________________________
🛠️ How It Works

The analysis follows a structured three-step pipeline:

1. Data Preprocessing :
Before analysis, the initial CSV file passes through:

•	De-duplication: Identifying and removing duplicate client records.

•	Data Imputation: Filling missing values.

•	Text Correction: Fixing typing errors and inconsistent formatting.

•	Normalization: Handling aberrant data.

2. Data Integration :
The system performs a relational join between the Clients dataset and the Coach table.

3. Behavior Analysis & Visualization
The final step generates charts that visualize client trends.

________________________________________
🚀 Usage

The entire workflow is automated. You can run the preprocessing, joining, and analysis with a single command:

python process.py

Output: Upon completion, the script will generate 5 distinct charts visualizing key client behaviors.

________________________________________
💻 Technologies Used :

•	Python: Core logic and scripting.

•	Pandas: Data manipulation and cleaning.

•	Seaborn: Statistical data visualization.

•	Matplotlib: Low-level graph customization.

________________________________________
📂 Project Structure:

•	process.py: The main entry point for the application.

•	data/: Folder containing CSV files.

•	scripts/: Modules for cleaning, joining and analysis.



Happy analyzing!

