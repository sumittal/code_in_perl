use 5.014;
use strict;
use warnings;

use LWP::UserAgent;
use JSON::XS;

# declare the variables
my ( $url, $ua, @headers, $response, $content, $word, $requested_url );

# ask user to enter the word
print "Enter the word - ";
$word = <>;
chomp($word);

# url which contains the output
$url =
    'https://en.wiktionary.org/w/api.php?format=json&action=query&titles='
  . $word
  . '&rvprop=content&prop=revisions&redirects=1';

# create the user-agent object
$ua = LWP::UserAgent->new();

@headers = (
    'User-Agent' => "VerbFinder",
    'Accept'     => 'application/json'
);

$response = $ua->get( $url, @headers );
$content = decode_json( $response->decoded_content );

my ($page) = ( keys %{ $content->{query}->{pages} } );
if ( $page eq '-1' ) {
    die "page does not exists\n";
}

my $output = $content->{query}->{pages}->{$page}->{revisions}->[0]->{'*'};

if ( $response->is_success ) {

    # do nothing
}
else {
    die $response->status_line;
}

my ( @all_section, @english_section, @verb_section );

@all_section = split( /\n/m, $output );

my $is_english_section_exists = 0;

foreach my $line (@all_section) {

    if ( $line =~ /^==English==$/ ) {
        $is_english_section_exists = 1;
        next;
    }

    last if ( $line =~ /^==[A-Za-z]/ );
    push @english_section, $line;
}

die "Error: English section does not exist\n"
  unless ($is_english_section_exists);

my $is_verb_section_exists = 0;
foreach my $line (@english_section) {

    if ( $line =~ /^===Verb===$/ ) {
        $is_verb_section_exists = 1;
        push @verb_section, $line;
        next;
    }

    if ($is_verb_section_exists) {
        if ( $line !~ /^==/ ) {
            push @verb_section, $line;
        }
        else {
            last;
        }
    }
}

die "Error: Verb section does not exist\n" unless ($is_verb_section_exists);

foreach my $line (@verb_section) {

    if ( $line =~ /^#\s/ ) {
        print "meaning : $line\n";
        last;
    }
}
