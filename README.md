# Reddit Title Generator
Python program to generate (barely coherent!) titles using a Markov Chain implemented with a pandas dataframe from top 1000 reddit posts on any subreddit.<br>
<h1>Usage:</h1>
<ul>
<li>Create a reddit bot account and fill in the parameters in redditcrawler.py<br>
<code>reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='',
                     username='',
 password='')</code>
<li>Run redditcrawler.py and enter the subreddit you want to generate the markov chain for that subreddit.</li>
<li>Run sengen.py and enter a subreddit with an available markov chain.</li>
</ul><br>
<h2> Sample </h2>
<ul>
 <li><b>AskReddit:</b><ul><li>What's the most outrageous eating sin you do to be relevant?</li><li>Business tactic that requires anyone under the doctor?</li></ul>
 <li><b>WorldNews:</b><ul><li>United nations press conference wednesday, experts tell meat.</li><li>Mass shootings, clears executive order would stay in ukraine president.</li>
  </ul>
  <li><b>Relationship Advice:</b><ul><li>My [29m] girlfriend [27/f] says I honestly anymore. I slept with a pedofile and [36/m]. What in.</li><li>My gf's (27f) miraculously got his dead bedroom.</li> 
   </ul>
