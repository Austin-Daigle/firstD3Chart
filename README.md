# Washington Post Police Shootings (2015-2017) analysis using D3.Js 
This repo contain the raw Washington Post dataset, cleaned data set, automated Python cleaning script, and chart(s) from the analytics.

The primary dataset for this project can be found [here](https://github.com/washingtonpost/data-police-shootings/tree/master/v1).
The webpage with the compiled plolty d3.js charts can be found [here](https://d3demopage.wixsite.com/fatal-police-shootin)

**All of the compiled data and d3.js graphs can be found on this demonstration [website](https://d3demopage.wixsite.com/fatal-police-shootin)**

**Washing Post Police Shooting Cleaning Script Instructions**
--> Download the v.1 Dataset from either the source [Github repo](https://github.com/washingtonpost/data-police-shootings/tree/master/v1) or the [project directory](https://github.com/Austin-Daigle/firstD3Chart/blob/main/fatal-police-shootings-data.csv)

--> Use the Python script to select the correct dataset from the filechooser and allow the script to return a cleaned dataset (you may need to adjust or code the cleaning rules if you have not already taken care of that). 

--> Create an account (if you don't have one already) for [plotly chart studio](https://chart-studio.plotly.com/create/#/)

--> Import the cleaned dataset from the Python Script

--> Use Plotly's Studio to create a d3.js graph.

--> Save and Export graph as either raw code (JavaScript, HTML5, HTML refference element).

<br></br>
# [The counted Cleaning Script](https://github.com/Austin-Daigle/firstD3Chart/blob/main/The%20Counted%20Cleaning%20Script/The%20Counted%20Cleaning%20Script.py) (Look Here if you are using "the counted 2015" or "the counted 2016")



**Important Usage Notes:**

Before executing this Python script, be sure to get your "the counted 2015" and "the counted 2016" data properly prepared and converted before loading it into
the cleaning script. 

**Process to prepare the file:**

-> Take the .csv file and open it using Excel 
-> select the "File" tab in the ribbon 

-> select "Export" from the option side ribbon

-> select the "Change the file type" option

-> under the "Other files types options" select "Text (Tab delimited) (.txt)" 

    this is extreamly important since the tab delimited system is required to parse and process the data into the cleaning script.
-> the output from the Excel convertion will be a .txt file.

-> open and execute the python script and select the converted .txt file

-> the script will clean the input file and create a new file called "cleaned_data_set (alt-script).csv"

    keep in mind that if there is a .csv file called "cleaned_data_set (alt-script).csv", the python script will not overide it. 
    

*Remember to write your cleaning rules in the given script section*
