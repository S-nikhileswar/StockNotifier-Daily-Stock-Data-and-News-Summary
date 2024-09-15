<h1>StockNotifier: Daily Stock Data and News Summary</h1>

<p>
  StockNotifier is a Python-based application designed to send daily stock market data and news summaries via email. 
  It enables users to track stock performance, providing key data such as stock prices and recent news updates, all 
  through an automated email notification system.
</p>

<h2>Project Features</h2>

<h3>1. Stock Data Fetching</h3>
<ul>
  <li>Utilizes the <strong>Alpha Vantage API</strong> to gather detailed stock data.</li>
  <li>Provides key stock details including:
    <ul>
      <li>Opening, closing, high, low prices</li>
      <li>Volume traded</li>
    </ul>
  </li>
  <li>Calculates percentage changes in stock price over:
    <ul>
      <li>One day</li>
      <li>One month</li>
      <li>Three months</li>
    </ul>
  </li>
</ul>

<h3>2. News Summaries</h3>
<ul>
  <li>Uses the <strong>News API</strong> to fetch the latest news related to the company.</li>
  <li>Sends up to three recent news headlines and brief summaries in the notification email.</li>
</ul>

<h3>3. Email Notification</h3>
<ul>
  <li>The email report includes:
    <ul>
      <li>Stock prices (open, high, low, close)</li>
      <li>Percentage changes over daily, monthly, and quarterly periods</li>
      <li>Volume traded</li>
      <li>Recent news articles about the company</li>
    </ul>
  </li>
</ul>

<h3>4. User Interface (UI)</h3>
<ul>
  <li>Simple GUI built with <strong>tkinter</strong>, allowing users to input:
    <ul>
      <li>Company code</li>
      <li>Company name</li>
      <li>Email address to receive notifications</li>
    </ul>
  </li>
</ul>

<h2>System Requirements</h2>
<ul>
  <li><strong>Python</strong> 3.x</li>
  <li><strong>Required Libraries</strong>:
    <ul>
      <li><code>requests</code> for API calls</li>
      <li><code>smtplib</code> for sending emails through Gmail SMTP</li>
      <li><code>tkinter</code> for building the GUI</li>
    </ul>
  </li>
</ul>

<h2>Setup Instructions</h2>

<h3>1. Clone the Repository</h3>
<pre><code>
git clone https://github.com/yourusername/stocknotifier.git
cd stocknotifier
</code></pre>

<h3>2. Install Dependencies</h3>
<p>Ensure you have the <code>requests</code> library installed:</p>
<pre><code>
pip install requests
</code></pre>

<h3>3. Set Up API Keys</h3>
<ul>
  <li>Obtain API keys from the following:
    <ul>
      <li><strong>Alpha Vantage API</strong> (for stock data)</li>
      <li><strong>News API</strong> (for fetching news articles)</li>
    </ul>
  </li>
  <li>Update the code with your API keys.</li>
</ul>

<h3>4. Configure Email Settings</h3>
<ul>
  <li>Generate an app-specific password from your Gmail account.</li>
  <li>Replace the email and password in the mail class with your credentials.</li>
</ul>

<h2>Code Structure</h2>

<ul>
  <li><code>main.py</code>: Core script that handles:
    <ul>
      <li>User input via GUI</li>
      <li>Fetching stock data and news</li>
      <li>Sending email notifications</li>
    </ul>
  </li>
</ul>

<h2>Classes Overview</h2>

<h3>1. <code>mail</code> Class</h3>
<p>Handles sending stock summary emails to the user.</p>

<h3>2. <code>display</code> Class</h3>
<p>Manages the GUI for user input.</p>

<h3>3. <code>information</code> Class</h3>
<p>Fetches stock data and news articles and calculates percentage changes (daily, monthly, quarterly).</p>

<h2>Usage Guide</h2>

<h3>1. Run the Application</h3>
<pre><code>
python main.py
</code></pre>

<h3>2. Input Required Information</h3>
<ul>
  <li>Stock company code (e.g., AAPL for Apple)</li>
  <li>Company name</li>
  <li>Your email address for notifications</li>
</ul>

<h3>3. Receive Email</h3>
<p>The system will fetch stock data, calculate percentage changes, and send a detailed email to your inbox, along with recent news.</p>

<h2>Email Content</h2>

<p>The notification email will include:</p>
<ul>
  <li><strong>Stock Data</strong>:
    <ul>
      <li>Stock name and date of the report</li>
      <li>Opening, highest, lowest, and closing prices</li>
      <li>Volume traded</li>
    </ul>
  </li>
  <li><strong>Percentage Changes</strong>:
    <ul>
      <li>One-day, one-month, and three-month percentage changes</li>
    </ul>
  </li>
  <li><strong>Latest News</strong>:
    <ul>
      <li>Up to three news headlines with brief summaries</li>
    </ul>
  </li>
</ul>

<h2>Potential Enhancements</h2>

<ul>
  <li><strong>Real-Time Updates</strong>: Implement real-time stock tracking with instant notifications for significant price changes.</li>
  <li><strong>Additional Stock Metrics</strong>: Include more financial metrics like P/E ratio, moving averages, etc.</li>
  <li><strong>Enhanced UI</strong>: Improve the GUI for a more polished and user-friendly experience.</li>
</ul>

<h2>Contributions</h2>

<p>Feel free to contribute by submitting issues or pull requests. For suggestions or improvements, reach out via the issue tracker.</p>
