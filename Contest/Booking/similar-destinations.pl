use strict;
use warnings;

use feature 'say';

my $common_tag = <> + 0;

my ( %input, %output );

while ( my $line = <> ) {
    chomp($line);

    last if ( $line eq '' );
    my @words = split( /[:,]/, $line );
    my $city = shift @words;

    $input{$city} = \@words;

}
my @keys = keys %input;

for ( my $i = 0 ; $i < @keys - 1 ; $i++ ) {
    my @tag1 = @{ $input{ $keys[$i] } };

    for ( my $j = 1 ; $j < @keys ; $j++ ) {

        my @tag2      = @{ $input{ $keys[$j] } };
        my $tag_count = 0;
        my @common;

        if ( $keys[$i] ne $keys[$j] ) {
            foreach my $tag (@tag1) {
                if ( grep( /\b$tag\b/, @tag2 ) ) {
                    ++$tag_count;
                    push @common, $tag;
                }
            }

            if ( $tag_count >= $common_tag ) {
                @common = sort { $a cmp $b } @common;
                my $value = join( ',', @common );
                my @temp = sort { $a cmp $b } ( $keys[$i], $keys[$j] );
                my $key = join( ',', @temp );

                $output{$key} = $value;

            }
        }
    }
}

my %temp;
foreach my $key ( sort { $output{$a} cmp $output{$b} } keys(%output) ) {
    push @{ $temp{ $output{$key} } }, $key;
}

foreach my $key ( sort keys(%temp) ) {
    my @t  = @{ $temp{$key} };
    my $s  = join( ',', @t );
    my @t1 = split( /,/, $s );
    my %h;
    foreach (@t1) {
        $h{$_}++;
    }
    my @f = sort( keys %h );
    my $str = join( ',', sort(@f) );
    say "$str:$key";
}

__DATA__
Problem	Statement
At	Booking.com	we	allow	users	to	search	accommodations	in	over	80,000	destinations	around	the	world.
We	want	to	improve	the	user’s	experience	by	suggesting	destinations	that	are	similar	to	the	ones	they've
just	searched	for.
To	identify	similar	destinations,	we	can	use	tags	entered	by	our	users	during	the	review	process.	These
tags	look	like	this:
london				:	theatre,	museums,	monuments,	food,	parks,	architecture,	nightlife
amsterdam	:	museums,	shopping,	architecture,	nightlife,	cycling,	food,	walking
berlin				:	monuments,	nightlife,	food,	architecture,	city_trip
paris					:	shopping,	food,	monuments,	architecture,	gourmet,	walking,	museums
barcelona	:	architecture,	shopping,	beach,	food,	tapas,	nightlife
Using	these	tags,	we	want	to	create	groups	of	destinations	based	on	tag	similarity.	Destinations	belong
to	a	group	if	they	have	at	least	n	tags	in	common.
For	example,	using	the	above	tags,	the	possible	unique	groups	with	at	least	4	tags	in	common	are	shown
here:
amsterdam,	paris					(5	tags	in	common:	architecture,	food,	museums,	shopping,	walking)
london,	paris								(4	tags	in	common:	architecture,	food,	monuments,	museums)
berlin,	london							(4	tags	in	common:	architecture,	food,	monuments,	nightlife)
amsterdam,	london				(4	tags	in	common:	architecture,	food,	museums,	nightlife)
amsterdam,	barcelona	(4	tags	in	common:	architecture,	food,	nightlife,	shopping)
Input	Format
The	first	line	of	the	input	is	the	minimum	number	of	common	tags	required	to	create	a	group.	This	number
is	always	greater	than	one	and	smaller	than	1000.
The	next	lines	each	specify	a	destination	and	its	tags.	First	there	is	the	destination	name	followed	by	a
colon,	then	the	tags	appear	separated	by	commas.	Destination	names	and	tags	only	contain	alphanumeric
characters	and	underscores.	There	are	no	spaces	in	the	lines.
The	destination	names	and	tags	are	all	in	english.	It	is	safe	to	read	the	input	as	ASCII.	The	destination	names
and	tags	can	have	between	1	and	255	characters.	The	input	can	contain	up	to	1,000	destinations.	And
there	will	be	no	more	than	1,000	unique	tags	in	total.	Each	destination	might	have	up	to	200	tags.
Output	Format
Each	line	of	the	output	starts	with	the	destinations	composing	each	group	sorted	alphabetically	and
separated	by	commas.	Then	a	colon	character	and	then	the	common	tags	of	the	group	also	sorted
alphabetically	and	also	separated	by	commas.
There	should	be	no	spaces	in	the	output.	Groups	must	be	unique,	which	means	that	there	can	not	be	two
or	more	groups	with	the	exact	same	destinations.	The	tags	for	a	group	must	be	all	the	common	tags,	but
groups	with	less	common	tags	than	the	minimum	number	provided	in	the	input	should	not	appear	in
the	output.
The	lines	should	be	sorted	by	the	length	of	the	groups,	with	those	groups	with	more	tags	in	common
appearing	first.	If	two	or	more	groups	have	the	same	number	of	common	tags,	the	lines	should	be	sortedalphabetically.
Sample	Input
4
london:theatre,museums,monuments,food,parks,architecture,nightlife
amsterdam:museums,shopping,architecture,nightlife,cycling,food,walking
berlin:monuments,nightlife,food,architecture,city_trip
paris:shopping,food,monuments,architecture,gourmet,walking,museums
barcelona:architecture,shopping,beach,food,tapas,nightlife	
Sample	Output
amsterdam,paris:architecture,food,museums,shopping,walking
amsterdam,barcelona:architecture,food,nightlife,shopping
amsterdam,london:architecture,food,museums,nightlife
berlin,london:architecture,food,monuments,nightlife
london,paris:architecture,food,monuments,museums
