use v5.14;
use warnings;

my $str1 = <>;
my $str2 = <>;

chomp($str1);
chomp($str2);

say anagram($str1,$str2);

sub buildmap {
    my $str = shift;
    my %map;

    my @temp = split(//,$str);
    my @arr = keys %map;

    foreach my $i(0 .. $#temp) {

        if( grep (!/$temp[$i]/, @arr) ) {
            $map{$temp[$i]} = 1;
        } else {
            $map{$temp[$i]} += 1;
        }
    }

    return \%map;
}

sub anagram {
    my $s1 = shift;
    my $s2 = shift;

    my $map1 = buildmap($s1);
    my $map2 = buildmap($s2);

    my $count = 0;

    my @m1 = keys %$map1;
    my @m2 = keys %$map2;

    foreach my $key (@m2) {
        if( grep(!/$key/, @m1) ) {
            $count += $map2->{$key};
        } else {
            $count += max(0, ($map2->{$key} - $map1->{$key}));
        }
    }

    foreach my $key (@m1) {
        if( grep(!/$key/, @m2) ) {
            $count += $map1->{$key};
        } else {
            $count += max(0, ($map1->{$key} - $map2->{$key}));
        }

    return $count;
    }
}

sub max {
    my ($a,$b) = @_;

    if($a > $b) {
        return $a;
    } elsif($b > $a) {
        return $b;
    } else {
        return $a;
    }
}

__DATA__
Alice recently started learning about cryptography and found that anagrams are very useful. Two strings are anagrams of each other if they have same character set and same length. For example strings "bacdc" and "dcbac" are anagrams, while strings "bacdc" and "dcbad" are not.

Alice decides on an encryption scheme involving 2 large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. She need your help in finding out this number.

Given two strings (they can be of same or different length) help her in finding out the minimum number of character deletions required to make two strings anagrams. Any characters can be deleted from any of the strings.

Input Format 
Two lines each containing a string.

Constraints 
1 <= Length of A,B <= 10000 
A and B will only consist of lowercase latin letter.

Output Format 
A single integer which is the number of character deletions.

Sample Input #00:

cde
abc
Sample Output #00:

4
Explanation #00: 
We need to delete 4 characters to make both strings anagram i.e. 'd' and 'e' from first string and 'b' and 'a' from second string.
