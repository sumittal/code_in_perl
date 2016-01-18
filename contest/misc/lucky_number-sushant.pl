my $input=<STDIN>;
my @d=split(/\s+/,$input);
my %IN_HASH=('6'=>$d[2],'5'=>$d[1], '4'=>$d[0]);
for my $k (reverse sort keys(%IN_HASH)) {
    for(1..$IN_HASH{$k}) {
        $max.=$k;
    }
}
#my $max='6'*$d[2].'5'*$d[1].'4'*$d[0];
#print "MAX $max\n";
my $min=4;
my $sum=0;
sub abcz {
    my ($i)=@_;
    my @r=@d;
    while($i) {
    my $mod=$i%10;
    if ($mod == 4 && $r[0]) {
        $r[0]--;
    } elsif ($mod == 5 && $r[1]){
        $r[1]--;
    }elsif($mod == 6 && $r[2]){
        $r[2]--;
    }else{
        return 0;
    }
    $i/=10;
    }
    return 1;
    }    
#    return 0 if ($i =~ /[^[4-6]]/);
#    my @t=split('',$i);
    #print "\n>>$i#@t#<<";
#    my %h=();
#    foreach my $item (@t) {
       # return 0 if ($item < 4 or $item > 6);
#        $h{$item}++;
#        return 0 if ($h{$item}>$IN_HASH{$item});
#    }
#    return 1;
#}
for ($min;$min<=$max;$min++) {
    #print "\n$min";
    if(abcz($min)) {
    #print "\n$min";
    $sum+=$min;
    }
}

print $sum;
