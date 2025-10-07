#!/usr/bin/perl

# <body><h1>Hello from Perl CGI!</h1></body></html>";


$title = "holy poop it's perl";
$background = "white";
$font_size_or_something = 20;
# print "Content-type: text/html", "\n\n";
# print "<html><head>", "\n";
# print "<title>$title</title></head>\n";
# print "<body bgcolor = $background>\n";
# print "<h1>ITS FUCKING PERL HOLY SHIT</h1>\n";
# print "great googly moogly it works<br>\n";
# print "</body></html>", "\n";
# exit(0);

# we can also execute bash commands like echo using `echo something blah`
# this notation is how commands get inserted into servers by malicious users.

# perl gives exponentiation operator **
# perl has weird string operators
# perl arrays are dynamic

@array = ("blink-182", "my chemical romance", "fallout boy"); # arrays can have different types within same array
$size = @array; # returns the current size not capacity of the array
# perl supports compareTo operator <=>
# until() loop function which is literally just a !while()

print "Content-type: text/html", "\n\n";
print << "DOC_END";
<HTML><HEAD>\n
<TITLE>$title</TITLE></HEAD>\n
<h1>ITS FLIPPING PERL HOLY POOP</h1>\n
great googly moogly it works<br>\n
and there's slightly better syntax too!<br><br>\n
DOC_END
for ($i = 0; $i < $size; $i++) {
    print "$array[$i]<BR>\n";
}
print "<hr>\n";

#address of operator is \ prepended before $
#to dereference just write 2 dollar signs on a pointer (that already 
#has one dollar sign)

@sorted = sort @array;
foreach $var(@sorted) {
    print "$var<BR\n>";
}

# to make 2D arrays in perl we need to construct an array of references
# anonymous references are a 2D array ostensibly generated at compile time with standard formatting
# ([],[],[])
# named references is the thing where its an array of addresses to 1D arrays
print "<hr>\n";
# hashmaps
%hash_variable = ("key1", "val1", "key2", "val2");
# to add a key
$hash_variable{"key3"} = "val3";
# to extract a value
$variable = $hash_variable{"key1"};
print "<p><ul><li>$variable</ul></p>\n";

foreach $key(keys %hash_variable) {
    print "$key<BR>\n";
}
foreach $val(values %hash_variable) {
    print "$val<BR>\n";
}

# can also do @keys = keys(%hash_variable)
# and @vals = values(%hash_variable)
# delete $hash_variable{key};

print "<hr>\n";
print "<p><ol>\n";
@key = keys(%ENV);
@value = values(%ENV);
for ($i = 0; $i < 2; $i++) {
    print "<li>$key[$i]: $value[$i]</li>";
}

# while (($key, $value) = each(%hash_variable)) {
#     print "<li>$key, $value</li>"
# }
print "<p><ol>\n";
print "OH MY GOSH I MADE THE ALIAS WORK 2";

print "</body></html>\n";
exit(0);
