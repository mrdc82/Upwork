import requests
from bs4 import BeautifulSoup

def save_website_text_to_file(url, filename):
    # Send a request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the website content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the text from the website
        text = soup.get_text()
        
        # Save the text to a file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
        
        print(f"Website text has been saved to {filename}")
    else:
        print(f"Failed to retrieve the website. Status code: {response.status_code}")

# Ask the user for the URL and output file name
url = input("Enter the URL of the website: ")
filename = input("Enter the name of the output text file (e.g., output.txt): ")

# Save the website text to the specified file
save_website_text_to_file(url, filename)
