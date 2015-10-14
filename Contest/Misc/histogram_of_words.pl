use strict;
use warnings;

use Data::Dumper;
use v5.14;

my $file = $ARGV[0];
say "file - $file";

my ($FH, %h);

if(-e $file) {
    if(-r $file) {
        open($FH, '<', $file);
    }
} else {
    die "file does not exist $!";
}

while(<$FH>) {
    chomp;
    map {$h{$_}++} split(//);
}

close($FH);
say Dumper(\%h);

say "Histogram in alphabetically order -";
foreach my $ch (sort {$a cmp $b} keys(%h)) {
    next if $h{$ch} <= 0;
    my $stars = '*' x $h{$ch};
    say "$stars$ch";
}

say "Histogram in ordered by count -";
foreach my $ch (sort {$h{$a} <=> $h{$b}} keys(%h)) {
    next if $h{$ch} <= 0;
    next if $h{$ch} > 80;
    my $stars = '*' x $h{$ch};
    say "$stars$ch";
}

__DATA__
You have the file with word at a single line. 
#input sample file 
abactor 
abaculus 
abacus 
Abadite 
. 
. 
Zyrenian 

#Output 
******************************************************************a 
*************b 
**********************************c 
**********************d 
*******************************************************************************e 

a) you have to count the character and create a histogram in alphabetical order. 
b) now you have to produce a histogram with max 80 character in line in reference to max count 
c) now same out based histrogram based on the character count
                                                                         
