## Project 04: Stock Portfolio

This is only a front-end project. So, no back-end (NO DJANGO).

You must implement this project using HTML, CSS, JavaScript, Bootstrap (or Foundation, if you know it). You can also use a javascript library for a date picker (you can use this one https://github.com/thedatepicker/thedatepicker or another of your preference). DO NOT use other JavaScript libraries.

You must develop an application to create one stock portfolio with an initial amount. Select the stocks you have invested in with the number of shares bought and the date (in the past, but not more than 10 years ago). Then, calculate the daily history value of the portfolios and the P&L (profit and loss).
**OPTIONAL:** If you finish everything required for the project and want a more complex challenge, create multiple portfolios with an initial amount for each.

### Data Source:
You must use twelve data API: (https://rapidapi.com/twelvedata/api/twelve-data1) through rapidapi.com

Sign up with your stuy Google account on rapidapi.com

Then, on the twelve data on rapidapi, go to pricing and choose the Basic subscription (free, https://rapidapi.com/twelvedata/api/twelve-data1/pricing).

You will get 800 requests per day, 8 requests per minute. This will be more than enough for the development of this project. Rapidapi will set up your credentials instantly; you will get your API key and your API host. You will also get code snippets for each endpoint. Select JavaScript and fetch for an example of the query you can use. You will also get an example response.

The endpoints that you must use are:

- Get stocks list (reference data) => Conditions: exchange name: NYSE and NASDAQ
- Get time series (core data) => Conditions: symbol from NYSE or NASDAQ, the interval is 1 day and outputsize 5000 (the maximum, https://twelvedata.com/docs#time-series)
  
When you open your application in the browser, it will ask the user to enter the API key and API host. You can save this information in a cookie, so when you reload the page, it will look for this information in the cookie, so it will not ask for the user input again. Keep a link in the header to open a modal with a form in Bootstrap (https://getbootstrap.com/docs/5.0/components/modal/) to edit the API key and host if we want to change it, and then save this info into the cookie.

### Web page structure:

Your web page should include a header, a portfolio configuration, and a portfolio result.

**Header:**

- Be creative in adding a header to your webpage (but do not spend much time on this; it is not very important).
- Have a link to open a modal with a form in Bootstrap (https://getbootstrap.com/docs/5.0/components/modal/) to edit the API key and host stored in the cookie.
Portfolio configuration:
- Set up an initial amount (cash, in dollars. As the stocks chosen are from NYSE and NASDAQ, everything is in US dollars).
- Have a button to add a stock.
Once a new stock is created, ask the user to choose the stock name and enter the number of shares and the stock purchase date (use the JS datepicker).

**Portfolio result:**

- Have a button to calculate the portfolio result.
- In the portfolio result section, you must display a table with the date in descending order (the most recent day, first), the portfolio's value, and the P&L.
- If you add new stocks to the portfolio configuration and recalculate the portfolio result, do not ask for the data of stocks that were there before. You must get the data for only new stocks on your list.

**Development Features:**

You must build most of the HTML in JavaScript and update it into the DOM.

When the user opens the web page, your code gets the API key and host (from the user input or from the cookie if it is there), and right away, it should ask for the list of stocks (NYSE and NASDAQ) and save it using JavaScript. You will not ask for this data again unless the user reloads the web page. So, this is a one-time query in the application's lifetime (when we reload the page, the application starts fresh).

It's the same thing when you ask for the stock data (time series). Once you perform a query for it, you save it using JavaScript. So, when you click on the button to get the portfolio result, your code should check if your application has the data for that stock and do the request on the API only if the stock is not present in the JavaScript data.

Also, take into consideration that your JavaScript can only do 8 requests per minute, so save the time for the last 8 requests, and your code will have to wait until it can do another query if you have reached the limit. If your code is waiting until it can do another query, please inform the user with a modal (BootStrap).

Your application needs to work on a mobile screen or a desktop screen. Use Bootstrap for these constraints. This is the priority order of this project (the first is higher priority):

1. JavaScript

2. Bootstrap (working on mobile and desktop screens)

3. CSS (you can use Bootstrap for that or create your own CSS file)

I want everybody in the group to be involved in the JavaScript coding part. 

Create a detailed log to track the team members' work. Log your tasks indicating the date you developed those tasks. Also, include the decisions made by the group after
each time you have a meeting. Upload this log to GitHub.

Projects should be available on GitHub. Please create branches. So I can see the logs and check the team members' activity. The project manager should share the project
repository with the teacher.

If you have any doubt, ask me during class.


