Data Cleaning 

Approach
Handling Missing Values
First, I checked how these pieces of data interacted and what they meant for the analysis. Given the limited size of the current dataset, I decided to maintain just the rows with values in all three variables. Without entire rows, it is difficult to make sense of the data.

If the dataset contained more information, such as product_id or event_duration, and a larger sample size, I could have used more advanced ways to fill in the missing values, such as predicting them based on other data, rather than simply removing missing rows.

If I had more access, I would try to fetch the missing data using additional sources. This could have helped improve the dataset.

Finally, it is actually best to handle missing values early in the ETL process and include certain tests to verify that the data is clean before it is loaded into the data warehouse.

Removing Duplicates
I tried to understand whether it was necessary to remove duplicates because, in some business contexts, it may be useful and necessary to keep them. For example, if each event in the provided dataset is expected to occur only once per timestamp, it makes sense to remove them. If not, I would need more fields to understand its uniqueness, i.e., user_session, purchase_amount, activity_type, product_id, device_id, etc., because the timestamp alone will not be enough to distinguish these activities. A user might be adding multiple products to the cart in the same second. The data did not have any duplicates in the end.

Parsing the Timestamp Column into a Proper Datetime Format
To begin, I checked the data type of the timestamp, just in case. Then I used datetime objects, which automatically formatted it into a datetime format. I could have defined a format with format=, but I did not think it was required. I verified the accuracy after running it.

Storing the Cleaned and Transformed Data
I loaded the dataset using Visual Studio Code and cloned my repository from GitHub. Then I saved the result as a CSV, pushed the modifications, and committed them.

How Would You Improve This Pipeline for Production Use?
I would not work with CSV files since the real data is too large to load into memory. They are also less secure, more prone to loss, and not ideal for sustainability and accessibility. A data warehouse would be a better solution than CSVs.

I would absolutely utilize automatic refresh and incremental refreshes. This would result in significant cost savings while also improving performance.

I would manage the missing data and ensure that the events were tracked properly and correctly.

I would integrate additional data sources to increase data integrity and enrich the dataset.

Indexes, cached data, materialized views, and query optimizations can significantly enhance performance.

I would add some alerts to be able to detect the anomalies in the pipeline.

Adding checks in the ETL process to ensure data accuracy, such as confirming that events occur in chronological order.

Additional Insights:
Data Type Check
I changed the data types for better performance after getting rid of NaNs:

user_id is converted to an integer from float64.
activity_type is converted to a category from object.
timestamp, as asked, is converted to datetime from object.
Event Sequence
I also wanted to check whether the logic in the provided dataset is accurate. To do this, I sorted the users by timestamp and checked whether each event followed the expected sequence based on the activity_type.

The expected logic was:

First, the user should log in, then they can view_item, add_to_cart, and purchase.
The user should be adding a product to their cart unless there is a direct purchase option available.
Logout must be the last event.
Ideally, users do not necessarily need to view the item, they can directly add_to_cart and purchase.

After sorting the data frame, I confirmed whether the timestamps were in the correct chronological order. I first verified the index positions before sorting to ensure they were initially in the correct sequence.

Anomalies Detected
After sorting, I noticed some anomalies in the data:

User 101: Made a purchase without logging in first, which suggests missing data.
User 103: The first recorded action is logging out, followed by adding items to the cart without logging back in.
This might indicate data loss, missing data, or that login events are not being tracked properly. This issue needs to be handled as it misrepresents the user journey.

