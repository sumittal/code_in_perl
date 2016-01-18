use v5.14;
use warnings;

sub findStrings{
    my %r=();
    my($a1,$x)=@_;

    for (my $i=0; $i<scalar(@{$a1});$i++) {

        my @a=split(//,$a1->[$i]);
        next if (scalar(@a) > 2000);

        my $ss='';

        for (my $j=0; $j<=$#a; $j++) {
            $ss = $a[$j] if($a[$j] ne " ");

            $r{$ss}=0;
            for(my $k=$j+1;$k<=$#a;$k++){
                $ss=$ss.$a[$k] if($a[$k] ne " ");
                if(!exists $r{$ss}) {
                    $r{$ss}=0;
                }
            }
        }
    }
    my @sorted = sort(keys%r);

    for (my $i=0;$i<scalar(@{$x});$i++) {
        if($x->[$i] > scalar(@sorted)) {
            print "INVALID\n";
        }else {
            print $sorted[$x->[$i]-1]."\n";
        }
    }
}

# Tail starts here
my $n = <> + 0;
my (@string,@words);
for (my $i=0;$i<$n;$i++) {
    $string[$i] = <>;
    chomp($string[$i]);
}

my $q = <> + 0;

for (my $i=0;$i<$q;$i++) {
    $words[$i] = <>;
    chomp($words[$i]);
}

findStrings(\@string,\@words);
