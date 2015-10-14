# Enter your code here. Read input from STDIN. Print output to STDOUT
use strict;
use warnings;

my %mins = (
    1  => "one minute",
    2  => "two minutes",
    3  => "three minutes",
    4  => "four minutes",
    5  => "five minutes",
    6  => "six minutes",
    7  => "seven minutes",
    8  => "eight minutes",
    9  => "nine minutes",
    10 => "ten minutes",
    11 => "eleven minutes",
    12 => "twelve minutes",
    13 => "thirteen minutes",
    14 => "fourteen minutes",
    15 => "quarter",
    16 => "sixteen minutes",
    17 => "seventeen minutes",
    18 => "eighteen minutes",
    19 => "nineteen minutes",
    20 => "twenty minutes",
    21 => "twenty one minutes",
    22 => "twenty two minutes",
    23 => "twenty three minutes",
    24 => "twenty four minutes",
    25 => "twenty five minutes",
    26 => "twenty six minutes",
    27 => "twenty seven minutes",
    28 => "twenty eight minutes",
    29 => "twenty nine minutes",
    30 => "half"
);

my %hours = (
    1  => "one",
    2  => "two",
    3  => "three",
    4  => "four",
    5  => "five",
    6  => "six",
    7  => "seven",
    8  => "eight",
    9  => "nine",
    10 => "ten",
    11 => "eleven",
    12 => "twelve",
    13 => "one"
);

my $hh = <> + 0;
my $mm = <> + 0;

if( $mm == 0 ) {
    print $hours{$hh} . " o' clock";
} elsif( $mm <= 30 ){
    print $mins{$mm} . " past " . $hours{$hh};
} elsif( $mm > 30 ) {
    print $mins{60 - $mm} . " to " . $hours{$hh + 1};
}

__DATA__
Problem Statement

Given the time in numerals we may convert it into words, as shown below:

5:005:015:105:305:405:455:475:28→ five o' clock→ one minute past five→ ten minutes past five→ half past five→ twenty minutes to six→ quarter to six→ thirteen minutes to six→ twenty eight minutes past five
Write a program which prints the time in words for the input given in the format mentioned above.

Input Format

There will be two lines of input:
H, representing the hours
M, representing the minutes

Constraints
1≤H<12
0≤M<60
Output Format

Display the time in words.

Sample Input

5  
47  
Sample Output

thirteen minutes to six
