# Project Sentinel (Proof of Concept)
Project Sentinel in essence is using machine learning to detect abnormalities in the query sent by the user. My goal is to train a model that is power enough to detect malicious query that is commonly sent by an attacker to do the common attacks such as SQLi or XSS.

# Motivation
I started this side project during one of my project in school. We need to build a vulnerable web application and harden it. I have realized that the traditional methods of blacklisting can be easily bypass. Having heard about the advantages of machine learning, I have decided to incorporate machine learning into my web application. This is a proof of concept project. The goal is to showcase the power of machine learning and my methods of detecting them. If you want to use it in a production server, use it at your own risk.

# General
I have used the library sklearn to train my machine learning model. For my classifier, I have used Support Vector Machines to train the model. The biggest issue I need to solve is how do I make the model understand the query. A research paper from Samrat Ashok Technological Institue Vidisha India talks about using tokens, spliting a query down into multiple parts. The second method I have seen is the use of hashing. However, I find it pointless since hash is a one way function. I would rather create a database and have the web application hash the query and do a search on the database. 

# Problem Faced
I do not want to use the traditional method since it has already been done before. Since machine learning prefer numbers, I also need to find a way to convert all my query into numbers. That is when it hits me and I began encoding them into ascii. However, I was faced with another problem. I intended to use decision tree classifier, however, I ran into two issues. The query cannot fit inside (around 19 bytes of data) and decision tree is not designed for this kind of thing.

# Solution
I went ahead and use support vector machine learning. It is extremely powerful, able to classify datasets on the vector non-linearly. They also allow way more inputs, around 309 characters. This allows me to train most of the query that is being queried. I went online and search for common malicious queries and went to train the model. I also hosted this code on a vitual private server online to receive the data from the web application and return 0 or 1. 

# Result
I have used the industry standard of testing 20% of the data against the 80%. The result is 0.9652 or around 96.52%.

# Issues 
Due to the amount of dataset I have on hand, the data is actual veru biased. It is not balance beetween the malicious and non-malicious query. With more dataset, I believe that this will be even more accurate.


