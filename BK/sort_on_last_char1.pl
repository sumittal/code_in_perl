use strict;
use Data::Dumper;
use v5.14;

my @users = ( 'Luis', 'Hector', 'Selena', 'Emmanuel', 'Amish' );

my (%f_name,%l_name);

foreach my $w (@users) {
    my $l_ch = lc(substr( reverse($w), 0, 1 ));
    $l_name{$l_ch} = $w;
    my $f_ch = lc(substr(($w, 0, 1)));

    $f_name{$f_ch} = $w;
}

say Dumper(\%f_name);
say "============";
say Dumper(\%l_name);

foreach my $l (keys(%l_name)) {
    foreach my $f (keys(%f_name)) {
        say $f_name{$f} if($l eq $f);
    }
}
