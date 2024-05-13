
// Listen for messages from the popup script or other parts of the extension
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  
  if (request.action === 'analyzeSentiment')  // Check if the message is to analyze sentiment
    {
    
    const tweetText = findTweetText();  // Find the tweet text on the current page
 
    const sentiment = analyzeSentiment(tweetText);    // Analyze the sentiment of the tweet text


    chrome.runtime.sendMessage({       // Send a message to the popup script with the tweet text
      action: 'updateTweet',
      tweet: tweetText,
    });

    // Send a message to the popup script with the sentiment analysis result
    chrome.runtime.sendMessage({
      action: 'updateResult',
      sentiment: sentiment,
    });
  }
});

// Function to find the tweet text on the current page

function findTweetText() {

  const tweetElements = document.querySelectorAll('[data-testid="tweet"]');   // Find all elements that represent tweets
 
  for (const tweetElement of tweetElements)   // Loop through each tweet element
    { 
    const tweetTextElement = tweetElement.querySelector('[lang]'); // Find the element that contains the tweet text
    
    if (tweetTextElement) // If the tweet text element is found, return the inner text (tweet text)
       {
      return tweetTextElement.innerText;
    }
  }
  // If no tweet text is found, return an empty string
  return '';
}

// Function to analyze the sentiment of a given text
function analyzeSentiment(text) {

  // Placeholder sentiment analysis logic
  // Replace with your actual sentiment analysis implementation


  return 'Positive'; // For demonstration purposes, always return 'Positive'
}

















