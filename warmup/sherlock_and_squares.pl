#Watson gives two integers (AA and BB) to Sherlock and asks if he can count the number of square integers between AA and BB (both inclusive).
#
#Note: A square integer is an integer which is the square of any integer. For example, 1, 4, 9, and 16 are some of the square integers as they are squares of 1, 2, 3, and 4, respectively.
#
#Input Format 
#The first line contains TT, the number of test cases. TT test cases follow, each in a new line. 
#Each test case contains two space-separated integers denoting AA and BB.
#
#Output Format 
#For each test case, print the required answer in a new line.
#
#Constraints 
#1≤T≤1001≤T≤100 
#1≤A≤B≤1091≤A≤B≤109
#
#Sample Input
#
#2
#3 9
#17 24
#
#Sample output
#2
#0

use POSIX;
$t = <STDIN>;
chomp $t;
for my $a0 ( 0 .. $t - 1 ) {
    $n = <STDIN>;
    chomp $n;
    my ( $A, $B ) = split( /\s+/, $n );
    print count_squares( $A, $B ) . "\n";
}

sub count_squares {
    my ( $a, $b ) = @_;

    $a = ceil( sqrt($a) );
    $b = floor( sqrt($b) );

    return int( $b - $a ) + 1;
}
