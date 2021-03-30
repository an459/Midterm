<?php
session_start();

error_reporting(E_ERROR | E_WARNING | E_PARSE | E_NOTICE);  
ini_set('display_errors' , 1);

include (  "account2.php"     ) ;
$connection = mysqli_connect($hostname, $username, $password, $dbname);
        
        if (!$connection){
            echo "Error connecting to database -MASTER: ".$connection->connect_errno.PHP_EOL; //
            exit();
        }

print "Successfully connected to MySQL.<br><br><br>";

mysqli_select_db( $connection, $dbname ); 

include "myfunctions.php";

$username = safe("username") ;
$password = safe("password") ;

if (! authenticate ($username, $password) ) 
{
	echo "<br>Invalid cred." ; 
	header ( "refresh: 2 ; url = login.html ");
	exit();
}
else 								
{
	echo "<br>Valid cred." ; 
	$_SESSION ["logged"] = true ;
	$_SESSION ["ucid"] = $ucid ;
	header ( "refresh: 2 ; url = landingpage.php ");
	exit();
}

print "<br>Bye" ;

?>
