use strict;
use warnings;

my $T = <> + 0;

foreach ( 1 .. $T ) {
    my $s1 = <>;
    chomp($s1);

    my $s2 = <>;
    chomp($s2);

    print find_substring($s1,$s2) . "\n";
}

sub find_substring {
    my ($s1, $s2) = @_;

    my (%h1,%h2);
    $h1{$_}++ for split(//,$s1);
    $h2{$_}++ for split(//,$s2);

    foreach (keys %h1){
        if(exists $h2{$_} && $h2{$_} >= 1) {
            return 'YES';
            last;
        }
    }
    return 'NO';
}
__DATA__
Problem Statement

You are given two strings, A and B. Find if there is a substring that appears in both A and B.

Input Format

Several test cases will be given to you in a single file. The first line of the input will contain a single integer T, the number of test cases.

Then there will be T descriptions of the test cases. Each description contains two lines. The first line contains the string A and the second line contains the string B.

Output Format

For each test case, display YES (in a newline), if there is a common substring. Otherwise, display NO.

Sample Input

2
hello
world
hi
world
Sample Output

YES
NO
Explanation

For the 1st test case, the letter o is common between both strings, hence the answer YES. 
For the 2nd test case, hi and world do not have a common substring, hence the answer NO.
