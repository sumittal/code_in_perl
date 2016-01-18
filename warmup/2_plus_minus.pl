use v5.14;
use warnings;

my $n = <> + 0;
my $lst = <>;
my @list = split(' ',$lst);

my ($p_count, $n_count, $z_count);

foreach(@list) {
    $p_count++ if($_ > 0);
    $n_count++ if($_ < 0);
    $z_count++ if($_ == 0);
}

printf("%.3f\n", $p_count/$n);
printf("%.3f\n", $n_count/$n);
printf("%.3f\n", $z_count/$n);
