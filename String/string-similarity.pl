use strict;
use warnings;

my $T = <> + 0;
my (@input,%count,%suffixes,@copy);

foreach (1 .. $T) {
    my $str = <>;
    chomp($str);

    push @input, $str;
    push @copy, $str;
}

foreach my $word ( @input ) {
    my $orig = $word;
    push @{$suffixes{$orig}},$orig;

    while(length($word)){
        substr($word, 0, 1) = "";
        push @{$suffixes{$orig}},$word if($word ne '');
    }
}

foreach my $key (keys %suffixes) {
    my @temp = @{$suffixes{$key}};

    my $count = 0;
    foreach my $w (@temp) {
        my $orig_key = $key;
        my $match = 0;

        while(length($w)) {

            if(substr($orig_key, 0, 1) eq substr($w, 0, 1) ) {
                substr($orig_key, 0, 1) = "";
                substr($w, 0, 1) = "";
                $match += 1;
            } else {
               last;
            }
        }
        $count += $match;
    }
    $count{$key} = $count;
}

foreach (@copy) {
    print $count{$_} . "\n";
}

__DATA__
Problem Statement

For two strings A and B, we define the similarity of the strings to be the length of the longest prefix common to both strings. For example, the similarity of strings "abc" and "abd" is 2, while the similarity of strings "aaa" and "aaab" is 3.

Calculate the sum of similarities of a string S with each of it's suffixes.

Input: 
The first line contains the number of test cases T. Each of the next T lines contains a string each.

Output: 
Output T lines containing the answer for the corresponding test case.

Constraints: 
1 <= T <= 10 
The length of each string is at most 100000 and contains only lower case characters.

Sample Input:

2
ababaa  
aa
Sample Output:

11  
3
Explanation: 
For the first case, the suffixes of the string are "ababaa", "babaa", "abaa", "baa", "aa" and "a". The similarities of these strings with the string "ababaa" are 6,0,3,0,1, & 1 respectively. Thus, the answer is 6 + 0 + 3 + 0 + 1 + 1 = 11.

For the second case, the answer is 2 + 1 = 3.
