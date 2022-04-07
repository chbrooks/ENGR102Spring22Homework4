#### HW 4: Basic Web applications
#### Due April 14, 11:59pm.

This is a combo lab/homework. We'll start it together and then you'll wrap it up yourself.

This assignment will be graded using specifications grading.
To get a C, complete tasks 1-5. To get a B, complete tasks 1-7. To get an A, complete all tasks.

To submit your work, please push it back up to your GitHub repo by the deadline. 


To begin, we'll start by building a very simple web client:

1. To begin, we'll open up a URL and read its contents. The fetchURL function does this.
Try running it on http://www.usfca.edu

2. Next, implement printLength. Like fetchURL, it should get the contents of a URL. However, it should print the length of the reply, rather than the reply itself.

3. Then, add a new function called getOutwardLinks. It should take as input a URL and find all the outward links in the page.
An outward link begins with href= - for example: href="https://maps.usfca.edu"

Next, let's set up a simple server.

4. To begin, install flask. Open up a terminal and do:
<pre>pip install flask</pre>

5. The file server.py contains a simple Flask server. Start that up and confirm that it's working. 
You should be able to load the URL http://127.0.0.1:5000/ in your favorite web browser
and see the string hello world!

6. Extend the "hello"  method to return HTML rather than plain text.

7. Let's add two additional routes:
   1. /joke - return a joke.
   2. /recipe - return a recipe


Next, let's add in client-server behavior.

8. First, return to client.py. Modify the client to prompt the user for a word. We'll then attach
that to the end of the URL, like so: 
<pre> http://127.0.0.1:5000/guess/(word)</pre> where (word) is the word being guessed.

Add a /guess route that attaches the guess as a dynamic URL. it should look at the guess and return the word 'correct' if they're the same, and 'incorrect' otherwise

9. Last, let's revisit wordle. Add a '/wordle' route. Have the user provide a 5-letter guess as a dynamic URL. Send that to the server in the 'data' parameter, as above. 
Return the Wordle representation of the guess. Feel free to reuse your code from lab 1!



