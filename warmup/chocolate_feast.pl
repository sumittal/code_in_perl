#Little Bob loves chocolate, and he goes to a store with $N$N in his pocket. The price of each chocolate is $C$C. The store offers a discount: for every MM wrappers he gives to the store, he gets one chocolate for free. How many chocolates does Bob get to eat?
#
#Input Format: 
#The first line contains the number of test cases, TT. 
#TT lines follow, each of which contains three integers, NN, CC, and MM.
#
#Output Format: 
#Print the total number of chocolates Bob eats.
#
#Constraints: 
#1≤T≤10001≤T≤1000 
#2≤N≤1052≤N≤105 
#1≤C≤N1≤C≤N 
#2≤M≤N2≤M≤N
#
#Sample input
#
#3
#10 2 5
#12 4 4
#6 2 2
#Sample Output
#
#6
#3
#5
#Explanation 
#In the first case, he can buy 5 chocolates with $10 and exchange the 5 wrappers to get one more chocolate. Thus, the total number of chocolates is 6.
#
#In the second case, he can buy 3 chocolates for $12. However, it takes 4 wrappers to get one more chocolate. He can't avail the offer and hence the total number of chocolates remains 3.
#
#In the third case, he can buy 3 chocolates for $6. Now he can exchange 2 of the 3 wrappers and get 1 additional piece of chocolate. Now he can use his 1 unused wrapper and the 1 wrapper of the new piece of chocolate to get one more piece of chocolate. So the total is 5.

#!/usr/bin/perl

$t = <STDIN>;
chomp $t;
for my $a0 ( 0 .. $t - 1 ) {
    $n_temp = <STDIN>;
    @n_arr  = split / /, $n_temp;
    $n      = $n_arr[0];
    chomp $n;
    $c = $n_arr[1];
    chomp $c;
    $m = $n_arr[2];
    chomp $m;

    print chocolate_count( $n, $c, $m ) . "\n";
}

sub chocolate_count {
    my ( $x, $y, $z ) = @_;

    my $eaten = 0;
    my $wraps = 0;

    $wraps = $eaten = int( $x / $y );

    while ( $wraps >= $z ) {
        my $newlyEaten = int( $wraps / $z );
        $eaten += $newlyEaten;

        $wraps %= $z;
        $wraps += $newlyEaten;
    }
    return $eaten;
}
