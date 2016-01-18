use strict;
use warnings;

use v5.10;

my $email = <>;
chomp($email);

#if( $email =~ /\b[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}\b/ ) {
#if( $email =~ /\b([A-Z0-9._+-])+@([A-Z0-9.-])+\.[A-Z]{2,4}\b/ ) {
if( $email =~ /(?:[\w\d\-_\.\+\&]+)@(?:[\w\d\-\.\+\&]{1,}\w+)/ ) {
    say 'VALID';
} else {
    say 'INVALID';
}

