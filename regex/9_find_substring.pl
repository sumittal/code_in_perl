use v5.14;
use warnings;

my $n = <> + 0;

my (@input,@subs,@matches);
foreach (1 .. $n) {
    my $line = <>;
    chomp($line);
    push @input, $line;
}

my $t = <> + 0;
foreach (1 .. $t) {
    my $line = <>;
    chomp($line);
    push @subs, $line;
}

foreach my $sub (@subs) {
    foreach my $string (@input) {
        #if(@matches = $string =~ /\b\S+$sub\S+\b/g) {
        if(@matches = $string =~ /\b[a-zA-Z_]+$sub[a-zA-Z_]+\b/g) {
            say scalar(@matches);
        } else {
            say "0";
        }
    }
}


