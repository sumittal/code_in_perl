use strict;
use warnings;

# Enter your code here. Read input from STDIN. Print output to STDOUT
my @input;
my $len;

while (my $input = <STDIN>) {
    chomp($input);
    last unless $input;
    $len = length($input);
    if( $len >= 50000 || $len < 1) {
        die "The input length is out of range\n";
    }
    push @input,$input;
}

my $size_of_input = $#input/2;

my $number_of_tests = $input[0];

if( $number_of_tests >= 10 || $number_of_tests < 1) {
    die "Wrong number of test cases\n";
}

if($number_of_tests != $size_of_input) {
    die "Number of test cases are not equal to number of inputs\n"
}

my $next_input = $input[1];

my ($string_length, $number_of_times) = split(/\s+/, $next_input); 
die "$number_of_times should be greater than 0\n" if($number_of_times < 0);

my $string = $input[2];

if($string_length != length($string)){
    die "Length of the string is not correct";
}
my %occurance;
my @chars = split(//,$string);
foreach my $char (@chars) {
    $occurance{$char} += 1;
}

my $flag = 1;
foreach my $c ( sort { $occurance{$b} <=> $occurance{$a} } keys %occurance) {
    if($occurance{$c} > $number_of_times) {
        print "$c";
        $flag = 0;
    }
}

if($flag) {
    print "NONE";
}

END {
    print "\n";
}
