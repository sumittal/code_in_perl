use v5.14;
use warnings;

my $nol = <> + 0;

my $r = '\b[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}\b';
my $regex = quotemeta($r);
my %mail;
my @final;

foreach (1 .. $nol) {
    my $line = <>;
    chomp($line);

    if($line =~ /($r)/){
        $mail{$1} += 1;
    } 
}

foreach my $key (sort {$a cmp $b} keys %mail) {
    push @final, $key;
}

my $output = join(';', @final);
say $output;
