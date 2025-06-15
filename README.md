# WagonR_Datascraping
## Sequence of execution 
### 1. Execute <base.py>
This file extracts 40 pages from olx website for wagon r databse.
Packages used are :
- requests
- datetime
- pickle
- numpy
### 2.Execute <Processing.py> 
Note:
1. Replace path of tab_dict with correct relative path of .pkl file generated in step1
2. This file cleans data and by using groupby consolidated table .csv is generated.

### 3. How to use .csv table to estimate resale value
1. Open .csv file in excel
2. Apply auto filters. Refer following link. [https://support.microsoft.com/en-us/office/use-autofilter-to-filter-your-data-7d87d63e-ebd0-424b-8106-e2ab61133d92].In case you dont find your make year choose nearest one.
3. From fileters filter out your make year from first column. In case you dont find your make year, choose nearest one.
4. Filter out your variant. Choose nearest one in case you dont find any.
5. Filter out your fueltype from fuel column.
6. Filter out your car's Km driven by choosing nearest value.
7. Now mean column will give you mean price for selected filters.  

