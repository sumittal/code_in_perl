# Solution: Merchant's Guide to the Galaxy
use strict;
use warnings;

use Data::Dumper;
use v5.14;
no if ( $] >= 5.018 ), 'warnings' => 'experimental';

my %roman = ( I => 1,
              V => 5,
              X => 10,
              L => 50,
              C => 100,
              D => 500,
              M => 1000
            );
my (%trans_list, %currency_list);

my $error = "I have no idea what you are talking about";
my $regex_assignment = qr/^([a-z]+) is ([I|V|X|L|C|D|M])$/;
my $regex_credits = qr/((?:[a-z]+ )+)([A-Z]\w+) is (\d+) ([A-Z]\w+)$/;
my $regex_howmany= qr/^how many ([a-zA-Z]\w+) is ((?:\w+ )+)([A-Z]\w+) \?$/;
my $regex_howmuch = qr/^how much is ((?:\w+[^0-9] )+)\?$/;

while ( my $line = <STDIN> ) {
    chomp($line);
    last unless $line;

    my $currency = "";

    if( $line =~ /$regex_assignment/ ) {
        $trans_list{$1} = $2;

    } elsif ( $line =~ /$regex_credits/ ) {
        # get currency name
        $currency = $4;
        my @trans = split(/\s+/,$1);

        my $translated_value = get_translated_value(\@trans);
        my $curr = $2;
        my $credits = $3;

        my $value = $credits/$translated_value;

        $currency_list{$curr} = $value;

    } elsif( $line =~ /$regex_howmany/ ) {

        my @trans = split(/\s+/,$2);
        my $translated_value = get_translated_value(\@trans);

        my $curr = $3;
        my $value = 0;
        foreach my $k (keys %currency_list) {
            if($k eq $curr) {
                $value = $currency_list{$k};
            }
        }
        my $total = $translated_value * $value;
        if($total != 0){
            print "$2$3 is $total $currency\n";
        }

    } elsif( $line =~ /$regex_howmuch/ ) {
        my @trans = split(/\s+/,$1);

        my $translated_value = get_translated_value(\@trans);
        if($translated_value != 0){
            print "$1is $translated_value\n";
        }
    } else {
        print "$error\n";
    }

}
print "trans_list - " . Dumper(\%trans_list) . "\n";
print "currency_list - " . Dumper(\%currency_list) . "\n";

sub get_translated_value {
    my $in = shift;
    my @trans = @{$in};

    my $value = 0;
    my @rom;

    for( my $i = 0; $i < scalar(@trans); $i++ ) {
        if(! grep( $trans[$i], keys(%trans_list) ) ) {
            print "Invalid input detected!\n";
            return 0;
        }
        push @rom, $trans_list{$trans[$i]};
    }

    my @src;
    foreach my $str ( @rom ) {
        push(@src,get_value_by_roman($str));
    }

    my @newsrc = substract(\@src);
    foreach my $val ( @newsrc ) {
        $value += $val;
    }
    return $value;
}

sub substract {
    my $in = shift;
    my @numbers = @{$in};
    my $current_element = 0;

    for( my $i = 0; $i < scalar(@numbers) - 1; $i++ ) {
        $current_element = $numbers[$i];
        if( $current_element < $numbers[$i + 1] ) {
            $numbers[$i] = - $current_element;
        }
    }
    return @numbers;
}

sub get_value_by_roman {
    my $str = shift;

    given ($str) {
        when('I') { return $roman{I} }
        when('V') { return $roman{V} }
        when('X') { return $roman{X} }
        when('L') { return $roman{L} }
        when('C') { return $roman{C} }
        when('D') { return $roman{D} }
        when('M') { return $roman{M} }
        default   { return 0 }
    }    
}

