use v5.14;
use warnings;

use Date::Calc qw/Delta_Days/;

my $fdate = <>;
chomp($fdate);
my $sdate = <>;
chomp($sdate);

my $fine;
my $diff;

my ( $d1, $m1, $y1 ) = split( / /, $fdate );
my ( $d2, $m2, $y2 ) = split( / /, $sdate );

my @f1 = ( $y1, $m1, $d1 );
my @f2 = ( $y2, $m2, $d2 );

if ( ( $d1 <= $d2 ) && ( $m1 <= $m2 ) && ( $y1 <= $y2 ) ) {
    $fine = 0;
}
elsif ( ( $d1 > $d2 ) && ( $y1 == $y2 ) && ( $m1 == $m2 ) ) {
    $fine = 15 * ( $d1 - $d2 );
}
elsif ( ( $m1 > $m2 ) && ( $y1 == $y2 ) ) {
    $diff = Delta_Days( @f2, @f1 );
    $fine = 500 * ( $m1 - $m2 );
}
elsif ( $y1 > $y2 ) {
    $diff = Delta_Days( @f2, @f1 );
    $fine = 10000 * ( $y1 - $y2 );
}

say $fine;

__DATA__
Problem Statement

The Head Librarian at a library wants you to make a program that calculates the fine for returning the book after the return date. You are given the actual and the expected return dates. Calculate the fine as follows:

If the book is returned on or before the expected return date, no fine will be charged, in other words fine is 0.
If the book is returned in the same calendar month as the expected return date, Fine = 15 Hackos × Number of late days
If the book is not returned in the same calendar month but in the same calendar year as the expected return date, Fine = 500 Hackos × Number of late months
If the book is not returned in the same calendar year, the fine is fixed at 10000 Hackos.
Input Format

You are given the actual and the expected return dates in D M Y format respectively. There are two lines of input. The first line contains the D M Y values for the actual return date and the next line contains the D M Y values for the expected return date.

Constraints 
1≤D≤31 
1≤M≤12 
1≤Y≤3000
Output Format

Output a single value equal to the fine.

Sample Input

9 6 2015
6 6 2015
Sample Output

45
Explanation

Since the actual date is 3 days later than expected, fine is calculated as 15×3=45 Hackos.
