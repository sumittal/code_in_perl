use strict;

my $input = 'atuslirabocynkebbterasiuaracnbawp';
 
foreach my $word ('car','boat','plane','bus','shuttle') {
    print "$word => " . find_word($word) . "\n";
}

sub find_word {
    my $word = shift;

    my %chars;
    $chars{$_}++ for split('', $input);
    
    my $count = 0;
    while (1) {
        foreach my $letter (split('', $word)) {
            if (exists $chars{$letter} && $chars{$letter} > 0) {
                $chars{$letter}--;
            } else {
                return $count;
            }
        }
        $count++;
    }
}

__DATA__
Provided a set of characters and a list of words, how many of those words can we create from the input characters ?

input:
chars = 'atuslirabocynkebbterasiuaracnbawp'
words = ['car','boat','plane','bus','shuttle']

output:
car => 2
boat => 1
plane => 1
bus => 2
shuttle => 0
