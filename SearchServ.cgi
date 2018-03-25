#!/usr/bin/perl

package SearchServ; 

use EPrints; 
use EPrints::DataObj::EPrint; 
use Data::Dumper;

sub searchEprint 
    {
    # input keywords and list fieldes for search
#    my( $self, $key, @fields) = @_;
    my( $self, $key, $fields, $date_range, $order) = @_;
    undef @result;
    
#my $test2=  join(',',\@fields);

    # start ssesion Eprints
    my $session = new EPrints::Session; 
    exit( 0 ) unless( defined $session );
    my $ds = $session->get_repository->get_dataset( "archive" ); 

    # Create search expression
    if($order){
 $search = new EPrints::Search(
        satisfy_all => 1,
        session => $session,
	dataset => $ds,
        custom_order => $order);
    }
    else {
 $search = new EPrints::Search(
        satisfy_all => 1,
        session => $session,
	dataset => $ds);

    }
    

##############work##################
#$search->add_field(
#    [                                                                       
#	$ds->get_field('type')
#    ],                                                                      
#       $key,                                                        
#      "IN",                                             
#     "ALL" ); 
#####################################


my @ListFields=@{$fields};                                              
                                                            
my $count=@ListFields;                                                 
                                                            
my $i=0;                                                               
    while ($i<$count)                                                  
    {                                                                  
    # $st=$st."\$ds->get_field(".@ListFields[$i]."),";
     $search->add_field($ds->get_field( @ListFields[$i] ), $key, "IN", "ALL");
     $i++;                                                             
     }                                                                 
#my $query="\$search->add_field( [".$st."],'".$key."','IN','ALL')".';';
#my $query="\$search->add_field( [".$st."],'".$key."', 'ANY','EX')".';';
#$search->add_field($ds->get_field( "creators_name" ), "Archer", "IN", "ALL");

#work
#my $query="\$search->add_field( [".$st."],'".$key."')".';';
#my $query="\$search->add_field( [".$st."],'".$key."')".';';


#  print Dumper ($key);


#eval ($query);

#date restriction
if ($date_range){
$search->add_field($ds->get_field( "date" ), $date_range);
}
     

# Make search
my $list = $search->perform_search; 

# Modify result for return
my @result=();
# Map function to each result
$list->map( 
	        sub {  
                my( $session, $dataset, $eprint ) = @_; 
                push @result, $eprint->get_id;
	        }
	); 
$list->dispose(); 

# Return result

my $listid=SOAP::Data->name('id')->type('ListOfID')->value(\@result); 
#my $test=SOAP::Data->name('test')->value($query); 

undef $key;
undef $fields;
#undef @result;
return ($listid);

#return ($test);	

	
# Tidy up 
$list->dispose();

# End session   
$session->terminate();  
}

package main;

use SOAP::Lite +trace;
use SOAP::Transport::HTTP;

SOAP::Transport::HTTP::CGI
->dispatch_to( 'SearchServ')
->handle;

1;
