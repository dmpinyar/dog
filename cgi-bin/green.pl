#!/usr/bin/perl

print "Content-type: text/html\n\n";
print "<html><head><title>Goodness gracious it works!</title></head>\n";
print "<BODY BGCOLOR = 'white'>\n";
$form_size = $ENV{'CONTENT_LENGTH'};
read (STDIN, $form_data, $form_size);
$form_data =~ s/%([\dA-Fa-f][\dA-Fa-f])/pack ("C", hex($1))/eg;
print <<"DOC_END";
General Information passed to cgi<P>
CONTENT_TYPE: $ENV{'CONTENT_TYPE'}<BR>
CONTENT_LENGTH: $ENV{'CONTENT_LENGTH'}<BR>
QUERY_STRING: $ENV{'QUERY_STRING'}<BR>
REQUEST_METHOD: $ENV{'REQUEST_METHOD'}<BR>
Form Data: $form_data<BR>
DOC_END
($field_name, $name) = split(/=/, $form_data);
$name =~ s/[;<>\(\)\{\}\*\|'`\&\$!#:"\\]/ /g;
$name =~ s/\+/ /g;

print "Name(+ Changed): $name<BR>\n";
print "</BODY></HTML>\n";
exit(0);