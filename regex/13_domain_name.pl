# Enter your code here. Read input from STDIN. Print output to STDOUT
use v5.14;
use warnings;

my $n = <> + 0;
my (%hash,@matches);

foreach (1 .. $n) {
    my $line = <>;
    chomp($line);

    if($line =~ /(?:(?:https?|ftp|file|):\/\/)?(?:ww[w\d]\.)?((?:[\-A-Z0-9]+\.)*[\-a-zA-Z0-9]+\.[A-Z0-9]+(?:[A-Z0-9]+)?)/gi) {
        $hash{$1} = 1;
#        say $1;
    } 
}

my @final = sort { $a cmp $b } keys %hash;
my $output = join(";",@final);
say $output;

