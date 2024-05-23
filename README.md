# CEDS-tools
A local server that contains automation software that is triggered via the company website.

The tools are:

A credit card link generator which will create a credit card link for customers
to pay using the python requests library. Before all the customer information and more
had to be manually typed into the website

A government invoice automator. This automates the recording of all sales on the panama
government system that businesses are required to use for every sale. This uses
selenium webdriver to enter all the information in the government system returning
the invoice id that is kept in the customer database.

The program is all kept within one file "server.py" that will run a local server containing
all the tools. This way the tools are able to be accessed via post requests containing the customer data.
All the customer data is on the business website and this makes it very easy and only requires the user
to click a button.

