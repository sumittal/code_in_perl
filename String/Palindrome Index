use v5.14;
use warnings;
use strict;

my $T = <> + 0;

foreach ( 1 .. $T ) {
    my $str = <>;
    chomp($str);
    say pindex($str);
}

sub pindex {
    my $str = shift;
    my @str = split(//,$str);

    return '-1' if($str eq reverse($str));
    my $j = $#str;
    my $i = 0;

    while ( $i < $j ) {

        if( $str[$i] eq $str[$j] ){
            $i++; $j--;
        } elsif($str[$i + 1] eq $str[$j] ) {
            return $i;
            break;
        } elsif($str[$i] eq $str[$j - 1] ) {
           return $j;
           break;
        }
    }
    return '-1' if( $j > $i);
}

__DATA__
Problem Statement

You are given a string of lower case letters. Your task is to figure out the index of the character on whose removal it will make the string a palindrome. There will always be a valid solution. 

In case the string is already a palindrome, then -1 is also a valid answer along with possible indices.

Input Format

The first line contains T, i.e. the number of test cases.
T lines follow, each containing a string.

Output Format

Print the position (0 index) of the letter by removing which the string turns into a palindrome. For a string, such as

bcbc
we can remove b at index 0 or c at index 3. Both answers are accepted.

Constraints 
1≤T≤20 
1≤ length of string ≤100005 
All characters are Latin lower case indexed.

Sample Input

3
aaab
baa
aaa
Sample Output

3
0
-1
Explanation

In the given input, T = 3,

For input aaab, we can see that removing b from the string makes the string a palindrome, hence the position 3.
For input baa, removing b from the string makes the string palindrome, hence the position 0.
As the string aaa is already a palindrome, you can output 0, 1 or 2 as removal of any of the characters still maintains the palindrome property. Or you can print -1 as this is already a palindrome.
Custom Checker logic

https://gist.github.com/shashank21j/58df3865a95bf960092c
