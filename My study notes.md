**Learning Materials from Prof. Wolfram Burgard**  
[University of Freiburg](http://ais.informatik.uni-freiburg.de/teaching/ss18/robotics/)

**Recommended reading order**  
* Chap. 2 &rArr; Chap. 7,8 &rArr; Chap. 3,4,5,6  
* Chap. 14 can be read early
---------------------  
# chapter 2  

+ To simplify notation, usually omit explicit mention of the random variable whenever possible:  
<img src="https://latex.codecogs.com/svg.latex?p(X=x)\rightarrow&space;p(x)" title="p(X=x)\rightarrow p(x)" />  

+ Unless explicitly stated, we assume all continuous random variables possess PDFs, a common density functuion is a 1-d normal distribution with mean <img src="https://latex.codecogs.com/svg.latex?\inline&space;\mu" title="\mu" /> and variance <img src="https://latex.codecogs.com/svg.latex?\inline&space;\sigma&space;^{2}" title="\sigma ^{2}" />  

+ **Theorem of total probability**:　　

+ **Prior probability distribution**, **data**, and **posterior probability distribution**  

+ **normalization constant**  

+ **conditional independence** does not imply **(absolute) independence** and **vice versa** but in special case, they may coincide  

+ Not all random variable possess finite expectation, but those that do not are of no relevance to the material in this book  

+ <img src="https://latex.codecogs.com/svg.latex?\inline&space;Cov[X]=E[X-E[X]]^{2}=E[X^{2}]-E[X]^{2}" title="Cov[X]=E[X-E[X]]^{2}=E[X^{2}]-E[X]^{2}" />  

+ ***entropy***  
The *entropy* of a proability distribution is given by the fllowing expression:  
<img src="https://latex.codecogs.com/svg.latex?\inline&space;H_{p}(x)=E[-log_{2}p(x)]" title="H_{p}(x)=E[-log_{2}p(x)]" />  
<img src="https://latex.codecogs.com/svg.latex?\inline&space;H_{p}(x)=-\sum_{x}p(x)log_{2}p(x)" title="H_{p}(x)=-\sum_{x}p(x)log_{2}p(x)" /> 
(discrete)  
<img src="https://latex.codecogs.com/svg.latex?\inline&space;H_{p}(x)=-\int&space;p(x)log_{2}p(x)dx" title="H_{p}(x)=-\int p(x)log_{2}p(x)dx" />  (continuous)  

+ ## State  
dynamic state, static state  
+   + robot pose  
	+ robot configuration referred to as kinematic state  
	+ robot velocity and the velocities of its joints  are commonly referred to as dynamic state  
	+ location and features of surrounding objects in the environment are also state variables
	+ location and velocitirs of movin objects and people are also potential state varibales
	+ whether a senor is broken can be state variable &rArr; endless state variables

---------------------
# I don't simply watched textbook anymore, I  started to watch the videos from Prof. Wolfram Burgard<br>

## **06.Probabilistic-Motion-Models-Part1 (Chapter. 5 in textbook )**<br>   

+ 2 kinds of distributions:<br>
  + Normal Distribution
  + Triangular Distribution
+ Two types of motion model:
  + Odometry-based
  + Velocity-based (dead reckoning)<br>

+ The atan2 function:<br>

<img src="https://latex.codecogs.com/svg.latex?atan2(y,x)=\left\{\begin{matrix}&space;atan(y/x)&space;&&space;if\,&space;x&space;>0\\&space;sign(y)(\pi-atan(\left&space;|&space;y/x&space;\right&space;|)&space;&&space;if\,&space;x<0\\&space;0&space;&&space;if\,&space;x=y=0\\&space;sign(y)\pi/2&space;&&space;if\,&space;x=0,y\neq&space;0&space;\end{matrix}\right" title="atan2(y,x)=\left\{\begin{matrix} atan(y/x) & if\, x >0\\ sign(y)(\pi-atan(\left | y/x \right |) & if\, x<0\\ 0 & if\, x=y=0\\ sign(y)\pi/2 & if\, x=0,y\neq 0 \end{matrix}\right" /><br>

## **07.Probabilistic-Motion-Models-Part2 (Chapter. 5 in textbook )**<br>  

+ Two motion model
Mathematical Derivation in 5.3.3 and 5.4.3
+ Sampling Algorithm 5.3.2 and 5.4.2
+ Map-Consistent Motion Model (Consider all kinds of obstacles...  )