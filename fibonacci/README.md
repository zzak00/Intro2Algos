# Generating function and Fibonacci numbers

According to Wikipedia, [Generating fuctions](https://en.wikipedia.org/wiki/Generating_function) is a way of encoding an infinite sequence of numbers by treating them as the coefficients of a formal power series.

## The Fibonacci Sequence as a Power Series

Recall that the Fibonacci numbers are defined by the recurrence relation <br>
><img src="https://latex.codecogs.com/svg.image?F_{n}=F_{n-1}&plus;F_{n-2}" title="Fn=Fn-1+Fn-2" />
><img src="https://latex.codecogs.com/svg.image?with&space;\hspace{10pt}&space;n\geq&space;0&space;\hspace{35pt}&space;F_{0}=0&space;\hspace{10pt}&space;and&space;\hspace{10pt}&space;F_{1}=1" title="with \hspace{10pt} n\geq 0 \hspace{35pt} F_{0}=0 \hspace{10pt} and \hspace{10pt} F_{1}=1" />

Let us define the generating function for the Fibonacci numbers as the formal power series whose coefficients are the Fibonacci numbers themselves:
><img src="https://latex.codecogs.com/svg.image?\mathfrak{F}(z)=\sum_{0}^{\infty}F_{n}z^{n}" title="\mathfrak{F}(z)=\sum_{0}^{\infty}F_{n}z^{n}" />
and let us prove that: 
><img src="https://latex.codecogs.com/svg.image?\mathfrak{F}(z)=z&plus;z\mathfrak{F}(z)&plus;z^{2}\mathfrak{F}(z)" title="\mathbb{F}(z)=z+z*\mathbb{F}(z)+z^{2}*\mathbb{F}(z)" />
<img src="https://latex.codecogs.com/svg.image?\begin{align*}\mathfrak{F}(z)&space;&space;&space;&space;&&space;=&space;z&space;&plus;&space;\sum_{n&space;=&space;2}^\infty&space;F_n&space;z^n&space;\\&space;&space;&space;&space;&&space;=&space;z&space;&plus;&space;\sum_{n&space;=&space;2}^\infty&space;(F_{n&space;-&space;1}&space;&plus;&space;F_{n&space;-&space;2})&space;z^n&space;\\&space;&space;&space;&space;&&space;=&space;z&space;&plus;&space;\sum_{n&space;=&space;2}^\infty&space;F_{n&space;-&space;1}&space;z^n&space;&plus;&space;\sum_{n&space;=&space;2}^\infty&space;F_{n&space;-&space;2}&space;z^n&space;\\&space;&space;&space;&space;&&space;=&space;z&space;&plus;&space;z&space;\sum_{n&space;=&space;1}^\infty&space;F_n&space;z^n&space;&plus;&space;z^2&space;\sum_{n&space;=&space;0}^\infty&space;F_n&space;z^n\end{align*}" title="\begin{align*}\mathfrak{F}(z) & = z + \sum_{n = 2}^\infty F_n z^n \\ & = z + \sum_{n = 2}^\infty (F_{n - 1} + F_{n - 2}) z^n \\ & = z + \sum_{n = 2}^\infty F_{n - 1} z^n + \sum_{n = 2}^\infty F_{n - 2} z^n \\ & = z + z \sum_{n = 1}^\infty F_n z^n + z^2 \sum_{n = 0}^\infty F_n z^n\end{align*}" />

Solving for the generating function, we get:
  
><img src="https://latex.codecogs.com/svg.image?\begin{align*}\mathfrak{F}(z)&space;&space;&space;&space;&&space;=&space;\frac{z}{1&space;-&space;z&space;-&space;z^2}.\end{align*}" title="\begin{align*}\mathfrak{F}(z) & = \frac{z}{1 - z - z^2}.\end{align*}" />

Next, we need to find roots of the denominator and use partial fraction derivative in order to express the generating function as a power seriesthen match its coefficients term-by-term with the corresponding Fibonacci numbers.

### Roots are: 
><img src="https://latex.codecogs.com/svg.image?\begin{align*}\phi&space;&space;&space;&space;&&space;=&space;\frac{1&space;&plus;&space;\sqrt{5}}{2}&space;=&space;1.61803...&space;\\\bar\phi&space;&space;&space;&space;&&space;=&space;\frac{1&space;-&space;\sqrt{5}}{2}&space;=&space;-0.61803...&space;\\\end{align*}" title="\begin{align*}\phi & = \frac{1 + \sqrt{5}}{2} = 1.61803... \\\bar\phi & = \frac{1 - \sqrt{5}}{2} = -0.61803... \\\end{align*}" />

Therefore:
><img src="https://latex.codecogs.com/svg.image?\begin{align*}\mathfrak{F}(x)&space;&space;&space;&space;&&space;=&space;\frac{1}{\sqrt{5}}&space;\left(&space;\frac{1}{1&space;-\phi&space;z}&space;-&space;\frac{1}{1&space;-\bar\phi&space;z}&space;\right).\end{align*}" title="\begin{align*}\mathfrak{F}(x) & = \frac{1}{\sqrt{5}} \left( \frac{1}{1 -\phi z} - \frac{1}{1 -\bar\phi z} \right).\end{align*}" />

We now wish to express each of these two terms as the sum of a geometric series. Recall that the sum of a geometric series is given by
><img src="https://latex.codecogs.com/svg.image?\begin{align*}\frac{1}{1&space;-&space;x}&space;&space;&space;&space;&&space;=&space;\sum_{n&space;=&space;0}^\infty&space;x^n.\end{align*}" title="\begin{align*}\mathfrak{F}(x) & = \frac{1}{\sqrt{5}} \left( \frac{1}{1 -\phi z} - \frac{1}{1 -\bar\phi z} \right).\end{align*}\begin{align*}\frac{1}{1 - x} & = \sum_{n = 0}^\infty x^n.\end{align*}" />
Note that this infinite sum converges if and only if |x|<1. However, considered as a formal power series, this identity always holds, then:
><img src="https://latex.codecogs.com/svg.image?\begin{align*}\mathfrak{F}(x)&space;&space;&space;&space;&&space;=&space;\frac{1}{\sqrt{5}}&space;\left(&space;\frac{1}{1&space;-&space;\phi&space;z}&space;-&space;\frac{1}{1&space;-&space;\bar\phi&space;z}&space;\right)&space;\\&space;&space;&space;&space;&&space;=&space;\frac{1}{\sqrt{5}}&space;\left(&space;\sum_{n&space;=&space;0}^\infty&space;\phi^n&space;x^n&space;-&space;\sum_{n&space;=&space;0}^\infty&space;\bar\phi^n&space;x^n&space;\right)&space;&space;&space;\\&space;&space;&space;&space;&&space;=&space;\sum_{n&space;=&space;0}^\infty&space;\frac{1}{\sqrt{5}}&space;\left(&space;\phi^n&space;-&space;\bar\phi^n&space;\right)&space;x^n.\end{align*}" title="\begin{align*}\mathfrak{F}(x) & = \frac{1}{\sqrt{5}} \left( \frac{1}{1 - \phi z} - \frac{1}{1 - \bar\phi z} \right) \\ & = \frac{1}{\sqrt{5}} \left( \sum_{n = 0}^\infty \phi^n x^n - \sum_{n = 0}^\infty \bar\phi^n x^n \right) \\ & = \sum_{n = 0}^\infty \frac{1}{\sqrt{5}} \left( \phi^n - \bar\phi^n \right) x^n.\end{align*}" />

Matching the coefficients, we conclude that:
><img src="https://latex.codecogs.com/svg.image?\begin{align*}F_n&space;&space;&space;&space;&&space;=&space;\frac{1}{\sqrt{5}}&space;\left(&space;\phi^n&space;-&space;\bar\phi^n&space;\right).\end{align*}" title="\begin{align*}F_n & = \frac{1}{\sqrt{5}} \left( \phi^n - \bar\phi^n \right).\end{align*}" />

### Observation:
<img src="https://latex.codecogs.com/svg.image?\left|&space;\bar\phi&space;\right|<&space;1" title="\left| \bar\phi \right|< 1" />
as n goes to infinity, phi_bar goes to 0.

At the end, we state that:
><img src="https://latex.codecogs.com/svg.image?\begin{align*}F_n&space;&space;&space;&space;&&space;=&space;\frac{1}{\sqrt{5}}&space;&space;\phi^n&space;\hspace{20pt}&space;for&space;\hspace{10pt}&space;i>0\end{align*}" title="\begin{align*}F_n & = \frac{1}{\sqrt{5}} \phi^n \hspace{20pt} for \hspace{10pt} i>0\end{align*}" /> rounded to the nearest integer.
