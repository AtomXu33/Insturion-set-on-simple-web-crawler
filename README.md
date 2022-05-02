# Insturion-set-on-simple-web-crawler
This is a instuirtion set on how to build a simple web crawler
Few easy steps help you have your first web crawler

In today’s life, data collection and analysis are needed in every field, but it is impossible to collect a large amount of data by hand, so here comes web crawler. Web Crawler is a program that collect all the information in a certain website you need, it is fully automatic once it is turned on. The process of writing it does not require much skill, as a computer science major freshman, I hope this can help other beginners who want to learn this process.

Level: beginner, with beginner on python and know how HTML file looks like

Time: approximately 15 minutes

you will need: electronic machine with Python 3.9.7(should work with any version of Python)

Step 1: Create an empty python file and name it “HTML Parser”, to create an empty python file, you need to open IDLE and click “file” on the top left corner and click “New File”. Before we start crawling data, we need to process the information first, and HTML Parser is the tool we need.
![htmlParser py - C__Users_26394_Desktop_htmlParser py (3 9 7) 2022_4_26 14_09_35](https://user-images.githubusercontent.com/46579637/166173090-5278edbf-b0f1-4fec-94d0-3a788076eeaa.png)
 

Step 2: import libraries we need, these libraries are python build-in libraries, they are basically providing you the ability to open an URL and read over it. You don’t need to know what’s in it if you just want a simple web crawler.
![htmlParser py - C__Users_26394_Desktop_htmlParser py (3 9 7) 2022_4_26 14_09_46](https://user-images.githubusercontent.com/46579637/166173091-2f5a47b9-61ff-4a5a-80db-d73c71b7899a.png)

Step 3: write a parser function to read in URLs, this is one of the most important steps. It helps you transfer the contents in a URL into things we can process with(String and chars).
![htmlParser py - C__Users_26394_Desktop_htmlParser py (3 9 7) 2022_4_26 14_09_56](https://user-images.githubusercontent.com/46579637/166173085-722a491e-102e-4436-853b-682060b258ed.png)
 

Step 4: write a header parser class to find and get all the words inside this HTML file, it can be named differently and do different works depends on what you want.
![htmlParser py - C__Users_26394_Desktop_htmlParser py (3 9 7) 2022_4_26 14_10_45](https://user-images.githubusercontent.com/46579637/166173086-00cbcbd4-0807-4051-aa7f-689b7087877d.png)![Picture1](https://user-images.githubusercontent.com/46579637/166173306-74100e0c-691c-49ef-9a73-c4c5e6ba18d4.png)

 

Step 5: write a data collector class to organize data, this class basically takes what you have in your list we created at the beginning and rewrite it for us to use easier.
![htmlParser py - C__Users_26394_Desktop_htmlParser py (3 9 7) 2022_4_26 14_11_07](https://user-images.githubusercontent.com/46579637/166173088-0a237574-913c-44d9-8293-758a61034056.png)

Step 6: write a collector class to collect all the links, since we are not just looking at 1 website, we are also collecting other contents from other website inside this one, we need to find them.
![htmlParser py - C__Users_26394_Desktop_htmlParser py (3 9 7) 2022_4_26 14_11_26](https://user-images.githubusercontent.com/46579637/166173096-c013e828-5006-426b-a8a5-844a86b0f7d1.png)
 
Step 7: create an empty python file and name it “firstcrawler”, this is the real crawler we will be using, we are going to use the data we get from HTML Parser and print it on the screen.
![_firstCrawler py - C__Users_26394_Desktop_firstCrawler py (3 9 7)_ 2022_4_26 14_12_13](https://user-images.githubusercontent.com/46579637/166173100-665366b1-c56b-4f4e-8173-5f5b45de6c2b.png)
 

Step 8: import libraries we need and the Parser we wrote
![_firstCrawler py - C__Users_26394_Desktop_firstCrawler py (3 9 7)_ 2022_4_26 14_12_22](https://user-images.githubusercontent.com/46579637/166173101-4aeb4e56-d750-481d-bc3d-c30883d68847.png)

Step 9: write our crawler class, by the crawl function, we could go deeper and deeper inside a website and find out what’s in it., and we analyze the data we receive by the analyze function. 
![_firstCrawler py - C__Users_26394_Desktop_firstCrawler py (3 9 7)_ 2022_4_26 14_12_30](https://user-images.githubusercontent.com/46579637/166173102-dc649460-8a57-4a40-91be-0b5add311de3.png)


Step 10: Congratulations! You now have your first web crawler! By running the first Crawler python file you can start using your crawler. 
![Picture1](https://user-images.githubusercontent.com/46579637/166173314-643cb36c-e455-4b41-a65f-f39217e88db1.png)
Tips: This is a very simple crawler that can only crawl limited items(words, links….), do not use this temple for complex tasks.

Troubleshooting: make sure when you call other method, call the right name, otherwise, python would send you an error message.

 










