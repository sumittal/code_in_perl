use v5.14;
use warnings;

my $n = <> + 0;
my $string = 'C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA: ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART: GROOVY:OBJECTIVEC';

foreach ( 1 .. $n) {
    my $line = <>;
    chomp($line);

    my $lang = (split(/\s/,$line))[1];

    if($string =~ /\b$lang\b/i) {
        say "VALID";
    } else {
        say "INVALID";
    }
}

# Problem statement
__DATA__
Every submission at HackerRank has a field called language which indicates the programming language which a hacker used to code his solution.

C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA: ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART: GROOVY:OBJECTIVEC

Sometimes, error-prone API requests can have an invalid language field. Could you find out if a given submission has a valid language field or not?

Input Format

First line contains N. N API requests follow, each in a newline. Each request has an integer api_id and a string language which are the request parameters placed by the an API request.

Constraints

1 <= N <= 100  
10^4 <= api_id < 10^5  
a valid language is any of the languages listed above (case sensitive):

Output Format

For every api request given in input, print "VALID" if it has a valid language string in it or print "INVALID" otherwise.

Sample Input

3
11011 LUA
11022 BRAINFUCK
11044 X
Sample Output

VALID
VALID
INVALID
