<h1>Repo for Machine Learning, AI, etc.</h1>

<h3>Perceptron</h3>
<br>
<h4>Usage: perceptron.py &ltinput file&gt</h4>
<p> Perceptron to handle somewhat arbitrary boolean functions. Idea based on 
notes from CS540 A.I. lecture at UW-Madison that detail how to create threshold
and weight updating equations.  If it is not a linearly-seperable function it should enter an infinite loop and stop at my arbitrary endpoint. </p>
<br>
<p> Weights are initialized as random tenths between 0 and 1.  
 Alpha was also chosen arbitrarily, just picked a value similar to a class
example.
<br> Program will complete either once it hits the loop kill or once it sees two iterations of the 4 input combinations that have 100% correct.</p>
