use v5.14;
use warnings;

my $count = <> + 0;

my (@input,@words,@matches);
foreach (1 .. $count) {
   my $line = <>;
   chomp($line);
   push @input, $line;
}

my $tmp = <> + 0;
foreach (1 .. $tmp) {
   my $line = <>;
   chomp($line);
   push @words, $line;
}

my %o;
foreach my $sub (@words) {
   foreach my $string (@input) {
        find_word($string , $sub, \$o{$sub});
   }
}

foreach my $key (@words) {
   say "$o{$key}";
}
sub find_word {
  my $string = shift;
  my $char = shift;
  my $count=shift;
  my $c1=$$count;
  my $offset = 0;
  my $result = index($string, $char, $offset);
  my ($x1,$x2)=('','');
  while ($result != -1) {

    $x1=substr($string, $result-1,1) if $result;
    $x2=substr($string,$result+length($char),1);
    if($x1!~/\w/ and $x2!~/\w/) {
        $$count++;
    }
    $offset = $result+1 ;
    $result = index($string, $char, $offset);
  }
}
