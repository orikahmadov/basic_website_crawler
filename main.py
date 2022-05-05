"""Command line interface for search_Dom. 
 """


from bs4 import BeautifulSoup
import requests, os, sys, re, argparse

def main (): # main function
    #import all modules for sending request and parsing response one line

    terminated =  False #terminated is a boolean variable to check if the program is terminated or not
    options = ["Crawl all paths","Quit"] #options for the user to choose from
    while not terminated: #while loop to keep the progr
        #ask the user to choose an option
        print("Choose an option: ")
        for i in range(len(options)):
            print(f"{i+1}. {options[i]}")
        choice = input("Enter your choice: ")
        if choice == "1":
            #Call crawl_url function to crawl all the urls of DOM
            url =  input("Enter the url: ") #get the url from the user
            #if the url is not valid, ask the user to enter a valid url
            while not re.match(r'^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&\'\(\)\*\+,;=.]+$', url):
                url = input("Enter a valid url: ")
            #use RE module to check if the url is valid
            if re.match(r'^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&\'\(\)\*\+,;=.]+$', url):
                crawl_url(url)
            else:
                print("Invalid url")

        elif choice == "2":
            #Terminate the program
            terminated = True




def crawl_url(url):
    """Crawls entire DOM of a website and displays them to user 
    then asks if user wants to save file """
    #get the response from the url
    #call another function to check url ending
    check_url(url)
    response = requests.get(url)
    #parse the response
    soup = BeautifulSoup(response.text, 'html.parser')
    #get all the links from the DOM
    links = soup.find_all('a')
    #print all the links to the user
    for i in range(len(links)):
        #check if there is NONE in the link
        if links[i].get('href') != None:
            print(f"{i+1}. {links[i].get('href')}")
    #ask the user if they want to save the file
    save = input("Do you want to save the file? (y/n): ") #ask the user if they want to save the file
    if save == "y": #if the user wants to save the file
        #ask for the name of the file
        file_name = input("Enter the name of the file: ")
        #check if the file name is valid
        while not re.match(r'^[a-zA-Z0-9_]+$', file_name):
            file_name = input("Enter a valid file name: ")
        #save the file
        with open(file_name+".txt", "w") as f:
            for i in range(len(links)):
                #check if there is NONE in the link
                if links[i].get('href') != None:
                    f.write(f"{links[i].get('href')}\n")
        #print the full path to the file
        print(f"File saved to: {os.getcwd()}/{file_name}.txt")
    else:
        print("File not saved")
        

def check_url(url):
    """Checks if the url ends with .com, gov, or org, edu, and if not, adds .com to the url"""
    #check if the url ends with .com, gov, or org, edu then it accepts the url otherwise it adds .com to the url
    [".com", ".gov", ".org", ".edu"] #list of endings
    for i in range(len([".com", ".gov", ".org", ".edu"])):
        if url.endswith([".com", ".gov", ".org", ".edu"][i]):
            return url
        else: #if the url does not end with any of the endings, add .com to the url
            url = url + [".com", ".gov", ".org", ".edu"][i]
            return url
            


        

if __name__ == "__main__":
    main()

    


    