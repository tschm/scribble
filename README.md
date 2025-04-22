# scribble

[![CodeFactor](https://www.codefactor.io/repository/github/tschm/scribble/badge)](https://www.codefactor.io/repository/github/tschm/scribble)

![Happy Birthday](Happy%20Birthday.png)

I am using this little tool to create wedding name
plates for all guests of my (first) wedding.
The underlying idea is described (and stolen from) here:
<https://www.mathworks.com/matlabcentral/mlc-downloads/downloads/submissions/23972/versions/22/previews/chebfun/examples/fun/html/Birthday.html>

However, I do not use Chebyshev polynomials as chebfun is very much a Matlab project.
Unfortunately I do not own a license.
Each letter is here a sequence of points with lines in between them.
Each such segment is discretized using n=100 points. An analytic function is
then applied to create some stunning effects on size,
orientation and position of all letters in a name.
