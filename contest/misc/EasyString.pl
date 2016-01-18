use strict;
use warnings;

# Enter your code here. Read input from STDIN. Print output to STDOUT
my @input;

while (my $input = <STDIN>) {
    chomp($input);
    last unless $input;
    if ($input =~/[^a-z]+/) {
        die "wrong Input";
    }   
    print get_easy_string($input);
}

sub get_easy_string{
    my $string=shift;
    my @s=split('', $string);
    my $length=scalar(@s);
    if($length >= 300000) {
        die 'wrong input length greater than 3*10^5';
    }
    my $mf=1;
    if ($length%2 == 0) {
        $mf=2;
    }   
    my $c=0;
    for(my $i=0; $i<=$#s; $i+=$mf) {
        my $li=$i+$mf-1;
        next if($li%2 ==1 and $mf==1);
        my $w=join('',@s[0..$li]);
        my $ni=($length-$li-1)/2+$li;
        my $y1=join('', @s[$li+1..$ni]);
        my $y2=join('', @s[$ni+1..$#s]);
        next if($y1 eq '');
        next if($y1 ne $y2);

        for my $l("$w$y1$y2" , "$y1$w$y2", "$y1$y2$w" ) 
        {
            if ($l eq $string) {
                $c++;
            }
        }
    }   
    return $c; 
}
