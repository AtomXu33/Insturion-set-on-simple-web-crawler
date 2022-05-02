# Insturion-set-on-simple-web-crawler
This is a instuirtion set on how to build a simple web crawler
Few easy steps help you have your first web crawler

In today’s life, data collection and analysis are needed in every field, but it is impossible to collect a large amount of data by hand, so here comes web crawler. Web Crawler is a program that collect all the information in a certain website you need, it is fully automatic once it is turned on. The process of writing it does not require much skill, as a computer science major freshman, I hope this can help other beginners who want to learn this process.

Level: beginner, with beginner on python and know how HTML file looks like

Time: approximately 15 minutes

you will need: electronic machine with Python 3.9.7(should work with any version of Python)

Step 1: Create an empty python file and name it “HTML Parser”, to create an empty python file, you need to open IDLE and click “file” on the top left corner and click “New File”. Before we start crawling data, we need to process the information first, and HTML Parser is the tool we need.
 

Step 2: import libraries we need, these libraries are python build-in libraries, they are basically providing you the ability to open an URL and read over it. You don’t need to know what’s in it if you just want a simple web crawler.
 

Step 3: write a parser function to read in URLs, this is one of the most important steps. It helps you transfer the contents in a URL into things we can process with(String and chars).
 

Step 4: write a header parser class to find and get all the words inside this HTML file, it can be named differently and do different works depends on what you want.

 

Step 5: write a data collector class to organize data, this class basically takes what you have in your list we created at the beginning and rewrite it for us to use easier.
 

Step 6: write a collector class to collect all the links, since we are not just looking at 1 website, we are also collecting other contents from other website inside this one, we need to find them.
 
Step 7: create an empty python file and name it “firstcrawler”, this is the real crawler we will be using, we are going to use the data we get from HTML Parser and print it on the screen.
 

Step 8: import libraries we need and the Parser we wrote
 

Step 9: write our crawler class, by the crawl function, we could go deeper and deeper inside a website and find out what’s in it., and we analyze the data we receive by the analyze function. 
Step 10: Congratulations! You now have your first web crawler! By running the first Crawler python file you can start using your crawler. 

Tips: This is a very simple crawler that can only crawl limited items(words, links….), do not use this temple for complex tasks.

Troubleshooting: make sure when you call other method, call the right name, otherwise, python would send you an error message.

 
