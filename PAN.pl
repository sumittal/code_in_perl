use v5.14;
use warnings;

my $n = <> + 0;

foreach ( 1 .. $n) {
    my $line = <>;
    chomp($line);

    if(length($line) == 10) {
        if($line =~ /\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b/) {
            say "YES";
        } else {
             say "NO";
        }
    }
}
__DATA__
The format of the PAN number is below -
<char><char><char><char><char><digit><digit><digit><digit><char>

Your task is to figure out if the PAN number is valid or not. A valid PAN number will have all its letters in uppercase and digits in the same order as listed above.
Constraints

1≤N≤10
Each char is an uppercase letter, i.e., char∈[′A′,′Z′].
Each digit lies between 0 and 9, i.e., digit∈[0,9].
The length of the PAN number is always 10, i.e., length(PAN)=10
Every character in PAN is either char or digit satisfying the above constraints.

Sample output -

YES
NO
NO
