use strict;
use warnings;

my $N = <> + 0;

my @rocks;
foreach ( 1 .. $N ) {
    my $in = <>;
    chomp($in);
    push @rocks, $in;
}
print get_gem_element(\@rocks) . "\n";

sub get_gem_element {
    my $p = shift;

    my @unique;
    foreach(@$p) {
        push @unique, remove_duplicates($_);
    }

    my %h;
    foreach my $word (@unique) {
        $h{$_}++ for split(//,$word);
    }

    my $count = 0;
    foreach my $k (keys(%h)){
        $count++ if($h{$k} == @unique);
    }

    return $count;
}

sub remove_duplicates {
    my $str = shift;
    my %h;

    $h{$_}++ for split(//,$str);

    my $t = join('', keys %h);

    return $t;
}

__DATA__
Problem Statement

John has discovered various rocks. Each rock is composed of various elements, and each element is represented by a lower-case Latin letter from 'a' to 'z'. An element can be present multiple times in a rock. An element is called a gem-element if it occurs at least once in each of the rocks.

Given the list of N rocks with their compositions, display the number of gem-elements that exist in those rocks.

Input Format

The first line consists of an integer, N, the number of rocks. 
Each of the next N lines contains a rock's composition. Each composition consists of lower-case letters of English alphabet.

Constraints 
1≤N≤100 
Each composition consists of only lower-case Latin letters ('a'-'z'). 
1≤ length of each composition ≤100
Output Format

Print the number of gem-elements that are common in these rocks. If there are none, print 0.

Sample Input

3
abcdde
baccd
eeabg

Sample Output

2
