# Calorie-Tracking-Application
Task: Calorie Tracking app
Tech Stack:
<br>
Backend: Used Flask to handle HTTP requests made by clients and to handle other data manipulation tasks. Various routes were created to handle requests.
<br>
Frontend:
HTML: Used HTML to create forms and other tags and tailwind css was used for styling.
<br>

Database: Postgresql was used for storing data (as a database)
Used psycopg2 library to connect to database and to manipulate the data.
<br>

Visualization: Used matplot library to visualize the data and create charts like bar plot, line plot and to generate and save charts, subplots in image and pdf format
<br>

Large Language Model: Used Open AI’s GPT 3-5 model for an additional feature of recommendations based on data

Intiial Login Page:
If a user already has an account they can just login, if he/she doesn’t have one they can register
 ![image](https://github.com/Kushal1306/Calorie-Tracking-Application/assets/95643826/a8bfcc87-99ba-479f-bb1e-1f648921e6b6)


ii) After Logging in:
A user can update their calorie intake by filling up details like calorie amount, meal_type and date
And recently updated data also can been seen on the page.
A view reports and summary page button is also available to view visualizations
![image](https://github.com/Kushal1306/Calorie-Tracking-Application/assets/95643826/21a296c7-b462-4858-acdf-b778fd5e536f)

 
One can export their data in CSV format upon clicking the download data button
Once a user clicks view summary and reports button he would be redirected to below page where he can choose report of type daily, weekly and monthly and he can also choose type of chart he wants (either bar chart or line plot)
Daily report shows the visulaization of daily calorie intake of the last 7 days
Weekly report shows the average weekly calorie intake
Monthly report shows the visualization of average monthly intake
![image](https://github.com/Kushal1306/Calorie-Tracking-Application/assets/95643826/6c24f9c9-dd5e-48ba-93ad-2a548aa83eca)

 
Below is daily report generated in bar chart format
 ![image](https://github.com/Kushal1306/Calorie-Tracking-Application/assets/95643826/775ce33f-aa82-43f3-b649-765edd40210a)


The below is weekly report generated in line plot format
![image](https://github.com/Kushal1306/Calorie-Tracking-Application/assets/95643826/c7e33b54-b4b8-4ac2-ad0e-6987c517d2ea)

 




A user can also download the charts in PDF OR PNG format by choosing type of chart and file format they want.
![image](https://github.com/Kushal1306/Calorie-Tracking-Application/assets/95643826/2b3392fc-1e7d-415f-aa84-2cb33dbd7d9a)

 
The below is the snapshot of pdf generated:
![image](https://github.com/Kushal1306/Calorie-Tracking-Application/assets/95643826/2c951c2c-6e59-4119-856c-c57b89f0cc2f)

 
The below is the image exported in png format:
![image](https://github.com/Kushal1306/Calorie-Tracking-Application/assets/95643826/933486c4-f359-4012-9122-de5073638827)

 
Additonal Feature: Once can generate personalised recommendations based on the data. This feature is powered by Open AI’s GPT 3.5
![image](https://github.com/Kushal1306/Calorie-Tracking-Application/assets/95643826/fba500a5-e238-4381-b15c-ab635f00b6ca)

 
The below is snapshot attached of personalized recommendations based on data (Generated by GPT 3.5)
![image](https://github.com/Kushal1306/Calorie-Tracking-Application/assets/95643826/1150adef-bfb5-4575-9ffd-d6d5594b1b2a)

 
