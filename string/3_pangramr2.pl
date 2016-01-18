chomp(my $line = <>);

my @array = split(//, $line);
my %hash;
foreach (@array) {
        my $key = lc($_);
        $hash{$key} = 1;
}
my $op = 'pangram';
foreach my $l ('a' .. 'z') {
        unless (defined $hash{$l}) {
                $op = 'not pangram';
                last;
        }
}
print $op;
