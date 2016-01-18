use v5.14;
use warnings;

my $n = <> + 0;

my (@input,@words,@matches);
foreach (1 .. $n) {
    my $line = <>;
    chomp($line);
    push @input, $line;
}

my $t = <> + 0;
foreach (1 .. $t) {
    my $line = <>;
    chomp($line);
    push @words, $line;
}

my %o;
foreach my $sub (@words) {
    foreach my $string (@input) {
        if(@matches = $string =~ /[^\w] $sub [^\w]?/xg) {
            $o{$sub} += scalar(@matches);
#            print "\n@matches\n";
        } 
    }
}

foreach my $key (@words) {
    say "$o{$key}";
}
