VBA code password: 123456
Open the userform by clicking the 'RunUO' button here at the quick access toolbar

![image](https://i.loli.net/2021/06/30/qhyuALHRXvkemfi.jpg)

This project is an assignment from Coursera see details below: 

This project has wide-ranging uses and applications.  Create a VBA user form that will: 
1) allow the user to add or delete new categories (user-defined) to a data table (these would be the columns/column headings) on a main worksheet, 
2) allow the user to add or delete records (a row of a table)
3) allow the user to look up different categories for a record (basically searching through the data and outputting a specific user-defined category) with the option of replacing those items.  
Please see the screencasts related to this project for help and a demonstration of what you are trying to create. 

Requirements
1)	Main Form.  The main form should have options to add a category, delete a category, add a new record (row of a table), delete record, and search through the data (by using one of the categories).  A delete confirmation box should appear to confirm deletion of any categories. 

Your main form might look something like this:

![image](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/vnN-ISmBEeiHZgqY3WPw8g_b981f11328a7c669bd64e542eadb2076_main-form.png?expiry=1625097600000&hmac=Xc52N2dS8NEVncmM9IpqvPb27879veFSViuBhDWbYFY)

2)	Add Category.  If the user wishes to create a new category, a user form similar to the one below should appear.  This allows the user to input the name of a new category.  This would be the heading of a column of data.  When the user selects “Add Category” then the next available (blank) column would be entitled what the user inputs.  As a simple example, some headings might be “Name”, “Phone Number”, and “Address”.

![image](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/2d9z3imBEeiISxJZ7npQ3g_0dcff447ce94d35eafc66ae4d802aa62_add-category.png?expiry=1625097600000&hmac=WdnsVXerfWRraXrp3XluhuLs9HUSOYU0GPIvrQvF0-8)

3)	Delete Category.  If the user wishes to delete an entire category (other than the Names category), a user form similar to the one below should appear.  All of the columns are populated in a combo box, with the default being the second column.  This allows the user to select the category that they wish to delete (i.e. an entire column of data from the spreadsheet).  This should be confirmed with a Yes/No message box after “Delete” is clicked!

 ![image](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/PwNTuimCEeiHZgqY3WPw8g_bd749b68ca5636f1d7894e30dc171897_delete-category.png?expiry=1625097600000&hmac=SR5qQjtjYHOgq2Y0P13q0m9vWX6-WGA7jigq7JaluJo)

4)	Add Record.  Next, we wish to be able to add records (rows of the table/spreadsheet).  A user form similar to the one below should allow the user to input a new record.  In the example below, I’ve assumed that the user has already created 3 categories (“Name”, “Phone”, and “Address”).  The user form should be able to display up to 12 different categories, so make sure there is extra space in case later on the user adds a new category.  Note that you should have 12 total labels and 12 total text boxes.  If there are currently n categories of data on the worksheet, then only n of the labels and n of the text boxes should be visible; all others should remain hidden.  See the screencasts on how to do this.  In the diagram below, the dotted lines represent that those labels and text boxes are hidden (i.e., not currently being used), but you should allow up to 12 total categories to be used on the spreadsheet.   

 ![image](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/aBYpGCmCEeiHZgqY3WPw8g_1f883238a214202d2bde22b1e723bc9e_new-record.png?expiry=1625097600000&hmac=MGA1FvQi180E5JE7o3KpE39o81fM2aSq2qkQBP_-9sw)

Again, there is a lot of space here such that if a new category is added then those new categories will show up.  When the user submits “Add Record”, the items in the user form are added in a single row of the spreadsheet. 

5)	Delete Record.  If the user wishes to delete an entire record (row of the spreadsheet, other than the first row), a user form similar to the one below should appear.  All of the names in column A will appear in a combo box.  This allows the user to select the record (name) that they wish to delete (i.e. an entire row of data from the spreadsheet).  This should be confirmed with a Yes/No message box after “Delete” is clicked!   

  ![image](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/lVFx7ymCEeiISxJZ7npQ3g_b1082f2745f94ec806ea251e2d5bb136_delete-record.png?expiry=1625097600000&hmac=uYHHK9bMK1uYeI9l5JHab2PLelOqTEcRPP0WgI7q7dI)

6)	Search/Replace.  The final aspect of the project is to allow the user to search through records for information and replace or add information.  The user should be able to select one of up to 12 categories (drop-down list) to use as a search criterion.  The user form will then display what the user is searching for and will also allow them to replace the information.  If the user selects to replace an item for a particular row and column, then the change will be permanently made to the worksheet.  If there is no available information for that item, then the user form will ask the user if they would like to add information to that record and category, and the addition should be made permanent on the worksheet (see my introduction screencast on what your project must do). 

  ![image](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/rCZSZCmCEeiTdA5yoE99Fg_6feb30553eee526cc63fc0b0d25d3077_search-form.png?expiry=1625097600000&hmac=jFZQdcN4rykVahVenyQiCXdG4a8nvh_dzmZxQ_EzLjo)
