#!/usr/bin/perl -w
use strict;
use warnings;

my $N = <STDIN>;
my $line;
my @total_lines;
my $word;
my $count = 0;
my $this_count;

for (my $i = 0; $i < $N; $i++)
{
  $line = <STDIN>;
  push (@total_lines, $line);
}

my $C = <STDIN>;
for (my $i = 0; $i < $C; $i++)
{
  $count = 0;
  $word = <STDIN>;
  chomp ($word);
  $word =~ m/(\w+o)u(r\w*)/gi;
  my ($p1, $p2) = ($1, $2);

  foreach (@total_lines)
  {
    $this_count = () = ("$_" =~ m/(${p1}u?${p2})\W/g);
	$count = $count + $this_count;
  }
  print ("$count\n");
}
