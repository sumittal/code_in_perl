use strict;
use warnings;

my ($pString);
chomp ($pString = <STDIN>);
my (@aSeen) = (0) x 26;
my ($a) = ord('a');
for (split //, $pString) {
  next if $_ eq ' ';
  $aSeen[ord(lc($_)) - $a] = 1;
}
my ($pUnseen) = scalar grep { $_ == 0 } @aSeen;
if ($pUnseen == 0) {
  print STDOUT 'pangram';
} else {
  print STDOUT 'not pangram';
}
