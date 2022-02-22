# Plot
The scripts were written in Python 2.7. 

- **DistFun.py** generate histogram according to the time stamp of post.
- **distLSTMallLabel.py** from the LSTM model annotated entire dataset, calculate the post frequency and label frequency.
- **extractInitPosts.py** extracts text data (title and description) from original json data collected from Reddit and save into list.
- **label.py** contains functions on different label lists, converting numerical label into TRIANGULUM label.
- **liwc2015Dist.py** from LIWC2015 word analysis results on Reddit dataset, calculate the median value.
- **liw2015FeatSelect.py** from LIWC2015 word feature list for each post, select features according to Chi2 and best K.
- **plotDist.py** plots the posts and comments distrition.
- **plotDist_24fig.py** plot the post and comments distributions for the 3 TRIANGULUM products in one page. 
- **plotDist_24fig_year_.py** plot the post and comments yearly distributions for the 3 TRIANGULUM products in one page. 
- **plotDist_largeData.py** for large dataset such as r/trees, it extremely slow to load data and plot directly. This script calculate intermediate values and use them to plot.
- **plotLSTMpred.py** plot products Tobacco, Marijuna, Vaping time variantion from LSTM prediction on entire dataset.
- **plotLSTMpre_year.py** plot products Tobacco, Marijuna, Vaping yearly variantion from LSTM prediction on entire dataset.
- **plotLSTMpredSimple_year.py** simplified version: plot products Tobacco, Marijuna, Vaping time variantion from LSTM prediction on entire dataset.
- **responseUser.py** counts the following comments from Json file.
- **subredditStat.py** calculate statictics from Json file: text length, number of comments, total number of users.
- **text2file.py** extracts text from Json and write it to text file.
- **timeLSTMpredDic.py** input LSTM prediction labels on each post and the time stamp of each post, output a dictionary post_time_stamp:list_LSTM_pred_label
- **timeUserList.py** from raw Json data extract a list of authors and a list of time stamps of the posts.
- **tokenizer.py** tokenize the sentences from the Json data.
- **UnixTime.py** time stamp lists and dictionaries. 


