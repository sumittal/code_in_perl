use 5.014;

use strict;
use warnings;


# Suppose the company and it's details is stored in some file
# or table and we have created the hash as mentioned below where
# key denotes the company name and value is array reference
# containing company's stock current price and gain in percentage.
# gain in % = ((Esimated stock price - Current stock price)/Current stock price) * 100
my %info = (
    'A' => [ 200, 25 ],
    'B' => [ 300, 33 ],
    'C' => [ 250, 60 ],
    'D' => [ 100, 20 ],
    'E' => [ 300, 10 ],
    'F' => [ 50,  0 ],
);

print "Enter the money to be invested - ";
my $total_amount = <> + 0;

my ( @stocks, $money );
$money = 0;

# sort hash of hash based on the % value in decending order
foreach my $key ( sort { $info{$b}->[1] <=> $info{$a}->[1] } keys %info ) {

    $money += $info{$key}->[0];

    # iterate and add the stock value in a array
    # if amount exceed than take next stock which can
    # fit under the limit.
    if ( $money < $total_amount ) {
        push @stocks, $key;
    }
    else {
        $money -= $info{$key}->[0];
    }

}

print "stocks to be purchased - @stocks\n";

