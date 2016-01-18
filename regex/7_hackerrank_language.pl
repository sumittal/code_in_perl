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
