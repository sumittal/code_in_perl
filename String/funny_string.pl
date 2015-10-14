use v5.14;
use warnings;

my $n = <> + 0;

foreach  (1 .. $n) {
    my $line = <>;
    chomp($line);

    is_funny($line);
}

sub is_funny {
    my $string = shift;

    my $flag = 0;
    my @str = split(//,$string);
    my @rstr = split(//,reverse($string));

    for(my $i = 1; $i <= $#str -1; $i++) {
        my $diff = abs(ord($str[$i]) - ord($str[$i-1]));
        my $rdiff = abs(ord($rstr[$i]) - ord($rstr[$i-1]));

        if( $diff == $rdiff) {
            $flag = 1;
        } else {
           $flag = 0;
           last;
        }
    }
    $flag ? say 'Funny' : say 'Not Funny';
}

__DATA__
Problem Statement

Suppose you have a string S which has length N and is indexed from 0 to N−1. String R is the reverse of the string S. The string S is funny if the condition |Si−Si−1|=|Ri−Ri−1| is true for every i from 1 to N−1.

(Note: Given a string str, stri denotes the ascii value of the ith character (0-indexed) of str. |x| denotes the absolute value of an integer x)

Input Format

First line of the input will contain an integer T. T testcases follow. Each of the next T lines contains one string S.

Constraints

1<=T<=10
2<=length of S<=10000
Output Format

For each string, print Funny or Not Funny in separate lines.

Sample Input

2
acxz
bcxz
Sample Output

Funny
Not Funny
