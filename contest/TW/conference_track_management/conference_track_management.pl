# Solution: Conference Track Management

# Algorithm
# ---------

#1 Read data from file and create a schedule hash.
#2 validate each string talk, check the time.
#3 sort the list of talks.
#4 find the possible days to schedule conference.
#5 find out the combination which can fill the first half (morning session total time 180 mins)
#6 find out the combination that can fill the evening sessions (180 >= totalSessionTime <= 240)
#7 check if any task remaining in the list if yes then try to fill all the evening session.

use strict;
use warnings;

# read the input file
my $infile = $ARGV[0];

open(my $FH, '<', $infile) or die "cannot open the file- $!\n";
my %schedule;

while(my $line = <$FH> ) {
    chomp($line);
    
    my $time = (split(/\s+/, $line))[-1];
    if( $time =~ /\d+/ ) {
        $time =~ s/(\d+).*/$1/;
    }

    # initialize the %schedule hash
    $schedule{$line} = $time;
}

my @timings = sort { $a <=> $b } keys(%schedule);


